==================
Keyboard Shortcuts
==================

All shortcuts are disabled when focus is inside an input field,
text area, or content-editable element.


Shortcuts
---------

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Key
     - Action
   * - :kbd:`/`
     - Focus the sidebar search field.
   * - :kbd:`t`
     - Toggle the floating on-page TOC panel.
   * - :kbd:`Escape`
     - Close the mobile sidebar and collapse the on-page TOC.
       Also clears the TOC filter input if focused.


On-Page TOC Behaviour
---------------------

- **≤ 5 entries**: starts collapsed regardless of screen width.
- **> 5 entries on wide screens** (≥ 1280 px): starts expanded.
- The toggle button (list / X icon) is always visible in the
  top-right corner when the page has a TOC.


TOC Filter
----------

The TOC panel includes a small search input at the top.  Typing
filters the visible entries in real time — only matching items and
their parent hierarchy remain visible.  Press :kbd:`Escape` while
the filter is focused to clear it.
