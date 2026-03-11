===================
SASS Customisation
===================


Architecture
------------

.. code-block:: text

   sass/
   ├── theme.scss           ← entry point
   ├── _variables.scss      ← design tokens (:root CSS vars + SASS vars)
   ├── _normalize.scss      ← minimal reset
   ├── _base.scss           ← typography, lists, tables, blockquotes
   ├── _layout.scss         ← wrapper, header, breadcrumbs, dark toggle
   ├── _sidebar.scss        ← left navigation panel
   ├── _toc.scss            ← floating on-page TOC with filter
   ├── _code.scss           ← code blocks, Pygments tokens
   ├── _admonitions.scss    ← notes, warnings, sidebar directive
   ├── _content.scss        ← Sphinx domains, roles, search, glossary
   ├── _footer.scss         ← pagination and footer
   ├── _responsive.scss     ← breakpoints, mobile, print
   ├── _landing.scss        ← landing page layout and cards
   └── _dark.scss           ← dark mode CSS var overrides + Pygments

Every partial uses ``@use "variables" as *`` for tokens.  All colours
reference ``var(--bst-xxx)`` so dark mode works automatically.


Workflow
--------

1. Edit any ``.scss`` file
2. Recompile: ``python build.py css``
3. Rebuild docs: ``python build.py docs``


Common Customisations
---------------------

**Wider sidebar:**

.. code-block:: scss

   $sidebar-width:      20rem !default;
   $sidebar-width-wide: 22rem !default;

**Different bullet style:**

.. code-block:: scss

   ul { list-style-type: disc; }   // default is square

**Remove h2 top border:**

.. code-block:: scss

   h2 { border-top: none; padding-top: 0; }

**Narrower ultra-wide content cap:**

.. code-block:: scss

   @media (min-width: 1920px) {
     .bst-article__content { max-width: 70%; }
   }

**Dark code blocks:**

.. code-block:: scss

   pre { background: #1e293b; color: #e2e8f0; border: none; }


Pygments Style
--------------

The default Pygments style is **Tango** (light) with custom dark
overrides in ``_dark.scss``.  To change:

.. code-block:: python

   pygments_style = "monokai"

Then adjust or remove the token rules in ``_code.scss`` and
``_dark.scss`` to avoid conflicts.
