# Claude Code setup — installed from `claude-code-best-practice`

This directory is an install of [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice).

| | |
|---|---|
| Upstream | `https://github.com/shanraisshan/claude-code-best-practice.git` |
| Commit | `20d8f78bdc18f7a637bbb3f3902f1c1e3a3b8563` (2026-08-24) |
| Scope | `.claude/` tree + root `.mcp.json`, trimmed to what applies to this repo |
| License | MIT (upstream) |

## What's here

| Path | What it is |
|---|---|
| `settings.json` | Permissions, hooks wiring, status line, output style, `plansDirectory`, env |
| `hooks/` | Cross-platform sound-notification system (`scripts/hooks.py`, 30 hook events, `sounds/`) |
| `agents/` | Subagents: `weather-agent`, `time-agent` |
| `commands/` | `/weather-orchestrator`, `/time-command` |
| `skills/` | `weather-fetcher`, `weather-svg-creator`, `time-skill`, `agent-browser` |
| `rules/` | Path-scoped memory rule (`markdown-docs.md`) |
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

4. **Chinese labels** — every `description` is prefixed with a bracketed Chinese label so the
   `/` menu and skill picker are scannable. `name` fields are untouched (the spec requires
   lowercase ASCII matching the directory, and `validate-skill.yml` enforces it).
5. **Trimmed 21 upstream-only files.** Two complete families were removed because nothing in
   this repository uses them, and one of them was actively dangerous:

   - **presentation family (7)** — `rules/presentation.md` routed to three `presentation-*`
     agents, which in turn used three `presentation/*` skills. All of them target
     `presentation/**` HTML decks that live only in the upstream repo.
   - **workflows family (14)** — eight `workflows:*` commands plus the six research agents they
     call. Four of those commands rewrite the upstream repo's `README.md` tables; run here they
     would overwrite this repository's own README.

   Both families were deleted whole, so no orphaned agent or skill is left behind. Everything
   is recoverable from git history if you want any of it back.

6. **`skills/weather-fetcher/SKILL.md`** — `allowed-tools` changed from a YAML list to a
   space-delimited string. Upstream ships it as a list, which violates the Agent Skills spec
   (`[allowed-tools-format] Allowed-tools must be a space-delimited string`) and fails this
   repository's `validate-skill.yml`. `agent-browser` already used the string form upstream.

   Note: `user-invocable` (on `weather-fetcher` and `time-skill`) is a Claude Code extension and
   is not in the spec's recognised field set, so the validator emits an `[unknown-field]`
   warning for it. The workflow runs with `fail-on-warning: false`, and the field is
   functional in Claude Code, so it is left as upstream wrote it.

## Review before relying on it

`settings.json` ships upstream's permission set, which allows `Edit(*)`, `Write(*)` and
`Bash(*)` without prompting (the `ask` list still intercepts `rm`, `chmod`, package managers,
`docker`, `kubectl`, etc.). Tighten `permissions.allow` if you want narrower auto-approval.

## Updating

```bash
git clone --depth 1 https://github.com/shanraisshan/claude-code-best-practice.git /tmp/ccbp
diff -ru .claude /tmp/ccbp/.claude
```

Re-apply the local adaptations above after any sync — including the trim, or the two removed
families will come back.
