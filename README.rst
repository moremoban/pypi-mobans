================================================================================
pypi-mobans
================================================================================

.. image:: https://api.travis-ci.org/moremoban/pypi-mobans.svg
   :target: http://travis-ci.org/moremoban/pypi-mobans

.. image:: https://codecov.io/github/moremoban/pypi-mobans/coverage.png
   :target: https://codecov.io/github/moremoban/pypi-mobans
.. image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :target: https://gitter.im/chfw_moban/Lobby
.. image:: https://img.shields.io/github/stars/moremoban/pypi-mobans.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/pypi-mobans/stargazers


Scaffolding templates for your Python project.


create a blank python package that is usable and ready to push to github. And future
updates on your organisation's specific static information can be instantly applies the
update accurately using `moban`_. Here is a list of features:

#. core python package
#. test configuration setup
#. ready to commit github repository
#. automated upload to pypi through twine
#. version management through jinja2
#. automated github release through gease


It is used with `yehua <https://github.com/chfw/yehua>`_.
Organisations using it:

- `pyexcel mobans <https://github.com/pyexcel/pyexcel-mobans>`_.
- `coala mobans <https://gitlab.com/coala/mobans>`_.
- `pyecharts pypkg mobans <https://github.com/pyecharts/pypkg-mobans>`_.
- `echarts maps mobans <https://github.com/echarts-maps/echarts-js-mobans>`_.

Features
================================================================================

Feature comparision
--------------------------------------------------------------------------------

The following table is a personal feature comparision. If you have a different
opinion, especially you are the author of the following repository, please
raise an issue and we can talk. This table is not a commerical sales pitch.

#. Y: have such a feature
#. M: manual operation
#. A: automatic operation

.. table:: Detailed feature comparision

    ============== ========================== ======================= ===================== ========== =====
    Group          Feature                    cookiecutter-pypackage  cookiecutter-vanguard PyScaffold yehua
    ============== ========================== ======================= ===================== ========== =====
    essential      setup.py                   Y                        Y                     Y         Y
    .              setup.cfg                  Y                        Y                     Y         Y
    .              source code stub           Y                        Y                     Y         Y
    test setup     requirements.txt                                    Y                     Y         Y
    .              requirements_dev.txt       Y                        Y                               Y
    .              Makefile                   Y                                                        Y
    .              tests code                 Y                        Y                     Y
    .              tox                        Y                                              Y
    .              travis                     Y                                              Y         Y
    .              test coverage                                       Y                               Y
    .              flake8                                                                              Y
    documentation  README.rst                 Y                                              Y         Y
    .              labels                                                                              Y
    .              gitignore                  Y                                              Y         Y
    .              AUTHORS.rst                Y                        Y                     Y
    .              CONTRIBUTING.rst           Y                        Y
    .              HISTORY.rst/CHANGELOG .rst Y                        Y                     Y         Y
    .              LICENCE                    Y                        Y                     Y         Y
    .              MANIFEST.in                Y                        Y                               Y
    .              sphinx docs                Y                        Y                     Y         Y
    usability      interactive shell          Y                        Y                               Y
    .              one liner                                                                 Y
    .              initialize github repo                                                              Y
    maintenance    publish on pypi            A                        M                               M
    .              dependency management      M                                              M         A
    .              template customization                                                              Y
    .              version management         M                                              M         A
    .              automated github release                                                            Y
    .              continous templating                                                                Y
    ============== ========================== ======================= ===================== ========== =====


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

User guides
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


Restrict your package to a python version
--------------------------------------------------------------------------------

The following strings are required in your project yaml file::

   python_requires: ">=3.6"
   min_python_version: "3.6"


Using dependency markers in `setup.py`
--------------------------------------------------------------------------------

In order to use dependency markers in `setup.py`, add `setup_use_markers: true`
in your `mobanfile.


Developer Guides
================================================================================

In order to update this README, please find the .moban.d/local-README.rst.jj2,
and place your changes there.

Then call::

    $ make upstreaming
