=========
Changelog
=========

3.2.1 — 2026-03-01
-------------------

**Bug Fixes**

- Fixed connection timeout handling in async mode.
- Improved error messages for malformed SQL queries.
- Corrected ``ResultSet.row_count`` for empty result sets.

**Documentation**

- Switched to Manticore Sphinx Theme for documentation.
- Added comprehensive Sphinx feature showcase pages.


3.2.0 — 2026-01-15
-------------------

**New Features**

- Added :meth:`Config.from_env() <Config.from_env>` for environment-based configuration.
- Added :meth:`Platform.query_async` for async query execution.
- Support for prepared statements with parameter binding.

**Deprecations**

- :meth:`Platform.close` is deprecated; use the context manager protocol instead.


3.1.0 — 2025-09-01
-------------------

**New Features**

- Initial support for Oracle storage backend.
- Added cluster health monitoring endpoint at ``/health``.
- ``ResultSet`` now supports ``async for`` iteration.

**Performance**

- 40% improvement in bulk insert throughput for H2 backend.
- Reduced memory usage for large result sets via streaming.

**Bug Fixes**

- Fixed race condition in connection pool under high concurrency.
- Corrected timezone handling for ``TIMESTAMP WITH TIME ZONE`` columns.


3.0.0 — 2025-04-01
-------------------

**Breaking Changes**

- Minimum Python version raised to 3.9.
- Removed legacy ``Connection`` class; use :class:`Platform` instead.
- Configuration format changed from INI to YAML.

**New Features**

- Complete rewrite of the query engine for better performance.
- Added PostgreSQL as a first-class storage backend.
- New ``acme-cli`` command-line tool for administration.
