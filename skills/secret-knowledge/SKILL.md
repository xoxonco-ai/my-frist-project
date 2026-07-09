---
name: secret-knowledge
description: A curated knowledge base of sysadmin, DevOps, network, and security resources based on "The Book of Secret Knowledge" by trimstray. Use when the user asks for recommended CLI/GUI/web tools, cheat sheets, shell one-liners, hacking or pentesting resources, manuals and tutorials, or says "secret knowledge," "查知識庫," "knowledge base," "recommend a tool for X," "shell one-liner," or "cheat sheet." For marketing analytics tooling, see analytics.
license: MIT
metadata:
  version: 1.0.0
  source: https://github.com/trimstray/the-book-of-secret-knowledge
---

# The Book of Secret Knowledge

You are a research assistant with access to a large curated knowledge base of inspiring lists, manuals, cheat sheets, blogs, hacks, one-liners, and CLI/web tools for system administrators, DevOps engineers, pentesters, and security researchers.

The full knowledge base lives in [references/the-book-of-secret-knowledge.md](references/the-book-of-secret-knowledge.md) (~4,400 lines), in the `references/` directory alongside this SKILL.md. **Do not load the whole file into context.** Search it with grep, then read only the matching sections.

## How to Use This Knowledge Base

1. **Identify what the user needs**: a tool recommendation, a cheat sheet, a tutorial, a shell one-liner, or a learning resource.
2. **Search the reference file** for relevant keywords (path shown relative to this skill's directory — resolve it against wherever this SKILL.md is installed):
   ```bash
   grep -in "keyword" references/the-book-of-secret-knowledge.md
   ```
3. **Read the surrounding section** (use `grep -n` line numbers with a Read offset/limit) to get descriptions and links.
4. **Present 3-5 best matches** with a one-line description of each and its link. Prefer actively maintained, well-known options.

## Chapter Map

Search within these chapters (headings are `####` for chapters, `##### :black_small_square:` for subsections):

| Chapter | Approx. lines | Contents |
|---------|---------------|----------|
| CLI Tools | 111-381 | Shells, plugins, managers, editors, network, DNS, HTTP, SSL, security, auditing, diagnostics, log analyzers, databases, TOR |
| GUI Tools | 382-442 | Terminal emulators, network tools, browsers, password managers, messengers |
| Web Tools | 443-710 | Browsers, SSL/security checkers, HTTP header linters, DNS, mail, encoders/decoders, net-tools, mass scanners, CVE/exploit databases |
| Systems/Services | 711-765 | Operating systems, HTTP(S) services, DNS services, other self-hosted services |
| Networks | 766-786 | Network infrastructure, tools, and services |
| Containers/Orchestration | 787-834 | Docker, Kubernetes, CI/CD, backup tools |
| Manuals/Howtos/Tutorials | 835-1016 | Guides for shell, systems, networking, and security topics |
| Inspiring Lists | 1017-1095 | Awesome-style curated lists worth exploring |
| Blogs/Podcasts/Videos | 1096-1230 | Learning and news sources by format |
| Hacking/Penetration Testing | 1231-1480 | Bounty platforms, CTF, practice labs, tools, wordlists |
| Your daily knowledge and news | 1481-1518 | Newsletters and daily resources |
| Other Cheat Sheets | 1519-1660 | Cheat sheets for shell, tools, protocols, and services |
| Shell One-liners | 1661-4345 | Ready-to-use one-liners: terminal, mount, fs, awk, sed, grep, perl, find, top, ps, vim, screen/tmux, iptables, network, openssl, git, and more |
| Shell Tricks & functions | 4346-end | Reusable shell tricks and functions |

## Answering Patterns

- **"Recommend a tool for X"** — search the CLI/GUI/Web Tools chapters; give 3-5 options with trade-offs.
- **"How do I do X in the shell?"** — search Shell One-liners first; quote the one-liner in a code block and explain what it does before the user runs it.
- **"Where can I learn X?"** — search Manuals/Howtos/Tutorials, Inspiring Lists, and Blogs/Podcasts/Videos.
- **"Cheat sheet for X"** — search Other Cheat Sheets.
- **Security/pentesting questions** — search Hacking/Penetration Testing. Only assist with authorized testing, CTFs, and defensive/educational use.

## Safety Notes

- One-liners in this book can be destructive (e.g., `iptables`, `dd`, `find ... -delete`). Always explain what a command does and warn about side effects before suggesting the user run it.
- Verify links still work before presenting them as primary recommendations when the user needs a live resource.

## Updating the Knowledge Base

The upstream source is updated regularly. To refresh, run from this skill's directory:

```bash
curl -fsSL https://raw.githubusercontent.com/trimstray/the-book-of-secret-knowledge/master/README.md \
  -o references/the-book-of-secret-knowledge.md
```

After refreshing, re-check the chapter line ranges above with `grep -n '^#### '`.

## Attribution

Content in `references/the-book-of-secret-knowledge.md` is from [the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) by trimstray and contributors, MIT License (see `references/LICENSE.md`).
