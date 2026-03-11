==========
Typography
==========

This page demonstrates heading levels, inline markup, and text formatting.


Heading Level 2
----------------

Body text flows naturally under headings. The theme uses Source Sans 3 for
body copy and JetBrains Mono for code. Line height is set to 1.7 for
comfortable reading.


Heading Level 3
^^^^^^^^^^^^^^^^

Third-level headings are indented in the sidebar navigation tree. This is
useful for grouping related content within a section.


Heading Level 4
""""""""""""""""

Fourth-level headings are the deepest level recommended. They render as
slightly emphasised body text.


Inline Markup
-------------

Sphinx and reStructuredText support rich inline formatting:

- **Bold text** is written with double asterisks.
- *Italic text* uses single asterisks.
- ``Inline code`` uses double backticks — rendered in monospace.
- :guilabel:`GUI Labels` mark interface elements.
- :menuselection:`File --> Export --> PDF` shows menu paths.
- :kbd:`Ctrl+Shift+P` displays keyboard shortcuts.
- :abbr:`HTML (HyperText Markup Language)` provides abbreviations.
- :command:`grep` marks command names.
- :file:`/etc/acme/config.yaml` highlights file paths.
- :envvar:`ACME_API_KEY` shows environment variables.
- :ref:`search` creates cross-references.
- Superscript: E = mc\ :sup:`2`
- Subscript: H\ :sub:`2`\ O


Paragraph-Level Elements
-------------------------

Normal paragraphs are separated by blank lines. This paragraph demonstrates
how body text wraps and flows at various screen widths. The max content width
is capped at 52rem by default.

| Line blocks preserve
| line breaks exactly
| as written in the source.

..

   Indented block quotes render with a left accent border and subtle
   background. They're useful for attributions or callouts.

.. rubric:: Rubric Heading

A rubric is a heading that does not appear in the table of contents. Use it
for decorative section dividers.

.. centered:: Centred text uses the ``centered`` directive.


Footnotes
---------

Sphinx supports both numbered and auto-numbered footnotes. The platform
supports multiple storage backends [1]_ including H2, PostgreSQL [2]_,
and Oracle.

.. [1] Storage backends are pluggable via the ``StorageProvider`` interface.
.. [2] PostgreSQL 14 or later is recommended for best performance.


Citations
---------

The architecture is based on the shared-nothing principle [Stonebraker2005]_.

.. [Stonebraker2005] Stonebraker, M. (2005). "One Size Fits All — An Idea
   Whose Time Has Come and Gone." *ICDE Keynote*.
