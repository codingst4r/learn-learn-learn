# Notes for Claude

> Claude's own working notes so a new session on either computer starts with context. Mike doesn't need to read this. `/leftoff` rewrites it each time. Keep it under ~20 lines, and drop anything stale.

## Open threads
- Next: homework 9-4 (9-3 converter + Enter binds). Then Lessons 10-12. Remind him homework = exact spec text.
- Lesson 13 try-it done. I fixed 2 bugs in his refactor at his request ("just this once"): missing `= False` inits and `setNumber(None)`. Suggested renaming `errorHandler` to `getArea` (optional). Debug prints may still be in there. Box-height math undercounts `\n` lines on very long input; he chose to leave it.
- Never ran the "delete `lambda event:`" experiment in lesson13.py.
- Side project for later: his own encoder/obfuscator (Caesar cipher). Asked what he'd protect, no answer yet.
- Laptop still needs the autopep8 extension.

## Hint ladder state
- No try-it in progress.

## What works with Mike (beyond CLAUDE.md)
- Talk like a homie. Play along with jokes, then back to code. "oh shit" may mean "I don't know". Ask before assuming.
- Tiny `py -c` demos make abstract stuff click. Mapping new cases onto ones that worked helps.
- He goes down rabbit holes (Pylance stubs, `__traceback__`, `__cause__`). Answer briefly, steer back.
- He thinks in code before words. When he says "can't put it in words," tell him to just write it.
- He has good design instincts (spotted "both fields bad" case, felt the code was too complicated). Praise specifically.
- "boom"/"/check" = check. "choose" = just pick. "ts" = this.

## Setup
- Git remote `mainremote`. Desktop uses `http.sslBackend schannel`. 2026-11-15 on laptop, 11-16 on desktop.
- `.vscode/settings.json`: autopep8, `--ignore=E251`, format on save off.
- Homework repo (Cengage, graded, read-only for me): github.com/cengage-csp-students-prod-4/9780357881019-fundamentals-of-python-3e-2f1c5246-2300-4dcb-b487-b6a87a876d81, branch `template`. Never write there.
