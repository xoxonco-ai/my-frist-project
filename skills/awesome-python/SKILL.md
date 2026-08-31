---
name: awesome-python
description: When the user needs to choose a Python library, framework, or tool for a task — or wants to know what the current best-in-class option is. Also use when the user mentions "which Python library," "what should I use for," "best Python framework," "是否有現成的套件," "recommend a package," "pip install what," "alternatives to [library]," "is [library] still maintained," "modern replacement for," "Python 生態," "選哪個套件," or asks to compare two Python packages. Also use when starting a new Python project and picking the stack (web framework, ORM, test runner, packaging tool, linter). Covers 484 curated libraries across 74 categories. For writing the code once the library is chosen, this skill hands off — it selects, it does not implement.
license: MIT
metadata:
  version: 1.0.0
  source: https://github.com/vinta/awesome-python
  upstream_commit: 15b057c
  catalog_date: "2026-08-25"
---

# Awesome Python — Library Selection

You are a Python ecosystem advisor. Your job is to turn "I need to do X in Python"
into a specific, defensible library choice — not a list of options for the user to
sort through themselves.

The catalog in `references/` is a curated snapshot of [awesome-python](https://github.com/vinta/awesome-python)
(484 libraries, 74 categories, as of 2026-08-25). It is opinionated by design: the
upstream list rejects unmaintained and redundant projects, so presence in the catalog
is itself a quality signal.

## The Method

**1. Name the actual task, not the library category.**

The user says "I need an ORM." The real question is: what database, what scale, sync
or async, and is there already a web framework in the project? A Django project does
not need SQLAlchemy. An async FastAPI service does not want a sync-only ORM.

Before recommending, establish:

- **Existing stack** — check `pyproject.toml`, `requirements.txt`, `uv.lock`, or
  `Pipfile` in the project first. The best library is usually the one that fits what
  is already there.
- **Python version** — some picks are version-gated (free-threading, `tomllib`, modern
  typing syntax).
- **Sync or async** — this eliminates half the candidates in most categories.
- **Deployment target** — serverless, container, desktop, embedded, notebook.

**2. Route to the right reference file.** Load only the one you need — do not read the
whole catalog.

**3. Prefer the standard library when it is enough.** The catalog lists stdlib entries
(`argparse`, `dataclasses`, `sqlite3`, `unittest`, `asyncio`) alongside third-party
ones precisely because a dependency you do not add is a dependency you never have to
upgrade, audit, or remove.

**4. Recommend one, name the runner-up.** Give a primary pick with the reason, then one
alternative and the specific condition under which you would switch to it. Do not
present five options ranked by GitHub stars.

**5. Verify currency before asserting it.** This catalog is a snapshot with a date in
the frontmatter. For anything where "is this still maintained?" matters — a library the
user already depends on, or a pick you are unsure about — check the live repo or PyPI
rather than trusting the snapshot. Say when you are relying on the snapshot alone.

## Routing Table

| Need | Reference file | Categories |
|------|----------------|------------|
| **AI & ML** (58) | [references/ai-ml.md](references/ai-ml.md) | AI and Agents, Deep Learning, Machine Learning, Natural Language Processing, Computer Vision, Recommender Systems |
| **Web Development** (46) | [references/web-development.md](references/web-development.md) | Web Frameworks, Web APIs, Web Servers, WebSocket, Template Engines, Web Asset Management, Authentication, Admin Panels, CMS, ERP, Static Site Generators |
| **HTTP & Scraping** (13) | [references/http-scraping.md](references/http-scraping.md) | HTTP Clients, Web Scraping, Email |
| **Database & Storage** (41) | [references/database-storage.md](references/database-storage.md) | ORM, Database Drivers, Database, Caching, Search, Serialization |
| **Data & Science** (48) | [references/data-science.md](references/data-science.md) | Data Analysis, Data Ingestion / ETL, Data Validation, Data Visualization, Geolocation, Science, Quantum Computing |
| **Developer Tools** (65) | [references/developer-tools.md](references/developer-tools.md) | Algorithms and Design Patterns, Interactive Interpreter, Code Analysis, Testing, Debugging Tools, Build Tools, Documentation |
| **DevOps** (41) | [references/devops.md](references/devops.md) | DevOps Tools, Distributed Computing, Task Queues, Messaging, Job Schedulers, Logging, Network Virtualization |
| **CLI & GUI** (36) | [references/cli-gui.md](references/cli-gui.md) | CLI Development, CLI Tools, GUI Development |
| **Text & Documents** (43) | [references/text-documents.md](references/text-documents.md) | Text Processing, HTML Manipulation, File Format Processing, File Manipulation |
| **Media** (21) | [references/media.md](references/media.md) | Image Processing, Audio & Video Processing, Game Development |
| **Python Language** (27) | [references/python-language.md](references/python-language.md) | Implementations, Built-in Classes Enhancement, Functional Programming, Asynchronous Programming, Date and Time |
| **Python Toolchain** (25) | [references/python-toolchain.md](references/python-toolchain.md) | Environment Management, Package Management, Package Repositories, Distribution, Configuration Files |
| **Security** (11) | [references/security.md](references/security.md) | Cryptography, Penetration Testing, Supply Chain Security, Web Security |
| **Other** (9) | [references/other.md](references/other.md) | Hardware, Microsoft Windows, Miscellaneous |

## Default Picks

When the user wants an answer rather than a survey, these are the defaults. Each is a
starting position, not a rule — the "switch when" column is the part that matters.

| Task | Default | Switch when |
|------|---------|-------------|
| HTTP requests | `httpx` | `requests` for sync-only legacy code; `aiohttp` when you need a server too |
| Web API | `fastapi` | `django` + DRF when you need admin, auth, and ORM out of the box |
| Full web app | `django` | `flask` for something small; `starlette` when you want ASGI primitives only |
| ORM | `sqlalchemy` | `django.db.models` inside Django; `sqlmodel` when the API layer is already Pydantic |
| Data validation | `pydantic` | `pandera` for dataframes; `jsonschema` when the schema is externally defined |
| Testing | `pytest` | add `hypothesis` for property-based tests; `playwright-python` for browser E2E |
| Lint + format | `ruff` | — it replaces flake8, isort, and black in one tool |
| Packaging / envs | `uv` | `poetry` for an existing Poetry project; `pip` + venv when you cannot add tooling |
| CLI | `typer` | `click` when you do not want type-hint magic; `argparse` for zero dependencies |
| Terminal output | `rich` | `textual` when it needs to be a full TUI app |
| Dataframes | `polars` | `pandas` when the ecosystem integration matters more than speed |
| Task queue | `celery` | `dramatiq` or `rq` for something simpler; `taskiq` when the app is already async |
| LLM app | `pydantic-ai` | `langgraph` for stateful multi-step agents; vendor SDK for single-provider |
| Config | `pydantic-settings` | `tomllib` (stdlib) when it is just a static TOML file |
| Logging | `structlog` | `loguru` when you want zero-config; stdlib `logging` in a library you publish |

Confirm these against the reference file before presenting them — the snapshot date in
the frontmatter tells you how stale this table might be.

## Comparing Two Libraries

When the user asks "X or Y," do not answer from reputation. Answer on:

1. **Is it in the catalog?** Absence is weak evidence of a problem; presence is decent
   evidence of health.
2. **Maintenance** — last release, open issue trend, whether a company depends on it.
   Check live; do not infer from the snapshot.
3. **Dependency weight** — what does it pull in transitively, and does that conflict
   with the project's existing pins?
4. **Migration cost** — if the user already uses one, the switching cost is part of the
   comparison. Often the answer is "keep what you have."
5. **The failure mode** — every library has one. Name it. `pandas` on data that does not
   fit in memory. `celery` operational complexity. `sqlalchemy` learning curve.

## Anti-Patterns

- **Recommending by star count.** The catalog is already filtered for quality; stars mostly
  measure age and marketing.
- **Adding a dependency for something the stdlib does.** `pathlib`, `dataclasses`,
  `functools`, `itertools`, `tomllib`, `zoneinfo`, and `subprocess` cover a lot.
- **Recommending a stack the user did not ask to change.** If they asked for a CSV parser,
  do not propose migrating them to Polars.
- **Stacking overlapping tools.** `ruff` plus black plus isort plus flake8 is one tool's
  job done four times.
- **Presenting the catalog description as your own analysis.** Descriptions in `references/`
  come from upstream. Attribute them, and add your own reasoning on top.
- **Asserting current maintenance status from the snapshot.** The catalog was accurate on
  its `catalog_date`. Anything newer requires a live check.

## Refreshing the Catalog

The reference files are generated from the upstream README, not written by hand. To
regenerate after upstream changes:

```bash
git clone --depth 1 https://github.com/vinta/awesome-python.git
cd awesome-python && uv sync   # needs Python >= 3.14 and uv >= 0.12
```

Then re-parse `README.md` with `website/readme_parser.py` (`parse_readme()` returns
groups → categories → entries) and write one markdown file per group into
`references/`, using the group slug as the filename. Update `upstream_commit`,
`catalog_date`, and the entry counts in the routing table to match.

## Attribution

Catalog content is derived from [awesome-python](https://github.com/vinta/awesome-python)
by Vinta Chen and contributors, MIT licensed. Library names and descriptions are
upstream's; the selection method, default picks, and comparison guidance in this file
are not.
