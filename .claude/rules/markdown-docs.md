---
paths:
  - ".claude/**/*.md"
---

# Markdown Docs

> **Scope note (local adaptation):** upstream applies this rule to `**/*.md`. Here it is
> narrowed to `.claude/**/*.md` so it governs the installed Claude Code assets only and does
> not impose the upstream repo's layout on this repository's own docs. The directory
> conventions below (`best-practice/`, `implementation/`, `reports/`, `tips/`) describe the
> upstream [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> repo, not this one.

## Documentation Standards

- Keep files focused and concise — one topic per file
- Use relative links between docs (e.g., `../best-practice/claude-memory.md`), not absolute GitHub URLs
- Include back-navigation link at top of best-practice and report docs (see existing files for pattern)
- When adding a new concept or report, update the corresponding table in README.md (CONCEPTS or REPORTS)

## Structure Conventions

- Best practice docs go in `best-practice/`
- Implementation docs go in `implementation/`
- Reports go in `reports/`
- Tips go in `tips/`
- Changelog tracking goes in `changelog/<category>/`

## Formatting

- Use tables for structured comparisons (see README CONCEPTS table as reference)
- Use badge images from `!/tags/` for visual consistency when linking best-practice or implementation docs
- Keep headings hierarchical — don't skip levels (e.g., don't jump from `##` to `####`)
