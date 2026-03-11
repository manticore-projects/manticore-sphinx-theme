===========
Admonitions
===========

Sphinx provides a rich set of admonition directives for callout boxes.
Each type has a distinct colour and icon.


Standard Admonitions
--------------------

.. note::

   This is a **note**. Use it for supplementary information that adds context
   without being essential to the main text.

.. tip::

   This is a **tip**. Use it for helpful suggestions and best practices
   that can improve the reader's workflow.

.. hint::

   This is a **hint**. Similar to a tip, but for less obvious information
   the reader might not discover on their own.

.. important::

   This is an **important** notice. Use it for information the reader
   must not overlook.

.. warning::

   This is a **warning**. Use it when the reader could encounter problems
   if they don't follow the guidance.

.. caution::

   This is a **caution** notice. Use it for actions that could lead to
   data loss or security issues if performed incorrectly.

.. attention::

   This is an **attention** notice. Use it to draw focus to a specific
   requirement or constraint.

.. danger::

   This is a **danger** notice. Use it for situations where incorrect
   actions could cause serious harm (data corruption, security breach).

.. error::

   This is an **error** notice. Use it to describe known error conditions
   and their resolutions.


See-Also Box
^^^^^^^^^^^^

.. seealso::

   :doc:`api-reference`
      Full API documentation for all classes and methods.

   `Sphinx Directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_
      Official reference for all built-in directives.


Custom Admonitions
------------------

.. admonition:: Custom Title

   The generic ``admonition`` directive allows a custom title. It uses
   the default styling with no special colour.

.. admonition:: Performance Note
   :class: tip

   You can apply a class to a generic admonition to inherit the styling
   of a specific type — this one uses the ``tip`` class.


Nested Content in Admonitions
-----------------------------

Admonitions can contain any body elements:

.. warning::

   When migrating databases, ensure you:

   1. Back up all data before starting
   2. Verify the backup can be restored
   3. Run the migration in a staging environment first

   .. code-block:: bash

      # Create a backup before migration
      acme-cli backup create --format=snapshot
      acme-cli backup verify --latest

   Skipping any of these steps may result in data loss.


Version Directives
------------------

.. versionadded:: 3.2
   The ``Config.from_env()`` class method for environment-based configuration.

.. versionchanged:: 3.1
   The ``ResultSet`` now supports async iteration via ``async for``.

.. deprecated:: 3.0
   The ``Platform.close()`` method. Use the context manager protocol instead.


Topic Directive
---------------

.. topic:: Why Admonitions Matter

   Good documentation uses callout boxes to break up walls of text and
   highlight critical information. They create visual anchors that help
   readers scan pages quickly and find what they need.


Sidebar Directive
-----------------

.. sidebar:: Related Resources

   - `Sphinx Admonitions <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#admonitions>`_
   - :doc:`typography`
   - :doc:`special-markup`

The sidebar directive creates a floating box on the right side of the
content. It's useful for auxiliary information that relates to the
surrounding text but doesn't interrupt the main flow.

Content continues to flow normally alongside the sidebar. When the
sidebar ends, the text expands back to full width.


Sidebar with Image
^^^^^^^^^^^^^^^^^^

.. sidebar:: Architecture Overview

   .. image:: https://via.placeholder.com/400x250/1e3a5f/ffffff?text=Architecture

   The platform uses a layered architecture with pluggable storage
   backends and a shared-nothing query engine.

This example shows a sidebar containing an image with a caption-like
paragraph below it.  The image scales to fit within the sidebar box
and maintains its aspect ratio. Text wraps around the sidebar naturally,
and the spacing between the sidebar and the body text keeps things
readable.


Todo Directive
--------------

.. todo::

   Add benchmarks comparing admonition rendering performance across
   different Sphinx themes.
