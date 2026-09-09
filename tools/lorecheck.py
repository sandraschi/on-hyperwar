"""Lore-check for on-ai-takeover - consistency without invention.

Checks (read-only, stdlib only):
  rungs   : which of 1-44 are mentioned where; flags gaps and [construction] tags
  xids    : 15-20 digit X status IDs mentioned; reports file:line, no network verify
  dates   : ISO-like dates present per chapter (revision-date hygiene for Ch V)
  language: forbidden attention-hazard terms (skynet, terminator) - Rule 2/style

Usage:
  python tools/lorecheck.py
  python tools/lorecheck.py --strict   # exit 1 on gaps/forbidden terms
"""
from __future__ import annotations

import argparse
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(REPO_ROOT, "chapters")
FORBIDDEN = ["skynet", "terminator"]
RUNG_RE = re.compile(r"\brungs?\s+(\d{1,2})(?:\s*(?:[-,+/&]|to|and)\s*(\d{1,2}))?", re.I)
BRACKET_RE = re.compile(r"\[construction\]", re.I)
XID_RE = re.compile(r"\b\d{15,20}\b")
DATE_RE = re.compile(r"\b202\d-\d{2}-\d{2}(?:T\d{2}:\d{2}(?::\d{2})?Z?)?\b")


def md_files() -> list[str]:
    out = []
    for root, _, files in os.walk(REPO_ROOT):
        if ".git" in root:
            continue
        for fn in sorted(files):
            if fn.endswith(".md"):
                out.append(os.path.join(root, fn))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Lore-check on-ai-takeover")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    files = md_files()
    rung_hits: dict[int, list[str]] = {}
    construction = 0
    xids: list[str] = []
    dates: dict[str, int] = {}
    forbidden: list[str] = []
    errors = 0

    for fp in files:
        rel = os.path.relpath(fp, REPO_ROOT)
        try:
            txt = open(fp, encoding="utf-8").read()
        except Exception as e:
            print(f"READ-ERR {rel}: {e}")
            errors += 1
            continue
        for m in RUNG_RE.finditer(txt):
            for g in m.groups():
                if g and g.isdigit():
                    n = int(g)
                    if 1 <= n <= 44:
                        rung_hits.setdefault(n, []).append(rel)
        construction += len(BRACKET_RE.findall(txt))
        for m in XID_RE.finditer(txt):
            line = txt[: m.start()].count("\n") + 1
            xids.append(f"{m.group(0)} {rel}:{line}")
        for m in DATE_RE.finditer(txt):
            dates.setdefault(m.group(0)[:10], 0)
            dates[m.group(0)[:10]] += 1
        low = txt.lower()
        for term in FORBIDDEN:
            # mention-vs-use: skip lines that negate or quote the term as a rule
            # ("no <term>", "without <term>", "ban <term>") to avoid flagging
            # the style rule itself.
            hit = False
            for line in txt.splitlines():
                l = line.lower()
                if term in l and not re.search(
                    r"\b(no|without|ban|avoid|never|forbidden)\b[^.\n]{0,40}" + re.escape(term), l
                ):
                    hit = True
                    break
            if hit:
                forbidden.append(f"{term} in {rel}")
                break

    mentioned = sorted(rung_hits)
    missing = [n for n in range(1, 45) if n not in rung_hits]

    print(f"files scanned: {len(files)}")
    print(f"rungs mentioned: {len(mentioned)}/44")
    if mentioned:
        print(f"  covered: {mentioned}")
    print(f"  missing: {missing if missing else 'none'}")
    print(f"[construction] flags: {construction}")
    print(f"X IDs found: {len(xids)}")
    for x in xids[:30]:
        print(f"  {x}")
    if len(xids) > 30:
        print(f"  ... +{len(xids) - 30} more")
    print(f"distinct dates: {len(dates)}")
    for d in sorted(dates)[-10:]:
        print(f"  {d} x{dates[d]}")
    print(f"forbidden terms: {forbidden if forbidden else 'none'}")

    problems = []
    if missing:
        problems.append(f"{len(missing)} rungs unmentioned")
    if forbidden:
        problems.append(f"{len(forbidden)} files with forbidden terms")
    if problems and args.strict:
        print("STRICT-FAIL: " + "; ".join(problems), file=sys.stderr)
        return 1
    if problems:
        print("note: " + "; ".join(problems) + " (non-strict, exit 0)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
