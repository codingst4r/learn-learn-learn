# Notes for Claude

> Claude's own working notes so a new session on either computer starts with context. Mike doesn't need to read this. `/leftoff` rewrites it each time. Keep it under ~20 lines, and drop anything stale.

## Open threads
- Next: homework 9-3 (temperature converter: lessons 3, 5, 6, 7) or Lesson 8 first. He asked to aim practice at homework. Remind him to follow the spec exactly on homework (he likes adding his own twists).
- Lesson 7 try-it accepted as his own design (warn once at 0, then disable -1). Small leftover: indent on line 26 is 12 spaces; Reset within 2 s gets overwritten by the pending `after`.
- Lesson 4 launcher: typing `cat` crashes with ValueError. Lesson 8 covers the GUI version.

## Hint ladder state
- No try-it in progress.

## What works with Mike (beyond CLAUDE.md)
- He experiments on his own and pushes back with reasons. Before correcting him, check what he actually means. On `self` I argued past his real point once (he meant "self in newClass has nothing to do with ClickCounter," which was right).
- Running a tiny non-GUI demo (two objects, print self) made the point concrete fast.
- Explain-it-back questions land well. When he says "choose," just pick and give a reason.
- "no distractions" / "keep moving" = drop side challenges. "boom" = he wants a check.

## Setup
- Git remote `mainremote` (GitHub). On 2026-11-11 the laptop failed pull with an SSL cert error; he ran `git config --global http.sslBackend schannel` and it worked.
- Desktop commits with a different git name/email than the laptop (harmless).
