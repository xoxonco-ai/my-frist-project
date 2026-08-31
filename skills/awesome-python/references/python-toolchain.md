# Python Toolchain

Categories: Environment Management, Package Management, Package Repositories, Distribution, Configuration Files

## Environment Management

Libraries for Python version and virtual environment management.

- [virtualenv](https://github.com/pypa/virtualenv) — A tool to create isolated Python environments.
- [uv](https://github.com/astral-sh/uv) — An extremely fast Python version, package and project manager, written in Rust.
- [pyenv](https://github.com/pyenv/pyenv) — Simple Python version management.

## Package Management

Libraries for package and dependency management.

**Package Managers**

- [pip](https://github.com/pypa/pip) — The package installer for Python.
- [uv](https://github.com/astral-sh/uv) — An extremely fast Python version, package and project manager, written in Rust.
- [poetry](https://github.com/python-poetry/poetry) — Python dependency management and packaging made easy.
- [hatch](https://github.com/pypa/hatch) — Modern, extensible Python project manager for environments, builds, and publishing.
- [pipx](https://github.com/pypa/pipx) — Install and Run Python Applications in Isolated Environments. Like `npx` in Node.js.
- [conda](https://github.com/conda/conda/) — Cross-platform, Python-agnostic binary package manager.

**Build Backends**

- [setuptools](https://github.com/pypa/setuptools) — The historical and still most widely used pyproject build backend.
- [hatchling](https://github.com/pypa/hatch) — Modern, extensible build backend from the hatch project.
- [uv-build](https://github.com/astral-sh/uv) — uv's fast, minimal build backend for pure-Python projects.

## Package Repositories

Local PyPI repository server and proxies.

- [bandersnatch](https://github.com/pypa/bandersnatch/) — PyPI mirroring tool provided by Python Packaging Authority (PyPA).
- [devpi](https://github.com/devpi/devpi) — PyPI server and packaging/testing/release tool.
- [warehouse](https://github.com/pypi/warehouse) — Next generation Python Package Repository (PyPI).

## Distribution

Libraries to create packaged executables for release distribution.

**Executables**

- [pyinstaller](https://github.com/pyinstaller/pyinstaller) — Converts Python programs into stand-alone executables (cross-platform).
- [Nuitka](https://github.com/Nuitka/Nuitka) — Compiles Python programs into high-performance standalone executables (cross-platform, supports all Python versions).
- [shiv](https://github.com/linkedin/shiv) — A command line utility for building fully self-contained zipapps (PEP 441), but with all their dependencies included.
- [cx-Freeze](https://github.com/marcelotduarte/cx_Freeze) — It is a Python tool that converts Python scripts into standalone executables and installers for Windows, macOS, and Linux.

**Obfuscation**

- [pyarmor](https://github.com/dashingsoft/pyarmor) — A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.

## Configuration Files

Libraries for storing and parsing configuration options.

- [configparser](https://docs.python.org/3/library/configparser.html) — (Python standard library) INI file parser.
- [python-dotenv](https://github.com/theskumar/python-dotenv) — Reads key-value pairs from a `.env` file and sets them as environment variables.
- [pydantic-settings](https://github.com/pydantic/pydantic-settings) — Settings management using Pydantic models with validation, loading from environment variables and secrets files.
- [hydra-core](https://github.com/facebookresearch/hydra) — Hydra is a framework for elegantly configuring complex applications.
- [dynaconf](https://github.com/dynaconf/dynaconf) — Dynaconf is a configuration manager with plugins for Django, Flask and FastAPI.
