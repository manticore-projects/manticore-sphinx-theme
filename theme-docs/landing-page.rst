============
Landing Page
============

The theme supports a corporate landing page that hides the sidebar,
breadcrumbs, on-page TOC, and pagination — presenting a clean centred
layout with a gradient title and card grid.


Enabling the Landing Page
-------------------------

Set ``landing_page`` in ``html_theme_options`` to the **pagename** of
your landing page (typically ``"index"``):

.. code-block:: python

   html_theme_options = {
       "landing_page": "index",
   }

The template checks ``pagename == theme_landing_page`` and adds
``class="bst-body--landing"`` to the ``<body>`` tag.  CSS does the rest.


What Gets Hidden
^^^^^^^^^^^^^^^^

The ``.bst-body--landing`` class hides these elements via
``display: none !important``:

- Left sidebar (still accessible via hamburger menu)
- Breadcrumb trail
- On-page TOC and its toggle button
- Prev/Next pagination

The header bar (dark mode toggle + repo link) and footer remain visible.


Content Layout
--------------

Landing content is centred at ``max-width: 64rem`` and uses special
styling:

- The **page title** (h1) renders with a gradient from primary → accent
- The **first paragraph** after the title becomes a centred subtitle
- **Section headings** (h2) are centred with an accent underline
- **toctree wrappers** render as a card grid

Landing Cards from conf.py
--------------------------

Define your landing page cards in ``html_context`` in ``conf.py``:

.. code-block:: python

   html_context = {
       "landing_page": {
           "menu": [
               {
                   "title": "IFRS VBox",
                   "url": "VBox/ifrs",
                   "description": "IFRS 9 compliant financial instruments.",
                   "icon": "M3 3h18v18H3z",  # optional SVG path
               },
               {
                   "title": "RISK VBox",
                   "url": "VBox/risk",
               },
           ]
       }
   }

Each card accepts:

``title`` (required)
   Display text shown as the card heading.

``url`` (required)
   Pagename relative to the documentation root (no ``.html``).

``description`` (optional)
   Subtitle text below the title, rendered in a lighter colour.

``icon`` (optional)
   An SVG path string (``d`` attribute) rendered inside a 24×24
   viewBox.  When omitted, the card shows title and description only.

The cards are rendered entirely by the Jinja template — no raw HTML
needed in your RST source.  They appear **after** the page body on
the landing page and adapt to dark mode automatically.


Mobile Behaviour
----------------

On mobile, the landing page shows the hamburger menu bar.  The sidebar
slides in as a drawer when tapped.  Card grids stack to a single column.
