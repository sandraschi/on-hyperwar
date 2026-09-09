set windows-shell := ["powershell.exe", "-NoProfile", "-Command"]

default:
  @just --list

# Lore-check: control-rung coverage, dates, forbidden terms.
lore:
  @py -3 tools/lorecheck.py

lore-strict:
  @py -3 tools/lorecheck.py --strict
