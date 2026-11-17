# Notes for Claude

> Claude's own working notes so a new session on either computer starts with context. Mike doesn't need to read this. `/leftoff` rewrites it each time. Keep it under ~20 lines, and drop anything stale.

## Open threads
- DESKTOP: has untracked, unpushed `lessons/lesson12.py` + `lesson12_try.py` (just the pasted example). The laptop pushed its own versions on 2026-11-17, so `git pull` on the desktop will fail with "untracked working tree files would be overwritten". He should delete the desktop copies first. If /start's pull fails like that, explain it and have him delete them (nothing original in them).
- Lesson 10 try-it (`lessons/lesson10_try.py`, ~1.5 KB) started, not checked. He saw `%-6d` vs `%6s` header misalignment; I said keep header and column widths/alignment matching.
- Next: Lesson 11, then homework 9-7 (TidBit schedule, needs text area + format codes). Homework 9-1..9-6 passed (9-6 on 2026-11-17). Remind: homework = exact spec text.
- Lesson 13 leftovers: optional rename `errorHandler` to `getArea`, maybe stray debug prints. Never ran the "delete `lambda event:`" experiment.
- Side project for later: encoder/obfuscator (Caesar cipher). Asked what he'd protect, no answer.
- Laptop still needs the autopep8 extension.

## Hint ladder state
- Lesson 10 try-it: no hints given.

## What works with Mike (beyond CLAUDE.md)
- Talk like a homie. "oh shit" may mean "I don't know". Ask before assuming.
- Tiny `py -c` demos with `[ ]` around output make formatting/abstract stuff click. Break-it tests (delete the default radio button) land great.
- He finds "works by accident" things fun (orient = "HORIZONTAL" vs "horizontal"). Point them out.
- Markdown in chat eats leading spaces. Use backticks when spaces matter.
- Rabbit holes: answer briefly, steer back. "boom"/"/check" = check. "choose" = pick. "ts" = this.
- Learning output style on: use ✶ Insight boxes.

## Setup
- Git remote `mainremote`. Desktop uses `http.sslBackend schannel`. 2026-11-17 on laptop.
- Homework repo (Cengage, graded, read-only for me): github.com/cengage-csp-students-prod-4/9780357881019-fundamentals-of-python-3e-2f1c5246-2300-4dcb-b487-b6a87a876d81, branch `template`. I clone it into my scratchpad (`hw/`) to read `chapter9/exNN/results/task1.txt`. Never write there.
