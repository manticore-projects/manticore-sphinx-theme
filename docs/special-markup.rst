==============
Special Markup
==============

This page collects miscellaneous Sphinx features: containers, meta
directives, production lists, download links, and more.


Epigraph
--------

.. epigraph::

   Measuring programming progress by lines of code is like
   measuring aircraft building progress by weight.

   -- Bill Gates


Compound Paragraph
-------------------

.. compound::

   This paragraph contains a literal block that is part of the same
   logical paragraph::

      $ acme-cli status
      Cluster: production
      Nodes: 5/5 healthy
      Uptime: 14d 6h

   The literal block is indented but flows logically with the
   surrounding text.


Pull-Quote
----------

.. pull-quote::

   Documentation is a love letter that you write to your future self.

   -- Damian Conway


Containers
----------

.. container:: custom-class

   The ``container`` directive wraps content in a ``<div>`` with a custom
   CSS class. Themes can style these however they like.


Replacement Substitutions
-------------------------

|project| is currently at version |release|, built on |today|.

.. |project| replace:: **Acme Platform**


Glossary Cross-References
--------------------------

The :term:`cluster` manages multiple :term:`nodes <node>` that communicate via
the internal gossip protocol. Data is stored using the configured
:term:`storage backend`.

See the glossary in :doc:`api-reference`.


Include Directive Simulation
----------------------------

In a real project, you can pull content from other files:

.. code-block:: rst

   .. include:: ../CHANGELOG.md
      :parser: myst_parser.sphinx_

This is useful for keeping a single source of truth for changelogs,
license files, and contribution guidelines.


Raw HTML
--------

.. raw:: html

   <div style="background: linear-gradient(135deg, #1e3a5f 0%, #0077b6 100%);
               color: white; padding: 1.5em 2em; border-radius: 6px;
               margin: 1.5em 0; text-align: center;">
     <strong style="font-size: 1.1em;">Acme Platform</strong><br>
     <span style="opacity: 0.85;">Enterprise-grade data processing</span>
   </div>


Tabs-like Structure with Rubrics
---------------------------------

.. rubric:: Python

.. code-block:: python

   from acme import connect

   with connect("acme://localhost:9090") as p:
       for row in p.query("SELECT 1"):
           print(row)

.. rubric:: cURL

.. code-block:: bash

   curl -X POST https://api.acme.local/v1/query \
     -H "Authorization: Bearer $TOKEN" \
     -d '{"sql": "SELECT 1"}'

.. rubric:: JavaScript

.. code-block:: javascript

   const acme = require('@acme/sdk');

   const client = await acme.connect('acme://localhost:9090');
   const result = await client.query('SELECT 1');
   console.log(result.rows);


Production List
---------------

A grammar for simple expressions:

.. productionlist::
   expression: `term` (('+' | '-') `term`)*
   term: `factor` (('*' | '/') `factor`)*
   factor: NUMBER | '(' `expression` ')'


Target and Reference
--------------------

.. _custom-anchor:

You can create anchors anywhere with ``.. _name:`` and reference them
with ``:ref:`custom-anchor```.


Only / ifconfig
---------------

.. only:: html

   This paragraph only appears in HTML output, not in LaTeX or other builders.

.. only:: latex

   This paragraph would only appear in LaTeX/PDF output.
