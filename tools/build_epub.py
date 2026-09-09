"""Build standalone valid EPUB 3 from chapters/*.md - pure Python stdlib.

No third-party dependencies required. Produces a compliant EPUB archive
with valid mimetype, container.xml, content.opf, nav.xhtml, and toc.ncx.

Usage:
  python tools/build_epub.py [--out site/on-hyperwar.epub]
"""
from __future__ import annotations

import argparse
import html
import os
import re
import uuid
import zipfile
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(REPO_ROOT, "chapters")

BOOK_TITLE = "On Hyperwar: Decision Speed as the Weapon"
BOOK_AUTHOR = "Sandra"
BOOK_IDENTIFIER = "urn:uuid:9c45a793-253f-5c72-ad28-2f5914849c66"
BOOK_LANGUAGE = "en"

ORDER = [
    "cold-open-variants.md",
    "01-the-question.md",
    "02-allen-lineage.md",
    "03-no-equation.md",
    "04-the-ladder.md",
    "05-locating-the-present.md",
    "06-thresholds.md",
    "07-control-case.md",
    "08-terminal-states.md",
    "09-day-two.md",
    "10-corpus.md",
    "side-what-scifi-gets-wrong.md",
]

EPUB_CSS = """@charset "utf-8";
body {
    font-family: Georgia, Cambria, "Times New Roman", Times, serif;
    line-height: 1.6;
    margin: 5%;
    text-align: justify;
    color: #1a1a1a;
}
h1, h2, h3, h4 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.25;
    text-align: left;
    color: #111827;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}
h1 { font-size: 1.8em; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.3em; }
h2 { font-size: 1.4em; }
h3 { font-size: 1.15em; }
p { margin: 0 0 1em 0; text-indent: 0; }
blockquote {
    margin: 1em 0 1em 1.5em;
    padding-left: 1em;
    border-left: 3px solid #ef4444;
    color: #4b5563;
    font-style: italic;
}
code {
    font-family: "Courier New", Courier, monospace;
    font-size: 0.9em;
    background-color: #f3f4f6;
    padding: 0.1em 0.3em;
}
pre {
    background-color: #f3f4f6;
    padding: 0.8em;
    overflow-x: auto;
    font-size: 0.85em;
    border-radius: 4px;
}
pre code { background: none; padding: 0; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.2em 0;
    font-size: 0.9em;
}
th, td {
    border: 1px solid #d1d5db;
    padding: 0.4em 0.6em;
    text-align: left;
}
th { background-color: #f9fafb; font-weight: bold; }
hr { border: none; border-top: 1px solid #e5e7eb; margin: 2em 0; }
"""


def slug(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def inline_xhtml(md: str) -> str:
    out = html.escape(md, quote=True)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def md_to_xhtml(md: str) -> tuple[str, str]:
    """Converts markdown to strictly valid XHTML for EPUB."""
    lines = md.split("\n")
    parts: list[str] = []
    title = "Untitled"
    i = 0
    in_fence = False
    fence_buf: list[str] = []
    n = len(lines)
    while i < n:
        line = lines[i]
        if line.strip().startswith("```"):
            if not in_fence:
                in_fence = True
                fence_buf = []
            else:
                in_fence = False
                parts.append("<pre><code>" + html.escape("\n".join(fence_buf)) + "</code></pre>")
            i += 1
            continue
        if in_fence:
            fence_buf.append(line)
            i += 1
            continue
        s = line.strip()
        if not s:
            i += 1
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", s)
        if m:
            level = len(m.group(1))
            text = inline_xhtml(m.group(2))
            if level == 1 and title == "Untitled":
                title = re.sub(r"<[^>]+>", "", text)
            parts.append(f'<h{level} id="{slug(text)}">{text}</h{level}>')
            i += 1
            continue
        if re.match(r"^---+$", s):
            parts.append("<hr />")
            i += 1
            continue
        if s.startswith(">"):
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            parts.append("<blockquote><p>" + " ".join(inline_xhtml(q) for q in quote) + "</p></blockquote>")
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ["<table><thead><tr>" + "".join(f"<th>{inline_xhtml(c)}</th>" for c in header) + "</tr></thead><tbody>"]
            t += ["<tr>" + "".join(f"<td>{inline_xhtml(c)}</td>" for c in r) + "</tr>" for r in rows]
            parts.append("".join(t) + "</tbody></table>")
            continue
        if re.match(r"^[-*]\s+", s):
            items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append("<li>" + inline_xhtml(re.sub(r"^[-*]\s+", "", lines[i].strip())) + "</li>")
                i += 1
            parts.append("<ul>" + "".join(items) + "</ul>")
            continue
        if re.match(r"^\d+\.\s+", s):
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append("<li>" + inline_xhtml(re.sub(r"^\d+\.\s+", "", lines[i].strip())) + "</li>")
                i += 1
            parts.append("<ol>" + "".join(items) + "</ol>")
            continue
        buf = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,3}\s|```|\||[-*]\s|\d+\.\s|>|---+$)", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        parts.append("<p>" + inline_xhtml(" ".join(buf)) + "</p>")
    return title, "\n".join(parts)


def build_epub(output_path: str, title: str = BOOK_TITLE, author: str = BOOK_AUTHOR) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    available = [f for f in ORDER if os.path.isfile(os.path.join(CHAPTERS_DIR, f))]
    extra = sorted(f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md") and f not in ORDER)
    files = available + extra

    chapters: list[dict[str, str]] = []
    for idx, fn in enumerate(files, 1):
        md = open(os.path.join(CHAPTERS_DIR, fn), encoding="utf-8").read()
        ch_title, body_xhtml = md_to_xhtml(md)
        filename = f"chapter_{idx:02d}.xhtml"
        chapters.append({
            "id": f"ch_{idx:02d}",
            "filename": filename,
            "title": ch_title,
            "body": body_xhtml,
        })

    pub_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Generate container.xml
    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""

    # Generate nav.xhtml (EPUB 3 TOC)
    nav_items = "\n".join(
        f'        <li><a href="{ch["filename"]}">{html.escape(ch["title"])}</a></li>'
        for ch in chapters
    )
    nav_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{BOOK_LANGUAGE}">
<head>
  <title>Table of Contents</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Table of Contents</h1>
    <ol>
{nav_items}
    </ol>
  </nav>
</body>
</html>"""

    # Generate toc.ncx (EPUB 2 backward compatibility)
    ncx_navpoints = "\n".join(
        f"""    <navPoint id="navpoint-{idx}" playOrder="{idx}">
      <navLabel><text>{html.escape(ch["title"])}</text></navLabel>
      <content src="{ch["filename"]}"/>
    </navPoint>"""
        for idx, ch in enumerate(chapters, 1)
    )
    toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{BOOK_IDENTIFIER}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{html.escape(title)}</text></docTitle>
  <navMap>
{ncx_navpoints}
  </navMap>
</ncx>"""

    # Generate content.opf
    manifest_items = [
        '    <item id="style" href="style.css" media-type="text/css"/>',
        '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
    ]
    for ch in chapters:
        manifest_items.append(
            f'    <item id="{ch["id"]}" href="{ch["filename"]}" media-type="application/xhtml+xml"/>'
        )

    spine_items = [f'    <itemref idref="{ch["id"]}"/>' for ch in chapters]

    content_opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id" xml:lang="{BOOK_LANGUAGE}">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">{BOOK_IDENTIFIER}</dc:identifier>
    <dc:title>{html.escape(title)}</dc:title>
    <dc:creator>{html.escape(author)}</dc:creator>
    <dc:language>{BOOK_LANGUAGE}</dc:language>
    <dc:date>{pub_date}</dc:date>
    <meta property="dcterms:modified">{pub_date}</meta>
  </metadata>
  <manifest>
{chr(10).join(manifest_items)}
  </manifest>
  <spine toc="ncx">
{chr(10).join(spine_items)}
  </spine>
</package>"""

    # Assemble ZIP file
    with zipfile.ZipFile(output_path, "w") as zf:
        # 1. mimetype must be stored uncompressed, as the very first file
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)

        # 2. META-INF/container.xml
        zf.writestr("META-INF/container.xml", container_xml, compress_type=zipfile.ZIP_DEFLATED)

        # 3. OEBPS contents
        zf.writestr("OEBPS/content.opf", content_opf, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/toc.ncx", toc_ncx, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/style.css", EPUB_CSS, compress_type=zipfile.ZIP_DEFLATED)

        # 4. Each chapter XHTML
        for ch in chapters:
            doc = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{BOOK_LANGUAGE}">
<head>
  <title>{html.escape(ch["title"])}</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  {ch["body"]}
</body>
</html>"""
            zf.writestr(f'OEBPS/{ch["filename"]}', doc, compress_type=zipfile.ZIP_DEFLATED)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"Generated EPUB 3: {output_path} ({size_kb:.1f} KB, {len(chapters)} chapters)")


def main() -> int:
    ap = argparse.ArgumentParser(description="Build EPUB 3 from chapters")
    ap.add_argument("--out", default=os.path.join(REPO_ROOT, "site", "on-hyperwar.epub"))
    args = ap.parse_args()
    build_epub(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
