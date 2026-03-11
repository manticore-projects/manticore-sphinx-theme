============
Optimization
============

The ``optimize.py`` script runs after ``sphinx-build`` to minify and
compress the output for production deployment.


Usage
-----

.. code-block:: bash

   python build.py docs-prod     # build + optimize in one step
   # or:
   make docs-prod

   # standalone:
   python optimize.py _build/html


What It Does
------------

1. **Minifies HTML** — removes comments, collapses whitespace (preserves
   ``<pre>`` contents).  Uses ``htmlmin`` if installed, otherwise a
   built-in regex processor.

2. **Minifies CSS** — strips comments and whitespace.  Uses ``rcssmin``
   if installed, otherwise built-in.

3. **Minifies JS** — removes single-line comments, collapses blank lines.

4. **Pre-compresses to .gz** — creates gzipped copies at level 9 for
   ``nginx gzip_static`` or similar CDN features.

5. **Reports savings** — total bytes saved across all files.


Example Output
--------------

.. code-block:: text

   ● Optimizing _build/html/…

     Minified:   42 files
                 385,200 → 298,400 bytes (22.5% reduction)
     Gzipped:    56 files (87,300 bytes saved)
     Total saved: 174,100 bytes

   ✓  Optimization complete


Pre-compiled CSS
----------------

The theme can ship with a pre-compiled ``theme.css``.  If you don't
modify SASS, you can skip ``make css`` and deploy using the shipped
CSS.  This means CI only needs Sphinx — no dart-sass required.

.. tip::

   After modifying SASS, commit the updated ``theme.css`` so CI and
   other developers don't need SASS tooling.
