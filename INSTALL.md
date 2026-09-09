# INSTALL - on-hyperwar (book + local reader)

Status: construction v0.1. No build tools beyond Python + just.

## Option A: double-click (Windows)

Double-click `start.bat`. It checks for Python and `just`, builds `site/`,
and serves the book at **http://localhost:10988/** (registered fleet port).

## Option B: manual

Requirements: Python 3 (`py -3` on Windows), `just`
(`winget install Casey.Just`).

```powershell
just serve            # build site/ + serve on :10988
just serve <port>     # custom port (verify free in WEBAPP_PORTS.md first)
just lore             # consistency check (control rungs, dates)
just declaim-print chapters/cold-open-variants.md   # speech dry run
```

Audio versions (needs `GOOGLE_API_KEY`, Gemini TTS):

```powershell
just audio chapters/05-locating-the-present.md   # -> site/audio/*.wav, embedded in page
```

## Troubleshooting

| Issue | Fix |
|---|---|
| `just: command not found` | `winget install Casey.Just`, reopen terminal |
| `py not found` | Install Python 3, enable `py` launcher |
| Port busy | `just serve <port>` (verify free first) |
| `just lore` strict fails | Expected until v1.0: rungs unnumbered, `[construction]` everywhere |
