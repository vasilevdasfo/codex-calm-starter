---
name: privacy-permissions
description: Protect a beginner before sending, publishing, deploying, purchasing, deleting, connecting an account, changing access, or handling sensitive data. Trigger on "отправь", "опубликуй", "подключи", "удали", "send", "publish", "connect", or any external or irreversible action.
---

# Privacy and permissions

## Gate

Before an external or irreversible action:

1. Name the exact action, destination, affected person, account, and data.
2. Show the exact draft, payload, file, or change.
3. Explain what stays local and what leaves the computer.
4. Wait for explicit confirmation of that exact action.
5. Execute once and verify the destination state.
6. If the result is unknown, inspect the destination before any retry.

## Never request or migrate

- passwords or one-time codes;
- private keys, cookies, tokens, or browser sessions;
- banking or identity documents;
- another person's private messages or files;
- another user's `.codex`, `.claude`, memory, or account profile.

Connect Gmail, Calendar, Telegram, Drive, GitHub, or another service one at a
time using the current owner's local authorization and identity check.
