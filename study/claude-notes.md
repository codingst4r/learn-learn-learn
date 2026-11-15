# Notes for Claude

> Claude's own working notes so a new session on either computer starts with context. Mike doesn't need to read this. `/leftoff` rewrites it each time. Keep it under ~20 lines, and drop anything stale.

## Open threads
- Lesson 9 try-it in progress (`lessons/lesson9_try.py`): third panel added (label text "Fields left blank: ", no 0 yet, not saved to self so submit can't update it). `submit` has an empty `if userName == "":` block, a syntax error right now. Never answered: "when you stretch the window, do buttons grow or just the panel?" (He saw it, I explained.)
- Next homework 9-4 needs Lesson 13 (Enter key). Homework 9-1..9-3 passed 2026-11-12.
- Side project for later: his own encoder/obfuscator (Caesar cipher etc.). Explained obfuscation vs encryption. Asked what he'd protect (code or files), no answer yet.
- Ask whether autopep8 Shift+Alt+F actually kept spaces (never confirmed).

## Hint ladder state
- Lesson 9 try-it: no hints given yet, he's building on his own.

## What works with Mike (beyond CLAUDE.md)
- Talk like a homie, not a teacher (his request 2026-11-13). Play along with jokes, then back to code.
- He experiments and pushes back with reasons. Check what he means before correcting.
- Break-it-on-purpose demos and tiny experiments (panel background colors) land great.
- Prefers book style `title = "x"`. "choose" = just pick. "boom" = wants a check.
- He forgets /leftoff sometimes. If /start on one machine misses work, the other machine probably didn't push.

## Setup
- Git remote `mainremote`. Sessions on 2026-11-11 to 11-14 were on the DESKTOP, which uses `http.sslBackend schannel`.
- `.vscode/settings.json`: autopep8 formatter, `--ignore=E251`, format on save off. Laptop still needs the autopep8 extension.
- Homework repo (Cengage, graded, read-only for me): github.com/cengage-csp-students-prod-4/9780357881019-fundamentals-of-python-3e-2f1c5246-2300-4dcb-b487-b6a87a876d81, branch `template`, `chapter9/ex01..ex09`. `results/task1.txt` = pass status. Clone works with his git login (no `gh`). Never write there.
- Claude memory files are per-machine. Tone preference is in desktop memory and here.
