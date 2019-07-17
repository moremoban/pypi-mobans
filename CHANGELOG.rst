Change log
================================================================================

0.0.8 - tba
--------------------------------------------------------------------------------

Updated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `moban#295 <https://github.com/moremoban/moban/issues/295>`_: limit publish
   command in setup.py to be less than 79

0.0.7 - 14.07.2019
--------------------------------------------------------------------------------

Updated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. sync templates/docs/make.bat.jj2 to include changes from
   https://github.com/sphinx-doc/sphinx/commit/0dbdae31
#. `#100 <https://github.com/moremoban/pypi-mobans/issues/100>`_: Fixed
   travis.yml.jj2 to not emit yamllint errors
#. `#101 <https://github.com/moremoban/pypi-mobans/issues/101>`_: Fixed
   travis.yml.jj2 .disable_global to reset `install:`
#. `#31 <https://github.com/moremoban/pypi-mobans/issues/31>`_: Added
   test_command to override travis.yml.jj2 use of Makefile
#. `#96 <https://github.com/moremoban/pypi-mobans/issues/96>`_: Expanded
   travis.yml.jj2 and use in in the pypi-mobans repo
#. `#88 <https://github.com/moremoban/pypi-mobans/issues/88>`_: Enhanced
   min_requirements.txt.jj2 support for dependencies with multiple constraints
   such as `>1,<3`
#. `#93 <https://github.com/moremoban/pypi-mobans/issues/93>`_: Added CI to
   ensure pypi-mobans is in sync with upstream
#. `#99 <https://github.com/moremoban/pypi-mobans/issues/99>`_: Formated
   changelog.yml according to yamllint default rules

Added
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `#89 <https://github.com/moremoban/pypi-mobans/issues/89>`_: setup.py.jj2
   support for dependencies using all PEP 508 environment markers; enable
   setup_use_markers to activate, and enable setup_use_markers_fix to use with
   setuptools pre v22
#. `#98 <https://github.com/moremoban/pypi-mobans/issues/98>`_: Added
   .gitattributes to reduce conflicts on changelog.yml

0.0.6 - 25-05-2019
--------------------------------------------------------------------------------

Updated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `#87 <https://github.com/moremoban/pypi-mobans/issues/87>`_: updated the
   pipfile syntax

Added
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `#87 <https://github.com/moremoban/pypi-mobans/issues/87>`_: Added tests for
   pipfile generation

0.0.5 - 04-05-2019
--------------------------------------------------------------------------------

Updated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `#75 <https://github.com/moremoban/pypi-mobans/issues/75>`_: separate flake8
   linting in separate travis job
#. `#72 <https://github.com/moremoban/pypi-mobans/issues/72>`_: project and
   copyright are no longer filled.
#. black style on setup.py, include python 3.7, 3.8 , update gitignore

0.0.4 - 18-02-2019
--------------------------------------------------------------------------------

Updated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. travis-ci: uses xenial dist. dropped python 3.4, 3.7-dev and added 3.7, pypy2
   and pypy3
#. added min_requirements.txt where minimum requirements are computed
#. `#71 <https://github.com/moremoban/pypi-mobans/issues/71>`_: include tests
   folder as test_suite if 'tests' folder exists
#. `#16 <https://github.com/moremoban/pypi-mobans/issues/16>`_: package data /
   MANIFEST.in.jj2 is not easy to customise
#. `#14 <https://github.com/moremoban/pypi-mobans/issues/14>`_: Mandatory
   CHANGELOG.rst become optional

0.0.3 - 18-01-2019
--------------------------------------------------------------------------------

First release
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. bug fix on `#60 <https://github.com/moremoban/pypi-mobans/pull/60>`_

0.0.2 - 18-01-2019
--------------------------------------------------------------------------------

Added
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `#60 <https://github.com/moremoban/pypi-mobans/pull/60>`_: codec and locale
   hacks added
#. `#61 <https://github.com/moremoban/pypi-mobans/pull/61>`_: add python
   classifiers

Updated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `#63 <https://github.com/moremoban/pypi-mobans/pull/63>`_: updated Pipfile
   implementation
#. Synchronize with sphinx doc file at release date

0.0.1 - 05-11-2018
--------------------------------------------------------------------------------

First release
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. versioning is applied
#. Pipfile included
