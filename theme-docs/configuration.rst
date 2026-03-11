=============
Configuration
=============

All settings live in ``html_theme_options`` in ``conf.py``.
Every option has a sensible default.

.. code-block:: python

   html_theme_options = {
       # Branding
       "logo": "mylogo.png",
       "logo_alt": "My Project",
       "favicon": "favicon.ico",

       # Colours
       "color_primary": "#030146",
       "color_accent": "#ff420e",
       "color_sidebar_bg": "#f5f6fa",
       "color_sidebar_text": "#2d2d48",

       # Navigation
       "navigation_depth": 4,
       "collapse_navigation": False,
       "show_breadcrumbs": True,

       # Footer
       "footer_text": "© 2026 My Company",
       "show_powered_by": True,

       # Content
       "content_max_width": "52rem",

       # Landing page
       "landing_page": "index",

       # Repository
       "repo_url": "https://github.com/myorg/myproject",
       "repo_name": "GitHub",
   }


Colour Roles
------------

``color_primary`` (default ``#030146``)
   Deep navy. Used for headings (h1–h6), sidebar TOC active links,
   API object names, on-page TOC active links, version badge, and
   pagination titles.

``color_accent`` (default ``#ff420e``)
   Vibrant orange. Used for unvisited links, the sidebar active border,
   the landing page gradient, the dark mode toggle hover, and the
   TOC toggle hover. Visited links turn grey.


Sphinx-Level Settings
---------------------

``html_show_sphinx = False``
   Suppresses the "Created using Sphinx" footer.

``html_show_copyright = False``
   Hides the copyright line.

``pygments_style = "tango"``
   The default syntax highlighting style (overridable).

For a complete table of every option, see :doc:`options-reference`.


Landing Page Cards
------------------

Landing cards are configured separately in ``html_context`` (not in
``html_theme_options``):

.. code-block:: python

   html_context = {
       "landing_page": {
           "menu": [
               {"title": "IFRS VBox", "url": "VBox/ifrs"},
               {"title": "RISK VBox", "url": "VBox/risk"},
               {"title": "OS Libraries", "url": "tools"},
           ]
       }
   }

See :doc:`landing-page` for full details.
