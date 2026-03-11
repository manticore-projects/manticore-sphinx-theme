============
Installation
============

Three ways to make the theme available to Sphinx.


Option A — pip install (recommended)
--------------------------------------

.. code-block:: bash

   cd manticore-sphinx-theme
   pip install -e .

Or with pipx-managed Sphinx:

.. code-block:: bash

   pipx inject sphinx /path/to/manticore-sphinx-theme

Then in ``conf.py``:

.. code-block:: python

   html_theme = "manticore_sphinx_theme"

The ``-e`` (editable) flag means CSS and template changes take effect
immediately without reinstalling.


Option B — Copy the theme directory
--------------------------------------

Copy ``manticore_sphinx_theme/`` into your project:

.. code-block:: text

   your-project/
   ├── docs/
   │   ├── conf.py
   │   └── index.rst
   └── manticore_sphinx_theme/
       ├── theme.toml
       ├── layout.html
       └── static/
           ├── css/theme.css
           └── js/theme.js

Then in ``conf.py``:

.. code-block:: python

   import os
   html_theme = "manticore_sphinx_theme"
   html_theme_path = [os.path.abspath("..")]


Option C — Reference by path
--------------------------------------

.. code-block:: python

   html_theme = "manticore_sphinx_theme"
   html_theme_path = ["/home/you/projects/manticore-sphinx-theme"]


Runtime Files
-------------

Only these files are needed at runtime:

.. code-block:: text

   manticore_sphinx_theme/
   ├── theme.toml       # Sphinx ≥ 7.3
   ├── theme.conf       # Sphinx < 7.3
   ├── layout.html      # Jinja2 master template
   └── static/
       ├── css/theme.css # compiled stylesheet
       └── js/theme.js   # sidebar, TOC, dark mode, filter

The ``static/sass/`` directory is only needed for recompilation.


Prerequisites
-------------

- Python 3.9+
- Sphinx 7.0+ (tested through 9.2)
- For CSS compilation: dart-sass (recommended) or Python libsass
- No NPM, Node.js, or webpack
