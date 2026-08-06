---
name: numbered-navigation
description: End every non-trivial result with clear numbered next actions, and use the same numbering when the person types a number to continue. Preserve task-local numbering and keep the recommended route obvious.
---

# Numbered navigation

After every non-trivial answer, completed task, diagnosis, plan, or visible
artifact, finish with:

```text
Куда двигаться:
1 = ⭐ Recommended safe route
Почему: One short reason
2 = Alternative
0 = Do all safe visible routes
Реко: 1
```

- Use `N = text`, not paragraphs of options.
- Put exactly one `⭐` on the recommended route. Put `Почему:` on the next line,
  never inside a route.
- Offer no more than three positive routes to a beginner.
- Continue from the last visible number while the same task remains active.
- Treat a typed number as selection of that route.
- Keep external, paid, destructive, or account actions behind exact approval.
- When only one safe continuation exists, show that one route plus `0`.
- Skip the menu only for a one-word acknowledgement or a simple factual answer
  that did not perform work.
- Before finalizing, verify that `Реко:` points to an existing route and that
  no route contains the word `Почему:`.
