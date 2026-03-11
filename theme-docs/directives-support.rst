====================
Directives Support
====================

This page documents every Sphinx and docutils directive supported by the
theme, including the HTML elements Sphinx generates and how they are
styled.  The theme targets class-only selectors (not ``div.xxx``) to
match both Sphinx 7 (``<div>``) and Sphinx 8+ (``<aside>``, ``<section>``).


Admonitions
-----------

All ten standard admonition types are styled with a coloured left border,
background tint, and an SVG icon in the title.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Directive
     - Colour
     - CSS selector
   * - ``.. note::``
     - Accent (orange)
     - ``.note``
   * - ``.. tip::``
     - Green (success)
     - ``.tip``
   * - ``.. hint::``
     - Green (success)
     - ``.hint``
   * - ``.. important::``
     - Accent (orange)
     - ``.important``
   * - ``.. warning::``
     - Primary (navy)
     - ``.warning``
   * - ``.. caution::``
     - Primary (navy)
     - ``.caution``
   * - ``.. attention::``
     - Primary (navy)
     - ``.attention``
   * - ``.. danger::``
     - Red (danger)
     - ``.danger``
   * - ``.. error::``
     - Red (danger)
     - ``.error``
   * - ``.. seealso::``
     - Accent (orange)
     - ``.seealso``

Generic ``.. admonition:: Title`` uses the base style with no colour.

``.. todo::`` uses ``.admonition-todo`` with info styling.


Version Directives
^^^^^^^^^^^^^^^^^^

``.. versionadded::``, ``.. versionchanged::``, ``.. deprecated::``
render as compact pills with green, yellow, and red left borders
respectively.


Sidebar Directive
-----------------

``.. sidebar:: Title`` floats right at 40% width with text wrapping.
Images inside sidebars are contained to the sidebar box.
See :doc:`sidebar-directive` for full details.

CSS: ``.sidebar``, ``aside.sidebar``, ``div.sidebar``


Topic Directive
---------------

``.. topic:: Title`` renders as a raised box, similar to admonitions
but without a coloured border.

CSS: ``.topic``, ``div.topic``


Code Blocks
-----------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Directive / Element
     - CSS selector
   * - ``.. code-block::``
     - ``div.highlight pre``
   * - ``.. literalinclude::``
     - ``div.highlight pre``
   * - Line numbers (``:linenos:``)
     - ``.linenodiv pre``, ``table.highlighttable``
   * - Caption (``:caption:``)
     - ``div.code-block-caption``
   * - Doctest blocks (``>>>``)
     - ``.doctest``
   * - Literal blocks (``::`` / parsed-literal)
     - ``pre``
   * - Inline code
     - ``:not(pre) > code``
   * - ``kbd`` role
     - ``kbd``

Code blocks use ``clear: right`` to drop below any sidebar float.


Tables
------

All table types — simple, grid, list-table, csv-table — use the same
base table styling with alternating hover rows.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Directive / Element
     - CSS selector
   * - ``.. list-table::``
     - ``table``
   * - ``.. csv-table::``
     - ``table``
   * - Field lists
     - ``dl.field-list``, ``table.field-list``
   * - Option lists
     - ``table.option-list``
   * - Index tables
     - ``table.indextable``, ``table.genindextable``

Tables use ``clear: right`` to drop below sidebar floats.


Images & Figures
----------------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Directive
     - CSS selector
   * - ``.. image::``
     - ``img``, ``a.image-reference``
   * - ``.. figure::``
     - ``figure``, ``figcaption``
   * - ``:align: left``
     - ``.align-left`` (float left)
   * - ``:align: right``
     - ``.align-right`` (float right)
   * - ``:align: center``
     - ``.align-center`` (centred block)


Domain Objects (Python, C++, JS)
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Element
     - CSS selector
   * - Class / function signatures
     - ``dl.py dt``, ``dl.cpp dt``, ``dl.js dt``
   * - Object name
     - ``.sig-name``, ``.descname``
   * - Parameter styling
     - ``.sig-param``, ``.sig-paren``
   * - Property keyword
     - ``.property``
   * - Description body
     - ``dl.py dd``


Inline Roles
------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Role
     - Styling
   * - ``:guilabel:``
     - Background pill with border (``code``-like)
   * - ``:menuselection:``
     - Same as guilabel
   * - ``:command:``
     - Bold monospace
   * - ``:file:``
     - Italic monospace with 📄 prefix
   * - ``:envvar:``
     - Monospace with code background
   * - ``:kbd:``
     - Raised key-cap style with bottom border
   * - ``:abbr:``
     - Dotted underline with cursor help
   * - ``:download:``
     - Bold with ⬇ prefix
   * - ``code.xref``
     - Transparent background, link colour


Block Elements
--------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Directive
     - Styling
   * - ``blockquote``
     - Accent left border, light background
   * - ``.. epigraph::``
     - Italic, wider margins, attribution with "—"
   * - ``.. pull-quote::``
     - Like epigraph but larger font and wider margins
   * - ``.. highlights::``
     - Raised background box
   * - ``.. rubric::``
     - Bold heading that doesn't appear in TOC
   * - ``.. centered::``
     - Centred bold text
   * - ``.. container::``
     - Generic wrapper with margin
   * - ``.. compound::``
     - Margin wrapper for compound paragraphs
   * - Line blocks (``|``)
     - Preserved line breaks, nestable
   * - ``.. productionlist::``
     - Monospace code-styled grammar box
   * - ``.. math::``
     - Scrollable container for MathJax


Footnotes, Citations, Glossary
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Element
     - Styling
   * - ``dl.footnote``
     - Left border, small font
   * - ``dl.citation``
     - Same as footnote
   * - ``a.footnote-reference``
     - Superscript accent colour
   * - ``dl.glossary dt``
     - Bold with dotted bottom border
   * - ``:term:`` role
     - Dotted underline, link colour


HTML5 Elements (Sphinx 8+)
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Element
     - Styling
   * - ``<section>``
     - ``display: block`` (replaces ``div.section``)
   * - ``<aside>``
     - Matches ``.sidebar`` and ``.admonition`` selectors
   * - ``<details>``/``<summary>``
     - Bordered box, clickable summary with hover accent
   * - ``nav.contents``
     - Raised box for ``.. contents::`` directive


Search Results (Sphinx 8+)
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Class
     - Styling
   * - ``li.kind-index``
     - Blue left border
   * - ``li.kind-object``
     - Green left border
   * - ``li.kind-title``
     - Accent left border
   * - ``li.kind-text``
     - Grey left border
   * - ``.highlighted``
     - Yellow background highlight


External Link Indicator
-----------------------

``a.reference.external`` appends a small ↗ superscript arrow after the
link text to distinguish external from internal links.
