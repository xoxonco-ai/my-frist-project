# Claude Code setup — installed from `claude-code-best-practice`

This directory is an install of [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice).

| | |
|---|---|
| Upstream | `https://github.com/shanraisshan/claude-code-best-practice.git` |
| Commit | `20d8f78bdc18f7a637bbb3f3902f1c1e3a3b8563` (2026-08-24) |
| Scope | full `.claude/` tree + root `.mcp.json` |
| License | MIT (upstream) |

## What's here

| Path | What it is |
|---|---|
| `settings.json` | Permissions, hooks wiring, status line, output style, `plansDirectory`, env |
| `hooks/` | Cross-platform sound-notification system (`scripts/hooks.py`, 30 hook events, `sounds/`) |
| `agents/` | Subagents: `weather-agent`, `time-agent`, presentation agents, workflow research agents |
| `commands/` | Slash commands, incl. `/weather-orchestrator` and the `workflows:*` research commands |
| `skills/` | `weather-fetcher`, `weather-svg-creator`, `time-skill`, `agent-browser`, `presentation/*` |
| `rules/` | Path-scoped memory rules (`markdown-docs.md`, `presentation.md`) |
| `agent-memory/` | Upstream demo of the auto-memory feature (`weather-agent`) |
| `../.mcp.json` | Project MCP servers: `playwright`, `context7`, `deepwiki` (via `npx`) |

## Try it

```bash
claude
/weather-orchestrator     # command -> agent -> skill demo; writes orchestration-workflow/
/time-command             # minimal command -> skill demo
```

Hook sounds need an audio player on `PATH`: `afplay` (macOS, built in), or `paplay` /
`aplay` / `ffplay` / `mpg123` (Linux). Without one, `hooks.py` exits 0 silently — hooks never
block a session.

## Local adaptations

Everything is upstream-verbatim except:

1. **`settings.json`** — dropped the upstream author's personal `spinnerVerbs` and
   `spinnerTipsOverride`; replaced the placeholder `statusLine` with `<dir> · <branch>`.
2. **`rules/markdown-docs.md`** — `paths` narrowed from `**/*.md` to `.claude/**/*.md` so the
   upstream repo's doc layout is not imposed on this repository's own markdown.
3. **Root `.gitignore`** — `.claude/` was previously ignored wholesale (for `npx skills add`
   artifacts). It is now `.claude/*` with explicit re-includes, so this install is tracked
   while `npx`-installed skills under `.claude/skills/` stay ignored. Adding a new tracked
   skill here means adding a matching `!.claude/skills/<name>/` line.

`rules/presentation.md` is scoped to `presentation/**`, which does not exist here, so it stays
dormant. The `presentation-*` agents and skills are upstream demo material and are safe to
delete if you don't want them in the `/` menu.

## Review before relying on it

`settings.json` ships upstream's permission set, which allows `Edit(*)`, `Write(*)` and
`Bash(*)` without prompting (the `ask` list still intercepts `rm`, `chmod`, package managers,
`docker`, `kubectl`, etc.). Tighten `permissions.allow` if you want narrower auto-approval.

## Updating

```bash
git clone --depth 1 https://github.com/shanraisshan/claude-code-best-practice.git /tmp/ccbp
diff -ru .claude /tmp/ccbp/.claude
```

Re-apply the three local adaptations above after any sync.
