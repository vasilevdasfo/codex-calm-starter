# Privacy

## Safe by default

- The release contains blank templates, not a person's profile or progress.
- Filled `ABOUT_ME.md`, `MY_PROGRESS.md`, `CLIENT_SYNC.json`, preflight reports,
  installation ID, and first-result files stay local and are ignored by Git.
- No account connector, MCP server, hook, automation, telemetry, or remote
  access is configured by this starter.
- Skills provide instructions and local scripts. They do not transmit data by themselves.

## No hidden tracking

`download`, `install`, `first_run`, and `first_result` are different events.
GitHub's asset count proves only a download. It does not identify a person or
prove installation.

The optional support check-in creates a local `PREVIEW_ONLY` file with
`destination: UNCONFIGURED` and `consent_to_send: false`. Connecting a website
requires a separate approved configuration and privacy notice.

## Do not store or migrate

Do not put passwords, one-time codes, private keys, tokens, cookies, payment
details, identity documents, another person's messages, or another person's
`.codex`, `.claude`, memory, or account data in this workspace.

## External actions

Before sending, publishing, deploying, purchasing, connecting an account,
changing access, or deleting data, Codex must show the exact action and wait
for explicit confirmation.
