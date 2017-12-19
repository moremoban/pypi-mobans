================================================================================
pypi-mobans
================================================================================

.. image:: https://api.travis-ci.org/moremoban/pypi-mobans.svg?branch=master
   :target: http://travis-ci.org/moremoban/pypi-mobans

Scaffolding templates for your Python project. It is used with `yehua <https://github.com/chfw/yehua>`_
and `pyexcel <https://github.com/pyexcel/pyexcel>`_.

Features
================================================================================

setup.py
----------

1. flake8 compliant setup.py

2. feature parity with `kennethreitz/setup.py <https://github.com/kennethreitz/setup.py>`_

   - automatically upload to pypi without using twine

   - automatically do git release while uploading to pypi

3. configured to build universial wheels by default

Installation
================================================================================

You can get it:

.. code-block:: bash

    $ git clone http://github.com/moremoban/pypi-mobans.git


Notes
================================================================================


In order to run, `python setup.py publish`, you will have setup `.pypirc` in
your home folder as::

   [distutils]
   index-servers =
     pypi

   [pypi]
   username=your_name
   password=your_password


And you need to configure `gease`. 
