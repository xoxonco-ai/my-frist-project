# Developer Tools

Categories: Algorithms and Design Patterns, Interactive Interpreter, Code Analysis, Testing, Debugging Tools, Build Tools, Documentation

## Algorithms and Design Patterns

Python implementation of data structures, algorithms and design patterns. Also see [awesome-algorithms](https://github.com/tayllan/awesome-algorithms).

**Algorithms**

- [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers) — Fast and pure-Python implementation of sorted collections.
- [algorithms](https://github.com/keon/algorithms) — Minimal examples of data structures and algorithms.
- [thealgorithms](https://github.com/TheAlgorithms/Python) — All Algorithms implemented in Python.

**Design Patterns**

- [transitions](https://github.com/pytransitions/transitions) — A lightweight, object-oriented finite state machine implementation.
- [python-patterns](https://github.com/faif/python-patterns) — A collection of design patterns in Python.
- [python-statemachine](https://github.com/fgmacedo/python-statemachine) — Expressive statecharts and finite state machines with a declarative API, in sync and async codebases.

## Interactive Interpreter

Interactive Python interpreters (REPL).

- [ipython](https://github.com/ipython/ipython) — A powerful interactive Python shell, and the kernel behind Jupyter notebooks.
- [jupyter](https://github.com/jupyter/notebook) — A rich toolkit to help you make the most out of using Python interactively.
  - Also see: [awesome-jupyter](https://github.com/markusschanta/awesome-jupyter)
- [marimo](https://github.com/marimo-team/marimo) — Transform data and train models, feels like a next-gen notebook, stored as Git-friendly Python.
- [ptpython](https://github.com/prompt-toolkit/ptpython) — Advanced Python REPL built on top of the [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit).

## Code Analysis

Tools of static analysis, linters and code quality checkers. Also see [awesome-static-analysis](https://github.com/analysis-tools-dev/static-analysis).

**Code Analysis**

- [vulture](https://github.com/jendrikseipp/vulture) — A tool for finding and analyzing dead Python code.
- [prospector](https://github.com/prospector-dev/prospector) — A tool to analyze Python code.
- [repowise](https://github.com/repowise-dev/repowise) — Codebase intelligence that indexes repos into dependency graphs, git history, and auto-generated docs with dead code detection.
- [complexipy](https://github.com/rohaquinlop/complexipy) — Cognitive complexity analysis for Python code, written in Rust.

**Git Hooks**

- [pre-commit](https://github.com/pre-commit/pre-commit) — A framework for managing and maintaining multi-language pre-commit hooks.

**Linters and Formatters**

- [ruff](https://github.com/astral-sh/ruff) — An extremely fast Python linter and code formatter.
- [black](https://github.com/psf/black) — The uncompromising Python code formatter.
- [isort](https://github.com/PyCQA/isort) — A Python utility / library to sort imports.
- [pylint](https://github.com/pylint-dev/pylint) — A fully customizable source code analyzer.
- [flake8](https://github.com/PyCQA/flake8) — A wrapper around `pycodestyle`, `pyflakes` and McCabe.
  - Also see: [awesome-flake8-extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions)
- [bandit](https://github.com/PyCQA/bandit) — A tool designed to find common security issues in Python code.

**Refactoring**

- [rope](https://github.com/python-rope/rope) — Rope is a python refactoring library.

**Type Checkers**

- [mypy](https://github.com/python/mypy) — Check variable types during compile time.
- [ty](https://github.com/astral-sh/ty) — An extremely fast Python type checker and language server.
- [pyright](https://github.com/microsoft/pyright) — Full-featured static type checker for Python from Microsoft, the engine behind Pylance.
- [pyrefly](https://github.com/facebook/pyrefly) — A fast type checker and language server for Python.

**Type Annotations Generators**

- [monkeytype](https://github.com/Instagram/MonkeyType) — A system for Python that generates static type annotations by collecting runtime types.

## Testing

Libraries for testing codebases and generating test data. Also see [awesome-python-testing](https://github.com/cleder/awesome-python-testing).

**Frameworks**

- [pytest](https://github.com/pytest-dev/pytest) — A mature full-featured Python testing tool.
  - Also see: [awesome-pytest](https://github.com/augustogoulart/awesome-pytest)
- [hypothesis](https://github.com/HypothesisWorks/hypothesis) — Hypothesis is an advanced Quickcheck style property based testing library.
- [robotframework](https://github.com/robotframework/robotframework) — A generic test automation framework.

**Test Runners**

- [tox](https://github.com/tox-dev/tox) — Auto builds and tests distributions in multiple Python versions
- [nox](https://github.com/wntrblm/nox) — Flexible test automation for Python.

**Browser Automation**

- [playwright-python](https://github.com/microsoft/playwright-python) — Python version of the Playwright testing and automation library.
- [selenium](https://github.com/SeleniumHQ/selenium) — Python bindings for [Selenium](https://selenium.dev/) [WebDriver](https://selenium.dev/documentation/webdriver/).
- [seleniumbase](https://github.com/seleniumbase/SeleniumBase) — Python framework for web automation & testing, with stealth options.

**Load Testing**

- [locust](https://github.com/locustio/locust) — Scalable user load testing tool written in Python.

**API Testing**

- [schemathesis](https://github.com/schemathesis/schemathesis) — A tool for automatic property-based testing of web applications built with Open API / Swagger specifications.

**Mock**

- [mock](https://docs.python.org/3/library/unittest.mock.html) — (Python standard library) A mocking and patching library.
- [responses](https://github.com/getsentry/responses) — A utility library for mocking out the requests Python library.
- [freezegun](https://github.com/spulec/freezegun) — Travel through time by mocking the datetime module.
- [vcrpy](https://github.com/kevin1024/vcrpy) — Record and replay HTTP interactions on your tests.
- [respx](https://github.com/lundberg/respx) — Mock HTTPX with awesome request patterns and response side effects.

**Object Factories**

- [factory_boy](https://github.com/FactoryBoy/factory_boy) — A test fixtures replacement for Python.
- [polyfactory](https://github.com/litestar-org/polyfactory) — mock data generation library with support to classes (continuation of `pydantic-factories`)

**Code Coverage**

- [coverage](https://github.com/coveragepy/coveragepy) — Code coverage measurement.

**Fake Data**

- [faker](https://github.com/joke2k/faker) — A Python package that generates fake data.
- [mimesis](https://github.com/lk-geimfari/mimesis) — is a Python library that help you generate fake data.

## Debugging Tools

Libraries for debugging code.

**pdb-like Debugger**

- [ipdb](https://github.com/gotcha/ipdb) — IPython-enabled [pdb](https://docs.python.org/3/library/pdb.html).
- [pudb](https://github.com/inducer/pudb) — A full-screen, console-based Python debugger.

**Tracing**

- [hunter](https://github.com/ionelmc/python-hunter) — A flexible code tracing toolkit.

**Profiler**

- [py-spy](https://github.com/benfred/py-spy) — A sampling profiler for Python programs. Written in Rust.
- [memray](https://github.com/bloomberg/memray) — A memory profiler that tracks allocations in Python code, native extensions, and the interpreter itself.
- [pyinstrument](https://github.com/joerick/pyinstrument) — A statistical wall-clock profiler with low overhead and readable call-tree output.
- [scalene](https://github.com/plasma-umass/scalene) — A high-performance, high-precision CPU, GPU, and memory profiler for Python.

**Others**

- [django-debug-toolbar](https://github.com/django-commons/django-debug-toolbar) — Display various debug information for Django.
- [icecream](https://github.com/gruns/icecream) — Inspect variables, expressions, and program execution with a single, simple function call.
- [flask-debugtoolbar](https://github.com/pallets-eco/flask-debugtoolbar) — A port of the django-debug-toolbar to flask.

## Build Tools

Compile software from source code. If you're looking for Python packaging/build tools, see [Package Management](#package-management).

- [invoke](https://github.com/pyinvoke/invoke) — A tool for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks.
- [scons](https://github.com/SCons/scons) — A software construction tool.
- [doit](https://github.com/pydoit/doit) — A task runner and build tool.

## Documentation

Libraries for generating project documentation.

- [sphinx](https://github.com/sphinx-doc/sphinx/) — Python Documentation generator.
  - Also see: [awesome-sphinxdoc](https://github.com/ygzgxyz/awesome-sphinxdoc)
- [mkdocs-material](https://github.com/squidfunk/mkdocs-material) — A documentation framework and Material Design theme built on MkDocs.
- [diagrams](https://github.com/mingrammer/diagrams) — Diagram as Code.
- [pdoc](https://github.com/mitmproxy/pdoc) — Epydoc replacement to auto generate API documentation for Python libraries.
- [zensical](https://github.com/zensical/zensical) — A modern static site generator for technical documentation.
