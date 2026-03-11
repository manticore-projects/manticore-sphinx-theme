==============================
Manticore Sphinx Theme
==============================

A clean, elegant documentation theme for **Sphinx 7+** built on
**Bulma CSS / SASS** with zero NPM or Node.js dependencies.

Designed for corporate software documentation with an RTD-style layout,
automatic dark mode, a floating on-page TOC with search, and a
corporate landing page — all in 1,500 lines of modern SCSS.


.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   quickstart

.. toctree::
   :maxdepth: 2
   :caption: Customisation

   configuration
   colours-fonts
   branding
   dark-mode
   landing-page
   sidebar-directive
   sass-customisation

.. toctree::
   :maxdepth: 2
   :caption: Building & Deploying

   build-system
   optimization
   deployment

.. toctree::
   :maxdepth: 1
   :caption: Reference

   options-reference
   keyboard-shortcuts
   directives-support


Features
--------

- **RTD-style layout** — fixed left sidebar with tree navigation
- **3-state dark mode** — System / Dark / Light, persisted across pages
- **Floating on-page TOC** with live search filter and fold/unfold
- **Corporate landing page** — no sidebar, centred hero, card grid
- **Sidebar directive** — ``.. sidebar::`` with images floats correctly
- **Roboto font family** — Medium for headings, Slab for body, Mono for code
- **Full Sphinx directive coverage** — every directive styled
- **Responsive** — mobile sidebar, touch-friendly, print stylesheet
- **No NPM** — compiles with ``dart-sass`` or Python ``libsass``
- **Modern SCSS** — ``@use`` / ``@forward``, CSS custom properties for dark mode
- **Cross-platform build** — ``Makefile`` and ``build.py`` (pure Python)
- **Post-build optimization** — HTML/CSS minification and gzip pre-compression
