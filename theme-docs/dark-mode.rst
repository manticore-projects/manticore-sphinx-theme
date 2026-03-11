=========
Dark Mode
=========

The theme includes a 3-state dark mode that respects system preferences
and persists across page navigations.


How It Works
------------

**Three states**, cycled by the toggle button in the header:

1. **System** (default) — monitor icon.  No ``data-theme`` attribute on
   ``<html>``, no value in localStorage.  CSS ``@media (prefers-color-scheme: dark)``
   handles everything — zero JavaScript involved.

2. **Dark** — moon icon.  Sets ``data-theme="dark"`` on ``<html>`` and
   stores ``"dark"`` in localStorage.

3. **Light** — sun icon.  Sets ``data-theme="light"`` on ``<html>`` and
   stores ``"light"`` in localStorage.

Clicking the toggle cycles: System → Dark → Light → System.


Persistence Across Pages
^^^^^^^^^^^^^^^^^^^^^^^^

An inline ``<script>`` in the ``<head>`` of every page runs **before
any CSS loads**:

.. code-block:: javascript

   var s = localStorage.getItem("bst-theme");
   if (s === "dark" || s === "light") {
     document.documentElement.setAttribute("data-theme", s);
   }

This prevents any flash of the wrong theme during navigation.  If no
value is stored (System mode), the script does nothing and CSS
``@media`` handles it.


Architecture
------------

All colours are CSS custom properties defined in ``_variables.scss``:

.. code-block:: scss

   :root {
     --bst-bg:     #ffffff;
     --bst-text:   #2d2d48;
     --bst-accent: #ff420e;
     /* ... 25+ properties ... */
   }

Dark mode overrides them in ``_dark.scss`` using two identical blocks:

.. code-block:: scss

   /* OS preference: */
   @media (prefers-color-scheme: dark) {
     html:not([data-theme="light"]) {
       --bst-bg:     #0e0e1e;
       --bst-text:   #d1d3de;
       --bst-accent: #ff6b3d;
       /* ... */
     }
   }

   /* Manual toggle: */
   html[data-theme="dark"] {
     --bst-bg:     #0e0e1e;
     --bst-text:   #d1d3de;
     --bst-accent: #ff6b3d;
     /* ... */
   }

No SASS mixin, no JavaScript for colour switching — pure CSS custom
property inheritance.  Pygments syntax highlighting tokens are the only
exception (they need explicit selectors for each token class).


Dark Palette
^^^^^^^^^^^^

The dark colours are derived from the Manticore branding:

- Navy (#030146) lightens to periwinkle (#7b7bbd)
- Orange (#ff420e) brightens to coral (#ff6b3d)
- Backgrounds go deep indigo (#0e0e1e, #141428, #18182e)
- Borders soften to dark slate (#2e2e50)


Customising Dark Mode
---------------------

Edit the dark palette in ``_dark.scss``.  Every ``--bst-*`` property
listed in the dark blocks can be changed.  Recompile with
``python build.py css``.

To disable dark mode entirely, remove ``@use "dark"`` from
``theme.scss`` and recompile.
