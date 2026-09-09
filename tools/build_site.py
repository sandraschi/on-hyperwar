"""Build static HTML book site from chapters/*.md - stdlib only, no deps.

Usage:
  python tools/build_site.py [--out site]

Output: <out>/index.html + one page per chapter (dark theme, prev/next nav,
rung anchors preserved). If <out>/audio/<stem>.wav exists, an <audio> player
is embedded (generate with: just audio chapters/<stem>.md).
"""
from __future__ import annotations

import argparse
import html
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(REPO_ROOT, "chapters")

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
]

CSS = """body{background:#09090b;color:#e4e4e7;font:16px/1.7 system-ui,sans-serif;margin:0}
main{max-width:46rem;margin:0 auto;padding:2rem 1.25rem 4rem}
nav.top{display:flex;justify-content:space-between;padding:.75rem 1.25rem;border-bottom:1px solid #27272a;font-size:.9rem}
a{color:#a5b4fc}a:visited{color:#c4b5fd}
h1,h2,h3{line-height:1.25;color:#fafafa}
code{background:#18181b;padding:.1em .35em;border-radius:.3em;font-size:.9em}
pre{background:#18181b;padding:1rem;border-radius:.5rem;overflow:auto}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:1rem 0}
th,td{border:1px solid #3f3f46;padding:.4rem .6rem;text-align:left}
blockquote{border-left:3px solid #6366f1;margin:1rem 0;padding:.25rem 1rem;color:#a1a1aa}
footer.pn{display:flex;justify-content:space-between;margin-top:3rem;padding-top:1rem;border-top:1px solid #27272a}
.construction{color:#fbbf24}
audio{width:100%;margin:1rem 0}"""


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
    """Returns (title, body_html). Handles headings, fences, tables, lists,
    quotes, hr, paragraphs. Anything else degrades to paragraphs."""
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
            parts.append(f"<h{level} id=\"{slug(text)}\">{text}</h{level}>")
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
            parts.append("<blockquote>" + " ".join(inline(q) for q in quote) + "</blockquote>")
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
        nav = f"<footer class=\"pn\">{l}{r}</footer>"
    player = f'<audio controls src="{audio}"><a href="{audio}">audio version</a></audio>' if audio else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} - On Hyperwar</title><style>{CSS}</style></head>
<body><nav class="top"><a href="index.html">On Hyperwar</a><span>construction v0.1</span></nav>
<main><h1>{html.escape(title)}</h1>{player}{body}{nav}</main></body></html>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Build static book site")
    ap.add_argument("--out", default=os.path.join(REPO_ROOT, "site"))
    args = ap.parse_args()
    out = args.out
    audio_dir = os.path.join(out, "audio")
    os.makedirs(out, exist_ok=True)

    available = [f for f in ORDER if os.path.isfile(os.path.join(CHAPTERS_DIR, f))]
    extra = sorted(f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md") and f not in ORDER)
    files = available + extra

    pages: list[tuple[str, str]] = []  # (filename.html, title)
    for fn in files:
        md = open(os.path.join(CHAPTERS_DIR, fn), encoding="utf-8").read()
        title, body = md_to_html(md)
        stem = fn[:-3]
        wav = f"audio/{stem}.wav" if os.path.isfile(os.path.join(audio_dir, stem + ".wav")) else None
        pages.append((stem + ".html", title))
        idx = len(pages) - 1
        prev = pages[idx - 1] if idx > 0 else None
        # next resolved after full list known; write with next=None for now
        open(os.path.join(out, stem + ".html"), "w", encoding="utf-8", newline="\n").write(
            page(title, body, prev, None, wav)
        )

    # second pass: fix next-links
    for idx, (fn_html, title) in enumerate(pages):
        prev = pages[idx - 1] if idx > 0 else None
        nxt = pages[idx + 1] if idx + 1 < len(pages) else None
        md = open(os.path.join(CHAPTERS_DIR, files[idx]), encoding="utf-8").read()
        t2, body = md_to_html(md)
        stem = files[idx][:-3]
        wav = f"audio/{stem}.wav" if os.path.isfile(os.path.join(audio_dir, stem + ".wav")) else None
        open(os.path.join(out, fn_html), "w", encoding="utf-8", newline="\n").write(
            page(t2, body, prev, nxt, wav)
        )

    items = "\n".join(f'<li><a href="{fn}">{html.escape(t)}</a></li>' for fn, t in pages)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="\n").write(
        page("Contents", f"<p>Control rungs over kill chains. Bands II-III, approaching the batch-approval threshold.</p><ol>{items}</ol>", None, None, None)
    )
    print(f"built {len(pages)} pages -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
