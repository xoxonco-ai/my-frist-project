# Python Language

Categories: Implementations, Built-in Classes Enhancement, Functional Programming, Asynchronous Programming, Date and Time

## Implementations

Implementations of Python.

- [cpython](https://github.com/python/cpython) — Default, most widely used implementation of the Python programming language written in C.
- [micropython](https://github.com/micropython/micropython) — A lean and efficient Python programming language implementation.
- [pypy](https://github.com/pypy/pypy) — A very fast and compliant implementation of the Python language.
- [Cython](https://github.com/cython/cython) — Optimizing Static Compiler for Python.
- [pyodide](https://github.com/pyodide/pyodide) — Python distribution for the browser and Node.js based on WebAssembly.

## Built-in Classes Enhancement

Libraries for enhancing Python built-in classes.

- [attrs](https://github.com/python-attrs/attrs) — Replacement for `__init__`, `__eq__`, `__repr__`, etc. boilerplate in class definitions.
- [bidict](https://github.com/jab/bidict) — Efficient, Pythonic bidirectional map data structures and related functionality.
- [uuid-utils](https://github.com/aminalaee/uuid-utils) — A fast, Rust-backed drop-in replacement for Python's built-in `uuid` module, supporting RFC 9562 (UUIDv6, UUIDv7, and UUIDv8).
- [python-box](https://github.com/cdgriffith/Box) — Python dictionaries with advanced dot notation access.

## Functional Programming

Functional Programming with Python.

- [functools](https://docs.python.org/3/library/functools.html) — (Python standard library) Higher-order functions and operations on callable objects.
- [more-itertools](https://github.com/more-itertools/more-itertools) — More routines for operating on iterables, beyond `itertools`.
- [toolz](https://github.com/pytoolz/toolz) — A collection of functional utilities for iterators, functions, and dictionaries. Also available as [cytoolz](https://github.com/pytoolz/cytoolz/) for Cython-accelerated performance.
- [funcy](https://github.com/Suor/funcy) — A fancy and practical functional tools.
- [returns](https://github.com/dry-python/returns) — A set of type-safe monads, transformers, and composition utilities.

## Asynchronous Programming

Libraries for asynchronous, concurrent and parallel execution. Also see [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio).

**Async I/O**

- [asyncio](https://docs.python.org/3/library/asyncio.html) — (Python standard library) Asynchronous I/O, event loop, coroutines and tasks.
  - Also see: [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio)
- [anyio](https://github.com/agronholm/anyio) — A high-level async concurrency and networking framework that works on top of asyncio or trio.
- [uvloop](https://github.com/MagicStack/uvloop) — Ultra fast asyncio event loop.
- [trio](https://github.com/python-trio/trio) — A friendly library for async concurrency and I/O.
- [gevent](https://github.com/gevent/gevent) — A coroutine-based Python networking library that uses [greenlet](https://github.com/python-greenlet/greenlet).
- [Twisted](https://github.com/twisted/twisted) — An event-driven networking engine.

**Parallelism**

- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) — (Python standard library) A high-level interface for asynchronously executing callables.
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) — (Python standard library) Process-based parallelism.

## Date and Time

Libraries for working with dates and times.

- [zoneinfo](https://docs.python.org/3/library/zoneinfo.html) — (Python standard library) IANA time zone support. Brings the [tz database](https://en.wikipedia.org/wiki/Tz_database) into Python.
- [python-dateutil](https://github.com/dateutil/dateutil) — Extensions to the standard Python [datetime](https://docs.python.org/3/library/datetime.html) module.
- [dateparser](https://github.com/scrapinghub/dateparser) — A Python parser for human-readable dates in dozens of languages.
- [pendulum](https://github.com/python-pendulum/pendulum) — Python datetimes made easy.
- [whenever](https://github.com/ariebovenberg/whenever) — A modern datetime library, type-safe and DST-safe, backed by Rust.
