"""Build static HTML book site and EPUB from chapters/*.md - pure Python stdlib.

Usage:
  python tools/build_site.py [--out site]

Output:
  <out>/index.html + chapter pages (dark reader theme, prev/next nav, rung anchors)
  <out>/on-hyperwar.epub (complete offline EPUB 3 ebook)
"""
from __future__ import annotations

import argparse
import html
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(REPO_ROOT, "chapters")
DOCS_DIR = os.path.join(REPO_ROOT, "docs")

sys.path.insert(0, os.path.join(REPO_ROOT, "tools"))
try:
    from build_epub import build_epub
except ImportError:
    build_epub = None

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
nav.top .epub-tag {
  background: #7f1d1d;
  color: #fecaca;
  padding: 0.2rem 0.6rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  text-decoration: none;
  font-weight: 600;
}
nav.top .epub-tag:hover {
  background: #991b1b;
  color: #ffffff;
}
a { color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }
a:visited { color: var(--accent-visited); }
a:hover { color: #fca5a5; }

h1, h2, h3, h4 {
  line-height: 1.28;
  color: var(--heading);
  margin-top: 2em;
  margin-bottom: 0.6em;
  font-weight: 600;
}
h1 { font-size: 2rem; margin-top: 1em; border-bottom: 1px solid var(--border); padding-bottom: 0.4em; }
h2 { font-size: 1.45rem; }
h3 { font-size: 1.2rem; }

code {
  background: var(--code-bg);
  padding: 0.15em 0.4em;
  border-radius: 0.35em;
  font-family: ui-monospace, "Cascadia Code", Consolas, Menlo, monospace;
  font-size: 0.88em;
  color: #f87171;
}
pre {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 1rem 1.2rem;
  border-radius: 0.5rem;
  overflow-x: auto;
}
pre code {
  background: none;
  padding: 0;
  color: var(--text);
  font-size: 0.9em;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.5rem 0;
  font-size: 0.95rem;
}
th, td {
  border: 1px solid var(--border);
  padding: 0.55rem 0.8rem;
  text-align: left;
}
th {
  background: var(--surface);
  color: var(--heading);
  font-weight: 600;
}
blockquote {
  border-left: 3px solid var(--callout-border);
  background: rgba(239, 68, 68, 0.05);
  margin: 1.5rem 0;
  padding: 0.5rem 1.25rem;
  color: var(--text-muted);
  border-radius: 0 0.4rem 0.4rem 0;
}
hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 2.5rem 0;
}
footer.pn {
  display: flex;
  justify-content: space-between;
  margin-top: 4rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
  font-size: 0.95rem;
}
.btn-box {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: #7f1d1d;
  color: #fee2e2 !important;
  text-decoration: none !important;
  padding: 0.6rem 1.2rem;
  border-radius: 0.4rem;
  font-weight: 600;
  margin: 1rem 0 2rem;
}
.btn-box:hover { background: #991b1b; }
.toc-list { list-style: none; padding-left: 0; }
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
audio { width: 100%; margin: 1.2rem 0; }
"""


def slug(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def inline(md: str) -> str:
    out = html.escape(md, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def md_to_html(md: str) -> tuple[str, str]:
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
            text = inline(m.group(2))
            if level == 1 and title == "Untitled":
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


def page(title: str, body: str, prev: tuple[str, str] | None, nxt: tuple[str, str] | None, audio: str | None) -> str:
    nav = ""
    if prev or nxt:
        l = f'<a href="{prev[0]}">&larr; {html.escape(prev[1])}</a>' if prev else "<span></span>"
        r = f'<a href="{nxt[0]}">{html.escape(nxt[1])} &rarr;</a>' if nxt else "<span></span>"
        nav = f'<footer class="pn">{l}{r}</footer>'
    player = f'<audio controls src="{audio}"><a href="{audio}">audio version</a></audio>' if audio else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{html.escape(title)} - On Hyperwar</title>
  <style>{CSS}</style>
</head>
<body>
    <nav class="top">
    <a href="index.html"><strong>On Hyperwar</strong></a>
    <div class="links">
      <a href="de/index.html" class="lang-switch">Deutsch (DE)</a>
      <a href="index.html">Contents</a>
      <a href="assessment.html">Assessment</a>
      <a href="references.html">References</a>
      <a href="reisner.html">Memo Reisner</a>
      <a class="epub-tag" href="on-hyperwar.epub" download>EPUB (EN)</a>
      <a class="epub-tag" href="de/on-hyperwar-de.epub" download style="background:#831843;color:#fbcfe8;">EPUB (DE)</a>
    </div>
  </nav>
  <main>
    <h1>{html.escape(title)}</h1>
    {player}
    {body}
    {nav}
  </main>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Build static book site and EPUB")
    ap.add_argument("--out", default=os.path.join(REPO_ROOT, "site"))
    args = ap.parse_args()
    out = args.out
    audio_dir = os.path.join(out, "audio")
    os.makedirs(out, exist_ok=True)

    # 1. Build EPUB first
    epub_path = os.path.join(out, "on-hyperwar.epub")
    if build_epub:
        build_epub(epub_path)

    # 2. Build Chapters
    available = [f for f in ORDER if os.path.isfile(os.path.join(CHAPTERS_DIR, f))]
    extra = sorted(f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md") and f not in ORDER)
    files = available + extra

    pages: list[tuple[str, str]] = []
    for fn in files:
        md = open(os.path.join(CHAPTERS_DIR, fn), encoding="utf-8").read()
        title, body = md_to_html(md)
        stem = fn[:-3]
        pages.append((stem + ".html", title))

    for idx, (fn_html, title) in enumerate(pages):
        prev = pages[idx - 1] if idx > 0 else None
        nxt = pages[idx + 1] if idx + 1 < len(pages) else None
        stem = files[idx][:-3]
        wav = os.path.join(audio_dir, stem + ".wav")
        wav = f"audio/{stem}.wav" if os.path.isfile(wav) else None
        md = open(os.path.join(CHAPTERS_DIR, files[idx]), encoding="utf-8").read()
        t2, body = md_to_html(md)
        open(os.path.join(out, fn_html), "w", encoding="utf-8", newline="\n").write(
            page(t2, body, prev, nxt, wav)
        )

    # 3. Build Docs (Assessment, References, Reisner Memo, Economics)
    doc_pages = [
        ("ASSESSMENT.md", "assessment.html"),
        ("REFERENCES.md", "references.html"),
        ("MEMORANDUM_REISNER.md", "reisner.html"),
        ("ECONOMICS_OF_HYPERWAR.md", "economics.html"),
    ]
    for src, dst in doc_pages:
        src_path = os.path.join(DOCS_DIR, src)
        if os.path.isfile(src_path):
            md = open(src_path, encoding="utf-8").read()
            t, body = md_to_html(md)
            open(os.path.join(out, dst), "w", encoding="utf-8", newline="\n").write(
                page(t, body, None, None, None)
            )

    # 4. Build Index
    chapter_items = "\n".join(
        f'<li><a href="{fn}">{html.escape(t)}</a></li>' for fn, t in pages
    )
    doc_items = """
      <li><a href="assessment.html">Strategic Assessment & Methodological Evaluation</a></li>
      <li><a href="references.html">Scholarly Apparatus & Academic Bibliography</a></li>
      <li><a href="reisner.html">Memorandum für Oberst dG Dr. Markus Reisner, PhD</a></li>
      <li><a href="economics.html">The Political Economy of Hyperwar (Attrition & Defense-Industrial Base)</a></li>
    """

    index_body = f"""
    <p><em>Decision Speed as the Weapon</em></p>
    <p>Hyperwar is not a weapon class; it is a clock speed. Forty-four rungs mapping the slide of human release authority from in-the-loop to on-the-loop to told-afterwards.</p>
    
    <p style="display:flex;gap:1rem;flex-wrap:wrap;">
      <a class="btn-box" href="on-hyperwar.epub" download>
        &#128214; Download EPUB (English)
      </a>
      <a class="btn-box" href="de/on-hyperwar-de.epub" download style="border-color:#f87171;">
        &#128214; EPUB herunterladen (Deutsch)
      </a>
      <a class="btn-box" href="de/index.html">
        &#127465;&#127466; Deutsche Webausgabe lesen
      </a>
    </p>

    <h2>Chapters</h2>
    <ol class="toc-list">
      {chapter_items}
    </ol>

    <h2>Scholarly, Strategic & Military Apparatus</h2>
    <ul class="toc-list">
      {doc_items}
    </ul>
    """

    open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="\n").write(
        page("On Hyperwar", index_body, None, None, None)
    )
    print(f"Built {len(pages) + len(doc_pages) + 1} web pages + EPUB -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
