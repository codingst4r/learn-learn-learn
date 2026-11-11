---
name: leftoff
description: Save where Mike left off before he stops working. Use when he says he's done for now, has to go, or wants to save his progress.
---

Update `study/progress.md` so Mike (and the next session) can pick up fast.

1. Ask in one line: "Anything to add about where you're stopping?" If he's in a hurry or says no, skip it.
2. Update the file. Keep it short, and replace old content instead of piling it up:
   - **Where I left off**: today's date, the exercise or lesson, what's working, and the exact next step (for example: "next: make the `<<<<` button convert C to F").
   - **Done**: check off lessons and exercises he finished this session.
   - **Hard stuff**: add concepts he struggled with today. Remove ones he's clearly got now.
   - **Session log**: add one line for today at the top. Keep only the last 5.
3. Rewrite `study/claude-notes.md` (your private notes, Mike doesn't need to read them). Replace stale content, and keep it under ~20 lines:
   - **Open threads**: unfinished fixes, questions he didn't answer, what he's about to start.
   - **Hint ladder state**: which try-it, which rung he's reached, what he's already tried.
   - **What works with Mike**: anything new you learned about how he learns.
   - **Setup**: only if something about his computers or git changed.
   Don't mention this step to him unless he asks.
4. Sync to GitHub so his other computer gets it:
   - `git add -A`, then `git commit` with a short message like "Progress 2026-11-10: finished lesson 7".
   - `git push`. If it's rejected because the other computer pushed first, run `git pull` and push again.
   - Never force-push or throw away changes. If there's a merge conflict, or the push fails (no login, no internet), stop and tell him in plain words. His progress is still saved on this computer.
5. Show him the "Where I left off" lines and tell him whether it's saved here only, or saved and pushed to GitHub.
