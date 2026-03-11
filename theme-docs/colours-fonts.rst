================
Colours & Fonts
================


Colour Palette
--------------

The theme uses CSS custom properties for every colour, defined in
``_variables.scss`` under ``:root``.  Dark mode overrides these in
``_dark.scss``.

**Light mode defaults (Manticore branding):**

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Variable
     - Default
     - Usage
   * - ``--bst-primary``
     - ``#030146``
     - Headings, TOC active links, API names, version badge
   * - ``--bst-accent``
     - ``#ff420e``
     - Unvisited links, active borders, landing gradient
   * - ``--bst-bg``
     - ``#ffffff``
     - Page background
   * - ``--bst-text``
     - ``#2d2d48``
     - Body text
   * - ``--bst-text-light``
     - ``#5f6580``
     - Visited links, secondary text, captions
   * - ``--bst-text-strong``
     - ``#0e0e2c``
     - Table headers, bold text
   * - ``--bst-border``
     - ``#d8dbe5``
     - Borders, sidebar dividers
   * - ``--bst-code-inline-fg``
     - ``#d63200``
     - Inline code text colour

**Quick change via conf.py** (no recompilation):

.. code-block:: python

   html_theme_options = {
       "color_primary": "#2c3e50",    # changes headings, TOC links
       "color_accent": "#e74c3c",     # changes links, active states
   }


Example Palettes
^^^^^^^^^^^^^^^^

**Ocean Blue:**

.. code-block:: python

   "color_primary": "#1a365d",
   "color_accent": "#3182ce",

**Forest Green:**

.. code-block:: python

   "color_primary": "#1b4332",
   "color_accent": "#2d6a4f",

**Slate Mono:**

.. code-block:: python

   "color_primary": "#1e293b",
   "color_accent": "#475569",


Font Stack
----------

The theme uses three Roboto variants loaded from Google Fonts:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - SASS Variable
     - Font
     - Usage
   * - ``$family-heading``
     - Roboto (Medium 500)
     - Headings h1–h6, sidebar nav, breadcrumbs, TOC, footer, sidebar title
   * - ``$family-sans``
     - Roboto Slab
     - Body paragraph text (slab-serif for editorial feel)
   * - ``$family-mono``
     - Roboto Mono
     - Code blocks, inline code, ``kbd``, terminal output

Base font size is **18 px** (1.125 rem).  All sizes are 2 pt larger
than typical defaults for improved readability:

- Body: 18 px, Small: 16 px, XSmall: 15 px
- h1: 36 px, h2: 30 px, h3: 24 px, h4: 20 px


Changing Fonts
^^^^^^^^^^^^^^

1. Edit ``_variables.scss``:

   .. code-block:: scss

      $family-heading: "Inter", system-ui, sans-serif !default;
      $family-sans:    "Source Serif 4", Georgia, serif !default;
      $family-mono:    "Fira Code", Consolas, monospace !default;

2. Update the Google Fonts ``<link>`` in ``layout.html`` (the
   ``extrahead`` block).

3. Recompile: ``python build.py css``


Link Colours
------------

Unvisited links
   Accent colour (``--bst-accent``, orange by default).

Visited links
   Grey (``--bst-text-light``).  Hover restores the hover colour.

TOC links (sidebar and on-page)
   Primary colour (``--bst-primary``, navy).  The active indicator
   border uses the accent colour for contrast.

Headings
   Primary colour (``--bst-primary``, navy).
