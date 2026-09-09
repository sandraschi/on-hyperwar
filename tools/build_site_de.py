"""Build German static HTML book site and EPUB from chapters_de/*.md - pure Python stdlib.

Usage:
  python tools/build_site_de.py [--out site/de]

Output:
  <out>/index.html + chapter pages in German (dark reader theme, prev/next nav, rung anchors)
  <out>/on-hyperwar-de.epub (complete offline German EPUB 3 ebook)
"""
from __future__ import annotations

import argparse
import html
import os
import re
import sys
import uuid
import zipfile
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DE_DIR = os.path.join(REPO_ROOT, "chapters_de")
SITE_DE_DIR = os.path.join(REPO_ROOT, "site", "de")

BOOK_TITLE = "Über den Hyperkrieg: Entscheidungsgeschwindigkeit als Waffe"
BOOK_AUTHOR = "Sandra"
BOOK_IDENTIFIER = "urn:uuid:9c45a793-253f-5c72-ad28-2f5914849c66-de"
BOOK_LANGUAGE = "de"

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

CSS = """
:root {
  --bg: #09090b;
  --surface: #18181b;
  --surface-hover: #27272a;
  --border: #27272a;
  --text: #e4e4e7;
  --text-muted: #a1a1aa;
  --heading: #fafafa;
  --accent: #f87171;
  --accent-visited: #fca5a5;
  --code-bg: #1f1f23;
  --callout-border: #ef4444;
}

* { box-sizing: border-box; }
body {
  background: var(--bg);
  color: var(--text);
  font: 16px/1.7 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
}
main {
  max-width: 48rem;
  margin: 0 auto;
  padding: 2.5rem 1.25rem 5rem;
}
nav.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.85rem 1.5rem;
  border-bottom: 1px solid var(--border);
  background: rgba(9, 9, 11, 0.85);
  backdrop-filter: blur(8px);
  position: sticky;
  top: 0;
  z-index: 100;
  font-size: 0.9rem;
}
nav.top a {
  color: var(--text);
  text-decoration: none;
  font-weight: 500;
}
nav.top a:hover { color: var(--accent); }
nav.top .links {
  display: flex;
  gap: 1.25rem;
  align-items: center;
}
nav.top .lang-switch {
  border: 1px solid var(--border);
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  color: var(--text-muted);
}
nav.top .epub-tag {
  background: #7f1d1d;
  color: #fecaca;
  padding: 0.2rem 0.6rem;
  border-radius: 9999px;
  font-size: 0.8rem;
}
h1, h2, h3, h4 {
  color: var(--heading);
  line-height: 1.3;
  margin-top: 2rem;
  margin-bottom: 0.75rem;
}
h1 { font-size: 2rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }
h2 { font-size: 1.4rem; border-bottom: 1px solid var(--border); padding-bottom: 0.3rem; }
h3 { font-size: 1.15rem; }
p, ul, ol { margin: 1rem 0; color: var(--text); }
li { margin: 0.35rem 0; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
hr { border: 0; border-top: 1px solid var(--border); margin: 2rem 0; }
pre, code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.9em;
}
pre {
  background: var(--code-bg);
  padding: 1rem;
  border-radius: 0.4rem;
  overflow-x: auto;
  border: 1px solid var(--border);
}
code {
  background: var(--code-bg);
  padding: 0.15em 0.35em;
  border-radius: 0.25rem;
  border: 1px solid rgba(255, 255, 255, 0.05);
}
pre code { border: none; padding: 0; background: transparent; }
blockquote {
  border-left: 3px solid var(--callout-border);
  margin: 1.2rem 0;
  padding: 0.6rem 1.2rem;
  background: var(--surface);
  border-radius: 0 0.4rem 0.4rem 0;
  color: var(--text-muted);
}
blockquote p { margin: 0.4rem 0; }
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 0.92rem;
}
th, td {
  border: 1px solid var(--border);
  padding: 0.6rem 0.8rem;
  text-align: left;
}
th {
  background: var(--surface);
  color: var(--heading);
  font-weight: 600;
}
img {
  max-width: 100%;
  height: auto;
  border-radius: 0.4rem;
  border: 1px solid var(--border);
  margin: 1.5rem 0 0.5rem;
}
.caption {
  font-size: 0.88rem;
  color: var(--text-muted);
  font-style: italic;
  margin-bottom: 1.5rem;
}
footer.pn {
  display: flex;
  justify-content: space-between;
  margin-top: 3.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
}
.btn-box {
  display: inline-block;
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 0.6rem 1rem;
  border-radius: 0.4rem;
  font-weight: 500;
  margin: 1rem 0;
}
.toc-list { list-style: none; padding: 0; }
.toc-list li {
  margin: 0.6rem 0;
  padding: 0.6rem 0.8rem;
  border-radius: 0.4rem;
  border: 1px solid transparent;
  transition: all 0.15s ease;
}
.toc-list li:hover {
  background: var(--surface);
  border-color: var(--border);
}
.toc-list a {
  text-decoration: none;
  font-weight: 500;
  color: var(--heading);
  display: block;
}
.toc-list a:hover { color: var(--accent); }
"""

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
img { max-width: 100%; height: auto; margin: 1em 0; }
"""


def slug(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def inline(md: str) -> str:
    # First handle images ![alt](src)
    def repl_img(m):
        alt = html.escape(m.group(1))
        src = m.group(2)
        # If image src is relative, in site/de it's ../src
        if not src.startswith("http") and not src.startswith("../"):
            src = "../" + src
        return f'<img src="{src}" alt="{alt}" />'

    out = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl_img, md)
    out = re.sub(r"`([^`]+)`", lambda m: f"<code>{html.escape(m.group(1))}</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def md_to_html(md: str) -> tuple[str, str]:
    lines = md.split("\n")
    parts: list[str] = []
    title = "Ohne Titel"
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
            text = inline(m.group(2))
            if level == 1 and title == "Ohne Titel":
                title = re.sub(r"<[^>]+>", "", text)
            parts.append(f'<h{level} id="{slug(text)}">{text}</h{level}>')
            i += 1
            continue
        if re.match(r"^---+$", s):
            parts.append("<hr>")
            i += 1
            continue
        if s.startswith(">"):
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            parts.append("<blockquote><p>" + " ".join(inline(q) for q in quote) + "</p></blockquote>")
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ["<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in header) + "</tr></thead><tbody>"]
            t += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows]
            parts.append("".join(t) + "</tbody></table>")
            continue
        if re.match(r"^[-*]\s+", s):
            items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append("<li>" + inline(re.sub(r"^[-*]\s+", "", lines[i].strip())) + "</li>")
                i += 1
            parts.append("<ul>" + "".join(items) + "</ul>")
            continue
        if re.match(r"^\d+\.\s+", s):
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append("<li>" + inline(re.sub(r"^\d+\.\s+", "", lines[i].strip())) + "</li>")
                i += 1
            parts.append("<ol>" + "".join(items) + "</ol>")
            continue
        buf = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,3}\s|```|\||[-*]\s|\d+\.\s|>|---+$)", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        parts.append("<p>" + inline(" ".join(buf)) + "</p>")
    return title, "\n".join(parts)


def inline_xhtml(md: str) -> str:
    out = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1" />', md)
    out = re.sub(r"`([^`]+)`", lambda m: f"<code>{html.escape(m.group(1))}</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def md_to_xhtml(md: str) -> tuple[str, str]:
    lines = md.split("\n")
    parts: list[str] = []
    title = "Ohne Titel"
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
            if level == 1 and title == "Ohne Titel":
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


def page(title: str, body: str, prev: tuple[str, str] | None, nxt: tuple[str, str] | None) -> str:
    nav = ""
    if prev or nxt:
        l = f'<a href="{prev[0]}">&larr; {html.escape(prev[1])}</a>' if prev else "<span></span>"
        r = f'<a href="{nxt[0]}">{html.escape(nxt[1])} &rarr;</a>' if nxt else "<span></span>"
        nav = f'<footer class="pn">{l}{r}</footer>'
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{html.escape(title)} - Über den Hyperkrieg</title>
  <style>{CSS}</style>
</head>
<body>
  <nav class="top">
    <a href="index.html"><strong>Über den Hyperkrieg</strong></a>
    <div class="links">
      <a href="../index.html" class="lang-switch">English</a>
      <a href="index.html">Inhalt</a>
      <a class="epub-tag" href="on-hyperwar-de.epub" download>EPUB (DE)</a>
    </div>
  </nav>
  <main>
    <h1>{html.escape(title)}</h1>
    {body}
    {nav}
  </main>
</body>
</html>
"""


def build_epub_de(output_path: str, files: list[str]) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    chapters: list[dict[str, str]] = []
    for idx, fn in enumerate(files, 1):
        md = open(os.path.join(CHAPTERS_DE_DIR, fn), encoding="utf-8").read()
        ch_title, body_xhtml = md_to_xhtml(md)
        filename = f"chapter_{idx:02d}.xhtml"
        chapters.append({
            "id": f"ch_{idx:02d}",
            "filename": filename,
            "title": ch_title,
            "body": body_xhtml,
        })

    pub_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""

    nav_items = "\n".join(
        f'        <li><a href="{ch["filename"]}">{html.escape(ch["title"])}</a></li>'
        for ch in chapters
    )
    nav_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{BOOK_LANGUAGE}">
<head>
  <title>Inhaltsverzeichnis</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Inhaltsverzeichnis</h1>
    <ol>
{nav_items}
    </ol>
  </nav>
</body>
</html>"""

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
  <docTitle><text>{html.escape(BOOK_TITLE)}</text></docTitle>
  <navMap>
{ncx_navpoints}
  </navMap>
</ncx>"""

    manifest_items = [
        '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '    <item id="css" href="style.css" media-type="text/css"/>',
    ]
    spine_items = []
    for ch in chapters:
        manifest_items.append(f'    <item id="{ch["id"]}" href="{ch["filename"]}" media-type="application/xhtml+xml"/>')
        spine_items.append(f'    <itemref idref="{ch["id"]}"/>')

    content_opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id" xml:lang="{BOOK_LANGUAGE}">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">{BOOK_IDENTIFIER}</dc:identifier>
    <dc:title>{html.escape(BOOK_TITLE)}</dc:title>
    <dc:language>{BOOK_LANGUAGE}</dc:language>
    <dc:creator>{html.escape(BOOK_AUTHOR)}</dc:creator>
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

    with zipfile.ZipFile(output_path, "w") as zf:
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        zf.writestr("META-INF/container.xml", container_xml, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/content.opf", content_opf, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/toc.ncx", toc_ncx, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/style.css", EPUB_CSS, compress_type=zipfile.ZIP_DEFLATED)
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
    print(f"Generated German EPUB 3: {output_path} ({size_kb:.1f} KB, {len(chapters)} chapters)")


def main() -> int:
    ap = argparse.ArgumentParser(description="Build German book site and EPUB")
    ap.add_argument("--out", default=SITE_DE_DIR)
    args = ap.parse_args()
    out = args.out
    os.makedirs(out, exist_ok=True)

    available = [f for f in ORDER if os.path.isfile(os.path.join(CHAPTERS_DE_DIR, f))]
    extra = sorted(f for f in os.listdir(CHAPTERS_DE_DIR) if f.endswith(".md") and f not in ORDER)
    files = available + extra

    # 1. Build German EPUB
    epub_path = os.path.join(out, "on-hyperwar-de.epub")
    build_epub_de(epub_path, files)

    # 2. Build German Chapters
    pages: list[tuple[str, str]] = []
    for fn in files:
        md = open(os.path.join(CHAPTERS_DE_DIR, fn), encoding="utf-8").read()
        title, body = md_to_html(md)
        stem = fn[:-3]
        pages.append((stem + ".html", title))

    for idx, (fn_html, title) in enumerate(pages):
        prev = pages[idx - 1] if idx > 0 else None
        nxt = pages[idx + 1] if idx + 1 < len(pages) else None
        md = open(os.path.join(CHAPTERS_DE_DIR, files[idx]), encoding="utf-8").read()
        t2, body = md_to_html(md)
        open(os.path.join(out, fn_html), "w", encoding="utf-8", newline="\n").write(
            page(t2, body, prev, nxt)
        )

    # 3. Build Index
    chapter_items = "\n".join(
        f'<li><a href="{fn}">{html.escape(t)}</a></li>' for fn, t in pages
    )
    index_body = f"""
    <p><em>Entscheidungsgeschwindigkeit als Waffe</em></p>
    <p>Hyperkrieg ist keine Waffenklasse; es ist eine Taktfrequenz. Vierundvierzig Sprossen, die das Entgleiten menschlicher Freigabeautorität von In-the-Loop über On-the-Loop bis hin zur bloßen nachträglichen Unterrichtung abbilden.</p>
    
    <p>
      <a class="btn-box" href="on-hyperwar-de.epub" download>
        &#128214; Deutsche EPUB-Ausgabe herunterladen
      </a>
    </p>

    <h2>Kapitel</h2>
    <ol class="toc-list">
      {chapter_items}
    </ol>
    """

    open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="\n").write(
        page("Über den Hyperkrieg", index_body, None, None)
    )
    print(f"Built German site ({len(pages) + 1} pages) + EPUB -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
