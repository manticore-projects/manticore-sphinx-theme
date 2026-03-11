=================
Sidebar Directive
=================

The reStructuredText ``.. sidebar::`` directive creates a floating box
on the right side of the content.  This theme provides full support
including images, figures, and text wrapping.


Usage
-----

.. code-block:: rst

   .. sidebar:: My Caption

      .. image:: _images/screenshot.png

      Description text below the image.

   Main body text flows here and wraps around the sidebar.
   Paragraphs continue alongside the floating box.

The sidebar floats right with ``float: right !important`` and occupies
40% of the content width (capped at 22rem, minimum 12rem).


Image Handling
--------------

Sphinx generates images inside sidebars as:

.. code-block:: html

   <aside class="sidebar">
     <p class="sidebar-title">Caption</p>
     <a class="image-reference">
       <img class="align-right" style="width: 100%;">
     </a>
   </aside>

The theme overrides Sphinx's ``align-right`` class on images inside
the sidebar to prevent the image from floating out of the box:

.. code-block:: scss

   .sidebar img {
     display: block !important;
     float: none !important;       // kill align-right
     width: 100%;
     max-width: 100% !important;
   }

The inline ``<style>`` block in ``layout.html`` provides the same rules
at highest CSS priority as a safety net.


Float Behaviour
---------------

**Paragraphs** after the sidebar wrap normally alongside it.

**Code blocks, tables, and other wide elements** use ``clear: right``
to drop below the sidebar — they're too wide to squeeze beside it.

On **mobile** (< 768px), the sidebar stops floating and goes full-width,
with images capped at 60% of the screen.


Tips
----

- Place the ``.. sidebar::`` directive **before** the text that should
  wrap around it in your ``.rst`` source.
- Add more content to the sidebar (text, lists) to make it taller and
  allow more wrapping.
- For very short sidebars, the wrapping effect may not be visible
  because the following paragraphs fit entirely in the remaining width.
