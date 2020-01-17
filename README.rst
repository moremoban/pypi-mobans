================================================================================
pypi-mobans
================================================================================

.. image:: https://api.travis-ci.org/moremoban/pypi-mobans.svg
   :target: http://travis-ci.org/moremoban/pypi-mobans

.. image:: https://codecov.io/github/moremoban/pypi-mobans/coverage.png
   :target: https://codecov.io/github/moremoban/pypi-mobans
.. image:: https://img.shields.io/github/stars/moremoban/pypi-mobans.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/pypi-mobans/stargazers

.. image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :target: https://gitter.im/chfw_moban/Lobby


Scaffolding templates for your Python project.
It is used with `yehua <https://github.com/chfw/yehua>`_.
Organisations using it:

- `pyexcel mobans <https://github.com/pyexcel/pyexcel-mobans>`_.
- `coala mobans <https://gitlab.com/coala/mobans>`_.
- `pyecharts pypkg mobans <https://github.com/pyecharts/pypkg-mobans>`_.
- `echarts maps mobans <https://github.com/echarts-maps/echarts-js-mobans>`_.

Features
================================================================================

setup.py
----------

1. flake8 compliant setup.py

2. feature parity with `kennethreitz/setup.py <https://github.com/kennethreitz/setup.py>`_

   - automatically upload to pypi without using twine

   - automatically do git release while uploading to pypi

3. configured to build universial wheels by default

4. comes with a feature of removing comments from requirements.txt while loading
into setup.py


Installation
================================================================================

You can get it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/pypi-mobans.git
    $ cd pypi-mobans

Development process
================================================================================

Please fork and make pull request to **dev** branch. Per each release, dev branch
will be merged into master branch.

In order to make moban updates: please call `make`.

Notes
================================================================================


Release and publish from command line
--------------------------------------------------------------------------------

In order to run, `python setup.py publish`, you will have setup `.pypirc` in
your home folder as::

   [distutils]
   index-servers =
     pypi

   [pypi]
   username=your_name
   password=your_password


And you need to configure `gease`.

Auto publishing via github action
--------------------------------------------------------------------------------


In order to configure github to publish your package, you will need to set up
two secrets::

    PYPI_USERNAME
    PYPI_PASSWORD

Once you have done that, a github release will trigger an auto publishing.
