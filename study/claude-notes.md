# Notes for Claude

> Claude's own working notes so a new session on either computer starts with context. Mike doesn't need to read this. `/leftoff` rewrites it each time. Keep it under ~20 lines, and drop anything stale.

## Open threads
- Lesson 13 try-it (`lessons/lesson13_try.py`, his area calculator + 2 Enter binds) not checked. Binds look right. Bugs to lead him to: line 37 `ValueError.__cause__(e)` (`__cause__` is an attribute, not a method, so calling it crashes; he probably wants `str(e)` or his own message). Line 38 `setNumber(area)` runs after the except, so bad input gives UnboundLocalError (area never set). Ask: "what happens after the pop-up closes?"
- Never ran the "delete `lambda event:`" experiment in lesson13.py.
- Then homework 9-4 (needs only Lesson 13). Then Lessons 10-12. Remind him homework = exact spec text (he changed the Lesson 9 label to start at 2, reasoned well).
- Side project for later: his own encoder/obfuscator (Caesar cipher). Asked what he'd protect, no answer yet.
- Laptop still needs the autopep8 extension.

## Hint ladder state
- No hints given on Lesson 13 try-it.

## What works with Mike (beyond CLAUDE.md)
- Talk like a homie. Play along with jokes, then back to code. "oh shit" may mean "I don't know", not "I broke something". Ask before assuming.
- Tiny `py -c` demos make abstract stuff click (did it for `__str__` and class.method(obj)).
- Mapping a new case onto one that already worked (e.__str__() -> ValueError.__str__(e)) fixed his confusion. He mixed up class/object order twice first.
- He goes down rabbit holes (Ctrl+click into Pylance stubs). Answer, then steer back. "boom" = check. "choose" = just pick.
- Learning output style is on: use ✶ Insight boxes.

## Setup
- Git remote `mainremote`. Desktop uses `http.sslBackend schannel`. 2026-11-15 session was on the laptop.
- `.vscode/settings.json`: autopep8, `--ignore=E251`, format on save off.
- Homework repo (Cengage, graded, read-only for me): github.com/cengage-csp-students-prod-4/9780357881019-fundamentals-of-python-3e-2f1c5246-2300-4dcb-b487-b6a87a876d81, branch `template`. Never write there.
