---
name: quiz
description: Quiz Mike with three quick questions on what he's studying so it sticks. Use when he asks to be quizzed, wants to review, or has a few spare minutes.
argument-hint: "[chapter or topic, optional]"
---

Quiz topic: $ARGUMENTS

If no topic was given, use the chapter he's working in, focusing on lessons he's checked off or listed under "Hard stuff" in `study/progress.md`.

Ask three short questions, **one at a time**, waiting for each answer:

1. **What does this do?** Show a 3 to 6 line snippet and ask what it prints or does.
2. **Spot the bug.** Show a 3 to 6 line snippet with one common mistake.
3. **How would you...?** A plain-words question, no code needed.

After each answer, say whether it's right, explain in a sentence or two, then ask the next one. At the end, give his score out of 3 and add any topic he missed to "Hard stuff" in `study/progress.md`.

Keep the snippets different from the guide examples he already practiced.
