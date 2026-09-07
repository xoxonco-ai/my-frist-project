# Database & Storage

Categories: ORM, Database Drivers, Database, Caching, Search, Serialization

## ORM

Libraries that implement Object-Relational Mapping or data mapping techniques.

**Relational Databases**

- [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) — The Python SQL Toolkit and Object Relational Mapper.
  - Also see: [awesome-sqlalchemy](https://github.com/dahlia/awesome-sqlalchemy)
- [django.db.models](https://github.com/django/django) — (part of Django) The Django [ORM](https://docs.djangoproject.com/en/dev/topics/db/models/).
- [peewee](https://github.com/coleifer/peewee) — A small, expressive ORM.
- [sqlmodel](https://github.com/fastapi/sqlmodel) — SQLModel is based on Python type annotations, and powered by Pydantic and SQLAlchemy.

**NoSQL Databases**

- [pynamodb](https://github.com/pynamodb/PynamoDB) — A Pythonic interface for [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).
- [mongoengine](https://github.com/MongoEngine/mongoengine) — A Python Object-Document-Mapper for working with MongoDB.
- [beanie](https://github.com/BeanieODM/beanie) — An asynchronous Python object-document mapper (ODM) for MongoDB.

## Database Drivers

Libraries for connecting and operating databases.

**MySQL**

- [pymysql](https://github.com/PyMySQL/PyMySQL) — A pure Python MySQL driver compatible to mysql-python.
- [mysqlclient](https://github.com/PyMySQL/mysqlclient) — MySQL connector with Python 3 support ([mysql-python](https://sourceforge.net/projects/mysql-python/) fork).

**PostgreSQL**

- [psycopg](https://github.com/psycopg/psycopg) — The most popular PostgreSQL adapter for Python.
- [asyncpg](https://github.com/MagicStack/asyncpg) — A fast PostgreSQL Database Client Library for Python/asyncio.

**SQLite**

- [sqlite3](https://docs.python.org/3/library/sqlite3.html) — (Python standard library) SQLite interface compliant with DB-API 2.0.
- [sqlite-utils](https://github.com/simonw/sqlite-utils) — Python CLI utility and library for manipulating SQLite databases.

**ClickHouse**

- [clickhouse-connect](https://github.com/ClickHouse/clickhouse-connect) — The official ClickHouse client, with SQLAlchemy and Superset connectors.
- [clickhouse-driver](https://github.com/mymarilyn/clickhouse-driver) — Python driver with native interface for ClickHouse.

**Other Relational Databases**

- [pyodbc](https://github.com/mkleehammer/pyodbc) — An ODBC bridge for connecting to SQL Server and any other ODBC-accessible database.
- [oracledb](https://github.com/oracle/python-oracledb) — The official Python driver for Oracle Database, successor to cx_Oracle.
- [mssql-python](https://github.com/microsoft/mssql-python) — Official Microsoft driver for SQL Server and Azure SQL, built on ODBC for high performance and low memory usage.

**NoSQL Databases**

- [redis](https://github.com/redis/redis-py) — The Python client for Redis.
- [pymongo](https://github.com/mongodb/mongo-python-driver) — The official Python client for MongoDB.
- [cassandra-driver](https://github.com/apache/cassandra-python-driver) — The Python Driver for Apache Cassandra.
- [django-mongodb-backend](https://github.com/mongodb/django-mongodb-backend) — Official MongoDB database backend for Django.

## Database

In-process databases usable directly from Python.

**Analytical**

- [duckdb](https://github.com/duckdb/duckdb) — An in-process SQL OLAP database management system; optimized for analytics and fast queries, similar to SQLite but for analytical workloads.
- [chdb](https://github.com/chdb-io/chdb) — In-process OLAP SQL engine with the full ClickHouse dialect, zero-copy pandas/Arrow interop, and federation to remote ClickHouse clusters via `remoteSecure()`.

**Vector**

- [chromadb](https://github.com/chroma-core/chroma) — An open-source embedding database for building AI applications with embeddings and semantic search.
- [lancedb](https://github.com/lancedb/lancedb) — A developer-friendly embedded retrieval database for multimodal AI.
- [zvec](https://github.com/alibaba/zvec) — An embedded vector database for on-device RAG and edge AI, the SQLite of vector databases.

**Key-Value & Document**

- [tinydb](https://github.com/msiemens/tinydb) — A tiny, document-oriented database.

## Caching

Libraries for caching data.

- [cachetools](https://github.com/tkem/cachetools) — Extensible memoizing collections and decorators.
- [diskcache](https://github.com/grantjenks/python-diskcache) — SQLite and file backed cache backend with faster lookups than memcached and redis.
- [hishel](https://github.com/karpetrosyan/hishel) — RFC 9111 compliant HTTP caching for httpx and requests, with sync and async support.
- [dogpile.cache](https://github.com/sqlalchemy/dogpile.cache) — dogpile.cache is a next generation replacement for Beaker made by the same authors.
- [django-cacheops](https://github.com/Suor/django-cacheops) — A slick ORM cache with automatic granular event-driven invalidation.

## Search

Libraries and software for indexing and performing search queries on data.

- [elasticsearch](https://github.com/elastic/elasticsearch-py) — The official low-level Python client for [Elasticsearch](https://www.elastic.co/products/elasticsearch).
- [opensearch-py](https://github.com/opensearch-project/opensearch-py) — The official low-level Python client for [OpenSearch](https://opensearch.org/).
- [meilisearch](https://github.com/meilisearch/meilisearch-python) — The official Python client for the [Meilisearch](https://www.meilisearch.com/) search engine.
- [django-haystack](https://github.com/django-haystack/django-haystack) — Modular search for Django.

## Serialization

Libraries for serializing complex data types.

- [msgpack](https://github.com/msgpack/msgpack-python) — MessagePack serializer implementation for Python.
- [orjson](https://github.com/ijl/orjson) — Fast, correct JSON library.
- [marshmallow](https://github.com/marshmallow-code/marshmallow) — A lightweight library for converting complex objects to and from simple Python datatypes.
- [msgspec](https://github.com/msgspec/msgspec) — A fast serialization and validation library with built-in support for JSON, MessagePack, YAML, and TOML.
