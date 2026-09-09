# On Hyperwar — decision speed as the weapon

**Status:** construction v0.1 (2026-09-09). Private. Audience: principals who
can attach brakes to kill chains, not hobbyists.

## Thesis (one sentence)

Hyperwar is not a weapon, it is a clock speed: humans slide from
in-the-loop to on-the-loop to told-about-it-afterwards, one irreversible
step at a time - this book orders those steps by reversibility of human
control, each with a dated observable fact.

## Lineage

- **2016:** John Allen's first hyperwar paper - before modern AI/LLMs.
  Decision speed + algorithmic teaming as the coming revolution.
- **2019:** Hyperwar book v1.
- **2024:** Newest edition with added chapters.
- **2022-2026:** Ukraine supplies the missing empirical half Allen could
  only theorize: mud engineering at weekly tit-for-tat cadence against
  Putin's adaptations. Shenzhen dual-use stack (DJI airframe + camera +
  Orin-class compute + 1 kg payload + km-long fiber backlink), built by the
  thousands. DIY cruise missiles flown into Moscow at orders of magnitude
  below Northrop Grumman unit cost. Sniper bots on precision dual-use
  gimbals with scopes and VLA (vision-language-action) models.

## The gap this book fills

Allen described hyperwar before LLMs and before a peer land war
instrumented it. The doctrine literature is capability-centric (ranges,
throw weights, autonomy percentages) and cannot be dated or acted on.
This book is control-centric: where, exactly, does the human leave the
kill chain, and what would still stop the next step?

## Chapters (I-X, stubs in `chapters/`)

I Cold open (a fiber-spooled FPV week, 2026) - II Allen 2016-2024, what
survived contact - III No equation of state (why OODA arithmetic and
Lanchester++ don't locate us) - IV The ladder (control rungs over kill
chains, Bands I-VI) - V Locating the present (living, revision-dated:
fiber FPV, DIY cruise missiles, sniper VLA) - VI Thresholds A-E as
attachment points (export chokepoints, approval gates, hotlines that work
at machine speed) - VII The control case and why it fails (certifications
that certify paperwork) - VIII Terminal states - IX Day Two (what war
termination looks like at machine speed) - X The book in the corpus.

## Design constraints (normative, see CONTRIBUTING.md)

- Rule 1 Observability: every rung a dateable public fact (strike footage
  with dates, procurement records, unit announcements, manufacturer specs).
  Intentions need quoted public speech. Classified programs excluded until
  publicly evidenced.
- Rule 2 Hazard (HARD): institutional facts + governance criteria ONLY.
  No TTPs, no build guides, no procurement how-tos, no targeting detail,
  no code. A chapter that teaches is a chapter that gets cut.
- Style: plain declarative, dates first, Kahn-flat. Allen's 2016 paper is
  the voice ancestor, Kahn the method ancestor.
- Sister repo: `on-ai-takeover` (same ladder method, training loops).
  Shared tooling: `just lore`, declaim pipeline.

## Tooling (to be ported from on-ai-takeover at v0.2)

`tools/lorecheck.py` + `just lore` (rung coverage, dates, forbidden terms),
`tools/declaim.py` (read-aloud gate), `tools/build_site.py` + `just serve`
(static reader, registered port TBD).
