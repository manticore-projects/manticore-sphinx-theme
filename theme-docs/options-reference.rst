=================
Options Reference
=================

Every ``html_theme_options`` key with type, default, and description.


Branding
--------

.. list-table::
   :header-rows: 1
   :widths: 20 12 15 53

   * - Option
     - Type
     - Default
     - Description
   * - ``logo``
     - string
     - ``""``
     - Logo image path relative to ``_static/``.  When empty, a
       built-in SVG icon is shown.  Renders at 3.5rem height.
   * - ``logo_alt``
     - string
     - ``"Documentation"``
     - Alt text / brand label for sidebar and mobile bar.
   * - ``favicon``
     - string
     - ``""``
     - Favicon path relative to ``_static/``.  ``.png``, ``.ico``, ``.svg``.


Colours
-------

.. list-table::
   :header-rows: 1
   :widths: 22 12 15 51

   * - Option
     - Type
     - Default
     - Description
   * - ``color_primary``
     - CSS colour
     - ``#030146``
     - Navy. Headings, TOC active links, API names, version badge.
   * - ``color_accent``
     - CSS colour
     - ``#ff420e``
     - Orange. Unvisited links, active borders, landing gradient.
   * - ``color_sidebar_bg``
     - CSS colour
     - ``#f5f6fa``
     - Sidebar background.
   * - ``color_sidebar_text``
     - CSS colour
     - ``#2d2d48``
     - Sidebar link text (non-active).


Navigation
----------

.. list-table::
   :header-rows: 1
   :widths: 25 12 12 51

   * - Option
     - Type
     - Default
     - Description
   * - ``navigation_depth``
     - integer
     - ``4``
     - Sidebar tree depth.  ``-1`` for unlimited.
   * - ``collapse_navigation``
     - boolean
     - ``False``
     - Collapse inactive sections.
   * - ``show_breadcrumbs``
     - boolean
     - ``True``
     - Show breadcrumb trail above content.


Footer
------

.. list-table::
   :header-rows: 1
   :widths: 22 12 18 48

   * - Option
     - Type
     - Default
     - Description
   * - ``footer_text``
     - string
     - ``"Built with…"``
     - Custom footer text.  Supports basic HTML.
   * - ``show_powered_by``
     - boolean
     - ``True``
     - "Powered by Sphinx & Bulma" in footer.


Content & Layout
----------------

.. list-table::
   :header-rows: 1
   :widths: 25 12 15 48

   * - Option
     - Type
     - Default
     - Description
   * - ``content_max_width``
     - CSS length
     - ``52rem``
     - Content column max width (overridden to 80% on ≥1920px).
   * - ``landing_page``
     - string
     - ``""``
     - Pagename for the landing page (e.g. ``"index"``).  Hides
       sidebar, TOC, breadcrumbs, and pagination on that page.


Repository
----------

.. list-table::
   :header-rows: 1
   :widths: 20 12 18 50

   * - Option
     - Type
     - Default
     - Description
   * - ``repo_url``
     - string
     - ``""``
     - Repository URL.  Shows GitHub icon in header.  Empty to hide.
   * - ``repo_name``
     - string
     - ``"Repository"``
     - Label for the repository link.


html_context (Landing Cards)
----------------------------

Landing page navigation cards are configured via ``html_context``,
not ``html_theme_options``:

.. code-block:: python

   html_context = {
       "landing_page": {
           "menu": [
               {"title": "Page Title", "url": "pagename"},
               ...
           ]
       }
   }

Each dict requires ``title`` (display text) and ``url`` (pagename
relative to doc root, no ``.html`` extension).  Cards render as
``.bst-landing-card`` elements on the landing page only.
