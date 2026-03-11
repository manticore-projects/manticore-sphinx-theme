===============
Getting Started
===============

This page demonstrates basic prose, lists, links, and block-level elements.


Installation
------------

Install via pip:

.. code-block:: bash

   pip install acme-platform

Or install from source:

.. code-block:: bash

   git clone https://github.com/acme/platform.git
   cd platform
   pip install -e ".[dev]"


Requirements
^^^^^^^^^^^^

The platform requires:

1. Python 3.9 or later
2. A running database (H2, PostgreSQL, or Oracle)
3. Network access to cluster nodes

For PostgreSQL backends, you also need ``libpq-dev`` installed.


Configuration
-------------

Create ``~/.acme/config.yaml``:

.. code-block:: yaml

   cluster:
     name: production
     nodes:
       - host: node1.acme.local
         port: 9090
       - host: node2.acme.local
         port: 9090

   storage:
     backend: postgres
     connection_string: postgresql://acme:secret@db.local/platform

.. warning::

   Never commit credentials directly into configuration files.
   Use environment variables or a secrets manager in production.


Quick Example
-------------

.. code-block:: python

   from acme import Platform, Config

   config = Config.from_file("~/.acme/config.yaml")

   with Platform.connect(config) as p:
       info = p.cluster_info()
       print(f"Connected to {info.name} ({info.node_count} nodes)")

       for row in p.query("SELECT * FROM events LIMIT 5"):
           print(row)


Definition Lists
^^^^^^^^^^^^^^^^

Platform
   The main entry point for cluster operations.

Config
   Immutable configuration object, loaded from YAML or environment.

ResultSet
   Iterable query result with column metadata and row access.


Nested Lists
^^^^^^^^^^^^

- **Compute layer**

  - Query planning and optimisation
  - Parallel execution engine
  - Result caching

- **Storage layer**

  - Page-level management
  - Write-ahead logging
  - Compaction and garbage collection

    - Minor compaction (within a level)
    - Major compaction (across levels)


Links and Cross-References
--------------------------

- External link: `Sphinx Documentation <https://www.sphinx-doc.org/>`_
- Internal cross-reference: :doc:`api-reference`
- Section reference: :ref:`search`
- Python reference: :class:`python:str`


Block Quotes
------------

As the original architect once wrote:

    The best documentation is the documentation that gets read.
    Make it scannable, make it searchable, make it beautiful.

    — Internal memo, 2024


Horizontal Rule
---------------

----

Content continues after the rule.


Next Steps
----------

- :doc:`typography` — Heading hierarchy and inline markup
- :doc:`admonitions` — Notes, warnings, tips
- :doc:`code-blocks` — Code highlighting and line numbers
