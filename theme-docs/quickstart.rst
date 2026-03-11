===========
Quick Start
===========

Five minutes to a working documentation site.


1. Install
----------

.. code-block:: bash

   cd manticore-sphinx-theme
   pip install -e .


2. Configure
------------

In your project's ``conf.py``:

.. code-block:: python

   html_theme = "manticore_sphinx_theme"

   html_theme_options = {
       "logo": "mylogo.png",          # in _static/
       "logo_alt": "My Project",
       "favicon": "favicon.ico",      # in _static/
       "color_primary": "#030146",    # navy — headings, TOC links
       "color_accent": "#ff420e",     # orange — links, active states
       "landing_page": "index",       # landing page (pagename)
       "repo_url": "https://github.com/myorg/myproject",
   }

   # Landing page navigation cards
   html_context = {
       "landing_page": {
           "menu": [
               {"title": "Getting Started", "url": "getting-started"},
               {"title": "API Reference", "url": "api-reference"},
           ]
       }
   }

   html_show_sphinx = False           # suppress "Created using Sphinx"


3. Build
--------

.. code-block:: bash

   python build.py clean css docs
   # or: make clean css docs

Open ``_build/html/index.html``.


4. Live-Reload
--------------

.. code-block:: bash

   python build.py docs-live
   # or: make docs-live

Starts a server at http://localhost:8080 with automatic refresh.


Minimal conf.py
----------------

.. code-block:: python

   import os

   project = "My Project"
   copyright = "2026, My Company"
   version = "1.0"

   html_theme = "manticore_sphinx_theme"
   html_theme_path = [os.path.abspath("..")]

   html_theme_options = {
       "logo_alt": "My Project",
       "color_primary": "#030146",
       "color_accent": "#ff420e",
   }

   html_show_sphinx = False
   html_static_path = ["_static"]
