.. module:: score.html
.. role:: confkey
.. role:: confdefault

**********
score.html
**********

A small convenience module that registers the ``html`` :term:`template format`
upon initialization.

Quickstart
==========

No need to do anything, except add this module to your initialization list:

.. code-block:: ini
    :emphasize-lines: 4

    [score.init]
    modules = 
        score.tpl
        score.html

Configuration
=============

.. autofunction:: score.html.init

.. autoclass:: score.html.ConfiguredHtmlModule()
