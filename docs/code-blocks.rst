===========
Code Blocks
===========

This page demonstrates code highlighting, line numbers, captions,
and other code-related Sphinx features.


Basic Code Block
----------------

.. code-block:: python

   def fibonacci(n):
       """Return the nth Fibonacci number."""
       a, b = 0, 1
       for _ in range(n):
           a, b = b, a + b
       return a


Multiple Languages
------------------

**Java:**

.. code-block:: java

   public class Platform implements AutoCloseable {
       private final ClusterClient client;

       public Platform(Config config) {
           this.client = new ClusterClient(config);
       }

       public ResultSet query(String sql) {
           return client.execute(sql);
       }

       @Override
       public void close() {
           client.disconnect();
       }
   }

**SQL:**

.. code-block:: sql

   SELECT
       e.event_type,
       COUNT(*) AS event_count,
       AVG(e.duration_ms) AS avg_duration
   FROM events e
   JOIN sessions s ON e.session_id = s.id
   WHERE e.created_at > NOW() - INTERVAL '1 hour'
   GROUP BY e.event_type
   ORDER BY event_count DESC
   LIMIT 10;

**Bash:**

.. code-block:: bash

   #!/bin/bash
   set -euo pipefail

   # Deploy to production cluster
   for node in node{1..5}.acme.local; do
       echo "Deploying to $node..."
       ssh "$node" "sudo systemctl restart acme-platform"
       sleep 10  # wait for health check
       curl -sf "http://$node:9090/health" || exit 1
   done
   echo "Deployment complete."

**YAML:**

.. code-block:: yaml

   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: acme-platform
     labels:
       app: acme
       tier: backend
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: acme


Line Numbers
------------

.. code-block:: python
   :linenos:

   import asyncio
   from acme import Platform, Config

   async def main():
       config = Config.from_env()
       async with Platform.connect(config) as p:
           result = await p.query_async(
               "SELECT * FROM events WHERE type = :type",
               params={"type": "login"},
           )
           async for row in result:
               print(row)

   asyncio.run(main())


Emphasised Lines
----------------

.. code-block:: python
   :linenos:
   :emphasize-lines: 3,7-9

   from acme import Platform

   # This line is emphasised
   config = Config.from_file("config.yaml")

   with Platform.connect(config) as p:
       # These three lines are emphasised
       result = p.query("SELECT count(*) FROM events")
       count = result.fetchone()["count"]
       print(f"Total events: {count}")


Caption and Name
----------------

.. code-block:: python
   :caption: platform_client.py — Main client module
   :name: platform-client-example

   class PlatformClient:
       """High-level client with connection pooling."""

       def __init__(self, config, pool_size=10):
           self.config = config
           self.pool = ConnectionPool(config, size=pool_size)

       def execute(self, sql, params=None):
           conn = self.pool.acquire()
           try:
               return conn.execute(sql, params)
           finally:
               self.pool.release(conn)

You can reference this code block by name: :ref:`platform-client-example`.


Inline Code
-----------

Use :func:`platform.query` to run SQL queries. The method accepts a
:class:`str` query and optional :class:`dict` parameters. The return type
is :class:`ResultSet`.

For configuration, set the :envvar:`ACME_CLUSTER_URL` environment variable
to point to your cluster. The default port is ``9090``.


Literal Include
---------------

Literal blocks can be created with double colons::

   This is a literal block.
   It preserves    spacing    and
       indentation exactly.

   No syntax highlighting is applied.


Parsed Literal
--------------

.. parsed-literal::

   $ acme-cli connect --cluster **production**
   Connected to production (5 nodes)
   Cluster version: |release|
   Ready.


Doctest Blocks
--------------

Doctest-style blocks are recognised automatically:

>>> from acme import Platform
>>> p = Platform.connect("acme://localhost:9090")
>>> p.cluster_info().name
'development'
>>> p.close()
