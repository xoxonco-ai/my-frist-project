# Web Development

Categories: Web Frameworks, Web APIs, Web Servers, WebSocket, Template Engines, Web Asset Management, Authentication, Admin Panels, CMS, ERP, Static Site Generators

## Web Frameworks

Traditional full stack web frameworks. Also see [Web APIs](#web-apis).

**Synchronous**

- [flask](https://github.com/pallets/flask) — A microframework for Python.
  - Also see: [awesome-flask](https://github.com/humiaozuzu/awesome-flask)
- [django](https://github.com/django/django) — The most popular web framework in Python.
  - Also see: [awesome-django](https://github.com/wsvincent/awesome-django)
- [bottle](https://github.com/bottlepy/bottle) — A fast and simple micro-framework distributed as a single file with no dependencies.
- [pyramid](https://github.com/Pylons/pyramid) — A small, fast, down-to-earth, open source Python web framework.
  - Also see: [awesome-pyramid](https://github.com/uralbash/awesome-pyramid)
- [fasthtml](https://github.com/AnswerDotAI/fasthtml) — The fastest way to create an HTML app.
  - Also see: [awesome-fasthtml](https://github.com/amosgyamfi/awesome-fasthtml)

**Asynchronous**

- [starlette](https://github.com/Kludex/starlette) — A lightweight ASGI framework and toolkit for building high-performance async services.
- [tornado](https://github.com/tornadoweb/tornado) — A web framework and asynchronous networking library.
- [litestar](https://github.com/litestar-org/litestar) — Production-ready, capable and extensible ASGI Web framework.
- [reflex](https://github.com/reflex-dev/reflex) — A framework for building reactive, full-stack web applications entirely with Python.

## Web APIs

Libraries for building RESTful, GraphQL, and RPC APIs.

**Django**

- [django-rest-framework](https://github.com/encode/django-rest-framework) — A powerful and flexible toolkit to build web APIs.
- [django-ninja](https://github.com/vitalik/django-ninja) — Fast, Django REST framework based on type hints and Pydantic.
- [strawberry-django](https://github.com/strawberry-graphql/strawberry-django) — Strawberry GraphQL integration with Django.
- [django-modern-rest](https://github.com/wemake-services/django-modern-rest) — Modern REST with speed, types, async, `msgspec`, `pydantic` and other goodies!

**Flask**

- [apiflask](https://github.com/apiflask/apiflask) — A lightweight Python web API framework based on Flask and Marshmallow.

**Framework Agnostic**

- [fastapi](https://github.com/fastapi/fastapi) — A modern, fast, web framework for building APIs with standard Python type hints.
- [connexion](https://github.com/spec-first/connexion) — A spec-first framework that automatically handles requests based on your OpenAPI specification.
- [strawberry](https://github.com/strawberry-graphql/strawberry) — A GraphQL library that leverages Python type annotations for schema definition.

**RPC**

- [grpcio](https://github.com/grpc/grpc) — HTTP/2-based RPC framework with Python bindings, built by Google.

## Web Servers

ASGI and WSGI compatible web servers.

**ASGI**

- [uvicorn](https://github.com/Kludex/uvicorn) — A lightning-fast ASGI server implementation, using uvloop and httptools.
- [granian](https://github.com/emmett-framework/granian) — A Rust HTTP server for Python applications built on top of Hyper and Tokio, supporting WSGI/ASGI/RSGI.
- [hypercorn](https://github.com/pgjones/hypercorn) — An ASGI and WSGI Server based on Hyper libraries and inspired by Gunicorn.

**WSGI**

- [gunicorn](https://github.com/benoitc/gunicorn) — Pre-forked, ported from Ruby's Unicorn project.
- [waitress](https://github.com/Pylons/waitress) — Multi-threaded, powers Pyramid.

## WebSocket

Libraries for working with WebSocket.

- [websockets](https://github.com/python-websockets/websockets) — A library for building WebSocket servers and clients with a focus on correctness and simplicity.
- [channels](https://github.com/django/channels) — Developer-friendly asynchrony for Django.
- [flask-socketio](https://github.com/miguelgrinberg/Flask-SocketIO) — Socket.IO integration for Flask applications.
- [autobahn-python](https://github.com/crossbario/autobahn-python) — WebSocket & WAMP for Python on Twisted and [asyncio](https://docs.python.org/3/library/asyncio.html).

## Template Engines

Libraries and tools for templating and lexing.

- [jinja](https://github.com/pallets/jinja) — A modern and designer friendly templating language.
- [mako](https://github.com/sqlalchemy/mako) — Hyperfast and lightweight templating for the Python platform.

## Web Asset Management

Tools for managing, storing, compressing and minifying website assets.

- [django-storages](https://github.com/jschneier/django-storages) — A collection of custom storage back ends for Django.
- [django-compressor](https://github.com/django-compressor/django-compressor) — Compresses linked and inline JavaScript or CSS into a single cached file.

## Authentication

Libraries for implementing authentication schemes.

**OAuth**

- [oauthlib](https://github.com/oauthlib/oauthlib) — A generic and thorough implementation of the OAuth request-signing logic.
- [authlib](https://github.com/authlib/authlib) — A comprehensive library for building OAuth, OpenID Connect, and JWT/JWS/JWE/JWK/JWA.
- [django-allauth](https://github.com/pennersr/django-allauth) — Authentication app for Django that "just works."
- [django-oauth-toolkit](https://github.com/django-oauth/django-oauth-toolkit) — OAuth 2 goodies for Django.

**JWT**

- [pyjwt](https://github.com/jpadilla/pyjwt) — JSON Web Token implementation in Python.

**Permissions**

- [django-guardian](https://github.com/django-guardian/django-guardian) — Implementation of per-object permissions for Django.
- [django-rules](https://github.com/dfunckt/django-rules) — A tiny but powerful app providing object-level permissions to Django, without requiring a database.

## Admin Panels

Libraries for administrative interfaces.

- [flask-admin](https://github.com/pallets-eco/flask-admin) — Simple and extensible administrative interface framework for Flask.
- [django-unfold](https://github.com/unfoldadmin/django-unfold) — Elevate your Django admin with a stunning modern interface, powerful features, and seamless user experience.
- [django-grappelli](https://github.com/sehmaschine/django-grappelli) — A jazzy skin for the Django Admin-Interface.

## CMS

Content Management Systems.

- [wagtail](https://github.com/wagtail/wagtail) — A Django content management system.
- [django-cms](https://github.com/django-cms/django-cms) — The easy-to-use and developer-friendly enterprise CMS powered by Django.

## ERP

Enterprise resource planning frameworks.

- [odoo](https://github.com/odoo/odoo) — A suite of open source business apps: CRM, e-commerce, accounting, inventory, and thousands of community modules.

## Static Site Generators

Static site generator is a software that takes some text + templates as input and produces HTML files on the output.

- [pelican](https://github.com/getpelican/pelican) — Static site generator that supports Markdown and reST syntax.
- [nikola](https://github.com/getnikola/nikola) — A static website and blog generator.
