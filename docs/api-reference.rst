==============
API Reference
==============

This page exercises Sphinx's Python domain — classes, methods, functions,
exceptions, attributes, and data objects.


Core Classes
------------

.. py:class:: Platform(config: Config)

   The main entry point for connecting to an Acme cluster.

   :param config: A :class:`Config` instance with connection details.

   .. py:method:: connect(config: Config) -> Platform
      :classmethod:

      Create and return a connected :class:`Platform` instance.

      :param config: Configuration object.
      :returns: A connected platform instance.
      :raises ConnectionError: If the cluster is unreachable.

   .. py:method:: query(sql: str, params: dict = None) -> ResultSet

      Execute a SQL query against the cluster.

      :param sql: SQL query string.
      :param params: Optional bind parameters.
      :returns: A :class:`ResultSet` with query results.

      **Example:**

      .. code-block:: python

         result = platform.query(
             "SELECT * FROM events WHERE type = :type",
             params={"type": "login"},
         )

   .. py:method:: query_async(sql: str, params: dict = None) -> AsyncResultSet
      :async:

      Asynchronous variant of :meth:`query`.

      .. versionadded:: 3.2

   .. py:method:: cluster_info() -> ClusterInfo

      Retrieve metadata about the connected cluster.

   .. py:method:: close() -> None

      Gracefully disconnect from the cluster.

      .. deprecated:: 3.1
         Use the context manager protocol (``with`` statement) instead.

   .. py:method:: __enter__() -> Platform

      Enter the context manager.

   .. py:method:: __exit__(exc_type, exc_val, exc_tb) -> None

      Exit the context manager, closing the connection.


.. py:class:: Config

   Immutable configuration for a platform connection.

   .. py:classmethod:: from_file(path: str) -> Config

      Load configuration from a YAML file.

   .. py:classmethod:: from_env() -> Config

      Build configuration from environment variables:

      - :envvar:`ACME_CLUSTER_URL` — cluster address
      - :envvar:`ACME_STORAGE_BACKEND` — ``h2``, ``postgres``, or ``oracle``
      - :envvar:`ACME_API_KEY` — authentication key

      .. versionadded:: 3.2

   .. py:attribute:: cluster_name
      :type: str

      The name of the target cluster.

   .. py:attribute:: nodes
      :type: list[NodeAddress]

      List of cluster node addresses.


.. py:class:: ResultSet

   Iterable query result.

   .. py:method:: __iter__() -> Iterator[Row]

      Iterate over result rows.

   .. py:method:: fetchone() -> Row | None

      Fetch the next row, or ``None`` if exhausted.

   .. py:method:: fetchall() -> list[Row]

      Fetch all remaining rows into a list.

      .. warning::

         This loads all rows into memory. For large result sets,
         prefer iterating row by row.

   .. py:attribute:: column_names
      :type: tuple[str, ...]

      Column names from the query.

   .. py:attribute:: row_count
      :type: int

      Total number of rows.


Exceptions
----------

.. py:exception:: ConnectionError

   Raised when a connection cannot be established.

.. py:exception:: QueryError(message: str, sql: str)

   Raised when a query fails.

   .. py:attribute:: sql
      :type: str

      The SQL string that caused the error.

.. py:exception:: TimeoutError(timeout: float)

   Raised when an operation exceeds the configured timeout.


Functions
---------

.. py:function:: connect(url: str, **kwargs) -> Platform

   Shorthand for creating a :class:`Config` and :class:`Platform` in one step.

   :param url: Connection URL (e.g. ``acme://host:port``).
   :param kwargs: Additional configuration overrides.
   :returns: A connected :class:`Platform`.
   :raises ValueError: If the URL format is invalid.

   .. code-block:: python

      from acme import connect

      with connect("acme://cluster.local:9090") as p:
          print(p.cluster_info())


Type Aliases
------------

.. py:data:: NodeAddress
   :type: tuple[str, int]

   A ``(host, port)`` pair identifying a cluster node.

.. py:data:: Row
   :type: dict[str, Any]

   A single result row as an ordered dictionary.


Constants
---------

.. py:data:: DEFAULT_PORT
   :value: 9090

   Default port for cluster connections.

.. py:data:: MAX_RETRIES
   :value: 3

   Maximum number of connection retry attempts.

.. py:data:: VERSION
   :value: "3.2.1"

   Current library version string.


Glossary
--------

.. glossary::

   Cluster
      A group of interconnected nodes that process queries cooperatively.

   Node
      A single server instance within a :term:`cluster`.

   ResultSet
      An iterable object returned by :meth:`Platform.query` containing
      rows of query results.

   Storage Backend
      The database engine used for persistent data (H2, PostgreSQL, Oracle).
