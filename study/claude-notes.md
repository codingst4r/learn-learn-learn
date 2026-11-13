# Notes for Claude

> Claude's own working notes so a new session on either computer starts with context. Mike doesn't need to read this. `/leftoff` rewrites it each time. Keep it under ~20 lines, and drop anything stale.

## Open threads
- Lesson 8: example typed in `lessons/lesson8.py`, not yet run. He plans to experiment with try/except. Lesson 8 try-it not started.
- Then homework 9-3 (temperature converter). Remind him to follow the spec exactly on homework (he likes adding his own twists).
- Didn't confirm autopep8 actually kept spaces / fixed line 26 indent in lesson7_try.py. Ask if it worked.
- Lesson 4 launcher: typing `cat` crashes with ValueError. Good try/except practice target.

## Hint ladder state
- No try-it in progress.

## What works with Mike (beyond CLAUDE.md)
- He experiments and pushes back with reasons. Check what he actually means before correcting (argued past his real point on `self` once).
- Tiny non-GUI demos (two objects, print self) make points concrete fast.
- He cares about readability: prefers book style `title = "x"` over PEP 8. Respect it.
- "choose" = just pick with a reason. "no distractions" = drop side challenges. "boom" = wants a check.

## Setup
- Git remote `mainremote`. Laptop uses `http.sslBackend schannel` (fixed SSL error 2026-11-11).
- `.vscode/settings.json`: autopep8 is the Python formatter with `--ignore=E251`, format on save off. Black ext still installed but unused. Desktop needs the autopep8 extension installed.
