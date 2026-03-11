==================
Corporate Branding
==================


Sidebar Logo
------------

Place your logo in ``_static/`` and reference it:

.. code-block:: python

   html_theme_options = {
       "logo": "mylogo.png",      # relative to _static/
       "logo_alt": "My Company",
   }

The logo renders at **3.5 rem height** (~56 px) in the sidebar, centred
above the project name.  On mobile, it scales to 2 rem.  SVG is
preferred for crisp rendering.


Default Corporate Icon
^^^^^^^^^^^^^^^^^^^^^^

When no ``logo`` is set, the theme displays a built-in SVG monitor icon
in the accent colour.  To replace it, edit the ``<svg>`` block in
``layout.html`` marked "Default corporate icon".


Browser Favicon
---------------

.. code-block:: python

   html_theme_options = {
       "favicon": "favicon.ico",
   }

Supports ``.png``, ``.ico``, and ``.svg``.


Project Name & Version
-----------------------

.. code-block:: python

   project = "My Platform"
   version = "3.2"

The version appears as a navy pill badge below the project title.
Set ``version = ""`` to hide it.


Repository Link
---------------

.. code-block:: python

   html_theme_options = {
       "repo_url": "https://github.com/myorg/myproject",
       "repo_name": "GitHub",
   }

Shows a GitHub icon + label in the header bar.  Set ``repo_url`` to
empty to hide it.  For GitLab, replace the SVG in ``layout.html``.


Complete Branding Example
--------------------------

.. code-block:: python

   project = "Acme Platform"
   version = "3.2"
   copyright = "2026, Acme Corp"

   html_theme = "manticore_sphinx_theme"

   html_theme_options = {
       "logo": "acme-logo.svg",
       "logo_alt": "Acme Platform",
       "favicon": "acme-favicon.png",
       "color_primary": "#030146",
       "color_accent": "#ff420e",
       "navigation_depth": 3,
       "show_breadcrumbs": True,
       "footer_text": "© 2026 Acme Corp.",
       "show_powered_by": False,
       "landing_page": "index",
       "repo_url": "https://github.com/acme/platform",
       "repo_name": "GitHub",
   }

   html_show_sphinx = False
