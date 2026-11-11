# Notes for Claude

> Claude's own working notes so a new session on either computer starts with context. Mike doesn't need to read this. `/leftoff` rewrites it each time. Keep it under ~20 lines, and drop anything stale.

## Open threads
- Lesson 6 try-it (`lessons/lesson6_try.py`): output field still uses `state = "disabled"`; suggested `"readonly"`. Also asked whether the "Area:" label's `sticky = "E"` (others are "W") was on purpose. No answer yet.
- Lesson 4 launcher (`lessons/lesson4.py`): typing `cat` at the menu crashes with ValueError. Offered try/except as an optional challenge; he skipped it. Lesson 8 covers the GUI version.
- Next up: Lesson 7, then homework 9-3 (temperature converter: lessons 3, 5, 6, 7). He asked to aim practice at homework.

## Hint ladder state
- No try-it in progress.

## What works with Mike (beyond CLAUDE.md)
- When he says "no distractions" / "keep moving", drop side challenges and go straight to the next step.
- He experiments on his own (launcher menu, Reset button, image in title screen). Praise it and explain what happened.
- Explain-it-back questions land well. Wrong first guesses fixed by a different angle (e.g. bouncer analogy for .gitignore).
- He says "boom" when he wants a check.

## Setup
- Git repo synced to GitHub (remote is named `mainremote`). Laptop and desktop both clone it. Credential manager set up on the laptop.
- Learned so far: .gitignore only skips untracked files; `git rm --cached` untracks; commits only include staged files.
- Desktop commits with a different git name/email than the laptop (harmless).
