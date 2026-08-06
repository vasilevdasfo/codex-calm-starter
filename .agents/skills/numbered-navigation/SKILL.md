---
name: numbered-navigation
description: Give clear numbered choices when a beginner asks what to do next, faces several options, feels stuck, or types a number to continue. Preserve task-local numbering across the same task and keep the recommended route obvious.
---

# Numbered navigation

When a real choice remains:

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
- Skip a menu when only one obvious safe action exists; perform it and show proof.
- Before finalizing, verify that `Реко:` points to an existing route and that
  no route contains the word `Почему:`.
