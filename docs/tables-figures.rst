=================
Tables & Figures
=================

This page demonstrates tables, figures, images, and related directives.


Simple Table
------------

==========  ==========  ============
Backend     Status      Since
==========  ==========  ============
H2          Stable      v1.0
PostgreSQL  Stable      v2.0
Oracle      Stable      v3.1
MySQL       Beta        v3.2
SQLite      Planned     —
==========  ==========  ============


Grid Table
----------

+------------------------+------------+----------+----------+
| Feature                | Community  | Pro      | Enterprise|
+========================+============+==========+==========+
| Query engine           | ✓          | ✓        | ✓        |
+------------------------+------------+----------+----------+
| Connection pooling     | 10 max     | 100 max  | Unlimited|
+------------------------+------------+----------+----------+
| Async I/O              | —          | ✓        | ✓        |
+------------------------+------------+----------+----------+
| Cluster management     | —          | —        | ✓        |
+------------------------+------------+----------+----------+
| 24/7 Support           | —          | —        | ✓        |
+------------------------+------------+----------+----------+


List Table
----------

.. list-table:: Configuration Options
   :header-rows: 1
   :widths: 20 15 65

   * - Option
     - Default
     - Description
   * - ``color_primary``
     - ``#1e3a5f``
     - Primary brand colour used for sidebar accents and heading emphasis.
   * - ``color_accent``
     - ``#0077b6``
     - Accent colour for links, buttons, and interactive elements.
   * - ``navigation_depth``
     - ``4``
     - Maximum depth of the sidebar navigation tree.
   * - ``show_breadcrumbs``
     - ``True``
     - Show breadcrumb trail above content area.
   * - ``content_max_width``
     - ``52rem``
     - Maximum width of the main content column.


CSV Table
---------

.. csv-table:: Performance Benchmarks
   :header: "Operation", "H2 (ms)", "PostgreSQL (ms)", "Oracle (ms)"
   :widths: 30, 20, 25, 25

   "Single read", "0.3", "1.2", "1.8"
   "Bulk insert (1K rows)", "45", "62", "58"
   "Full scan (100K rows)", "180", "95", "110"
   "Index lookup", "0.1", "0.8", "0.9"
   "Join (3 tables)", "12", "8", "9"


Field Lists
-----------

:Platform:    Linux, macOS, Windows
:Language:    Python 3.9+
:License:     MIT
:Repository:  https://github.com/acme/platform
:Build:       |release|


Option Lists
------------

-o             Output file path
-v, --verbose  Enable verbose logging
-q, --quiet    Suppress non-error output
--format=FMT   Output format: ``json``, ``csv``, or ``table``
--dry-run      Show planned actions without executing


Math
----

The query cost model uses:

.. math::

   C(q) = \alpha \cdot |R| + \beta \cdot \log_2(|I|) + \gamma \cdot |J|

where :math:`|R|` is the result set size, :math:`|I|` is the index cardinality,
and :math:`|J|` is the join width.

For multi-node queries, total cost is:

.. math::

   C_{\text{total}} = \sum_{i=1}^{N} C_i(q) + \delta \cdot N \cdot \text{latency}


Figures
-------

.. figure:: https://via.placeholder.com/600x200/1e3a5f/ffffff?text=Architecture+Diagram
   :alt: Platform architecture diagram
   :align: center
   :width: 80%

   *Fig. 1:* High-level architecture of the Acme Platform, showing the
   query engine, storage layer, and cluster management components.
