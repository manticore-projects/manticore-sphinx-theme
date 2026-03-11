============
Build System
============

Two equivalent build systems: ``Makefile`` and ``build.py``.


Tool Detection
--------------

Both auto-detect tools in this priority:

- **Python**: ``.venv/bin/python3`` → ``python3``
- **Sphinx**: ``.venv/bin/sphinx-build`` → ``sphinx-build`` on PATH → ``python3 -m sphinx``
- **Installer**: ``pipx`` (CLI tools) → ``pip`` in ``.venv`` → ``pip3 --break-system-packages``
- **SASS**: ``dart-sass`` binary → Python ``libsass``

Run ``python build.py info`` or ``make info`` to see what's detected.


Command Reference
-----------------

.. list-table::
   :header-rows: 1
   :widths: 22 22 56

   * - Makefile
     - build.py
     - Description
   * - ``make help``
     - ``python build.py help``
     - Show commands
   * - ``make info``
     - ``python build.py info``
     - Show detected tools
   * - ``make env``
     - ``python build.py env``
     - Create ``.venv`` with Sphinx
   * - ``make deps``
     - ``python build.py deps``
     - Install dependencies
   * - ``make css``
     - ``python build.py css``
     - Compile SASS → CSS
   * - ``make css-min``
     - ``python build.py css-min``
     - Minified CSS
   * - ``make css-watch``
     - ``python build.py css-watch``
     - Watch and recompile
   * - ``make docs``
     - ``python build.py docs``
     - Build HTML docs
   * - ``make docs-prod``
     - ``python build.py docs-prod``
     - Build + minify + gzip
   * - ``make docs-live``
     - ``python build.py docs-live``
     - Live-reload server
   * - ``make clean``
     - ``python build.py clean``
     - Remove artifacts

``build.py`` supports chaining: ``python build.py clean css docs``


pipx Integration
----------------

If you use pipx (common on Arch Linux), ``make deps`` / ``build.py deps``
uses ``pipx install`` for CLI tools and ``pip`` for libraries:

.. code-block:: bash

   make deps   # pipx install sphinx; pipx install build; pip install libsass

To install the theme into the pipx-managed Sphinx:

.. code-block:: bash

   pipx inject sphinx /path/to/manticore-sphinx-theme
