set windows-shell := ["powershell.exe", "-NoProfile", "-Command"]

default:
  @just --list

# Lore-check: control-rung coverage, dates, forbidden terms.
lore:
  @py -3 tools/lorecheck.py

lore-strict:
  @py -3 tools/lorecheck.py --strict

# Dry run: show speech chunks without audio.
declaim-print FILE:
  @py -3 tools/declaim.py {{FILE}} --print

# Audio version of a chapter (Gemini TTS, needs GOOGLE_API_KEY). Embedded by build_site.
audio FILE:
  @py -3 tools/declaim.py {{FILE}} --provider auto --voice Kore --out site/audio/{{file_stem(FILE)}}.wav --no-play

# Build + serve the book locally (http://localhost:10988/).
serve PORT="10988":
  @py -3 tools/build_site.py
  @py -3 -m http.server {{PORT}} --bind 127.0.0.1 --directory site
