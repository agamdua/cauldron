===============================
Cauldron - store all the things!
===============================

.. image:: https://badge.fury.io/py/cauldron.png
    :target: http://badge.fury.io/py/cauldron

.. image:: https://travis-ci.org/agamdua/cauldron.png?branch=develop
        :target: https://travis-ci.org/agamdua/cauldron

.. image:: https://pypip.in/d/pycauldron/badge.png
        :target: https://pypi.python.org/pypi/pycauldron


Cauldron lets you store all the objects according to rules

* Free software: BSD license
* Documentation: https://cauldron.readthedocs.org.

Features
--------

Cauldron allows you to store all your objects according to a
set of rules.


Usage
-----

The API is a WIP, but essentially run:

.. highlight:: python
	python object_cache.py

Note that this requires one to clone the repository as opposed to
install it.

As one can see, this package has not been released yet.


Configuration
-------------

Cauldron collects objects based on two types of rules:

1. Rules for the module walk, i.e., rules to decide which file to
look in
2. Rules for inspection, i.e., rules according to which certain objects
will be stored in the cache.

These rules are supplied while instantiating an `ObjectCache` instance.
