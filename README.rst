================================================================================
pypi-mobans
================================================================================

.. image:: https://api.travis-ci.org/moremoban/pypi-mobans.svg
   :target: http://travis-ci.org/moremoban/pypi-mobans

.. image:: https://codecov.io/github/moremoban/pypi-mobans/coverage.png
   :target: https://codecov.io/github/moremoban/pypi-mobans

.. image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :target: https://gitter.im/chfw_moban/Lobby


Scaffolding mobans for your Python project.
It is used with `yehua <https://github.com/chfw/yehua>`_.
Organisations using it:

- `pyexcel <https://github.com/pyexcel/pyexcel>`_.
- `coala <https://github.com/coala/coala>`_.

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

    $ git clone https://github.com/moremoban/pypi-mobans.git
    $ cd pypi-mobans

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
