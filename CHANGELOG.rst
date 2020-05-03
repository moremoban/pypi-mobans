Change log
================================================================================

0.0.11 - 03.05.2020
--------------------------------------------------------------------------------

**Updated**

#. Configure lint and moban stage use to MINREQ=0
#. Updated gitignore to latest as of the release date

0.0.10 - 20.04.2020
--------------------------------------------------------------------------------

**Added**

#. add python_requires in setup.py
#. no code coverage support
#. add github star badges

**Fixed**

#. fixed travis config

0.0.9 - 13.10.2019
--------------------------------------------------------------------------------

**Added**

#. pypi download stats are displayed in README
#. Add mit license text
#. `#126 <https://github.com/moremoban/pypi-mobans/issues/126>`_: support github
   auto pypi publishing action
#. `#133 <https://github.com/moremoban/pypi-mobans/issues/133>`_: provide CI
   azure build yaml files

**Updated**

#. Test on python 3.8 instead of python 3.8-dev
#. `#131 <https://github.com/moremoban/pypi-mobans/issues/131>`_: remove useless
   statements when a complex installation requirement is in place.
#. `#128 <https://github.com/moremoban/pypi-mobans/issues/128>`_: Exclude tests
   in installation package
#. Install mock only on python 2

0.0.8 - 13.10.2019
--------------------------------------------------------------------------------

**Fixed**

#. `#114 <https://github.com/moremoban/pypi-mobans/issues/114>`_: setup.py.jj2
   gets default console_scripts entry always
#. `#120 <https://github.com/moremoban/pypi-mobans/issues/120>`_: changelog rst
   syntax cause 400 error
#. `#122 <https://github.com/moremoban/pypi-mobans/issues/122>`_:
   UPLOAD_FAILED_MSG cannot be formatted

0.0.7 - 14.07.2019
--------------------------------------------------------------------------------

**Updated**

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

**Added**

#. `#89 <https://github.com/moremoban/pypi-mobans/issues/89>`_: setup.py.jj2
   support for dependencies using all PEP 508 environment markers; enable
   setup_use_markers to activate, and enable setup_use_markers_fix to use with
   setuptools pre v22
#. `#98 <https://github.com/moremoban/pypi-mobans/issues/98>`_: Added
   .gitattributes to reduce conflicts on changelog.yml

0.0.6 - 25-05-2019
--------------------------------------------------------------------------------

**Updated**

#. `#87 <https://github.com/moremoban/pypi-mobans/issues/87>`_: updated the
   pipfile syntax

**Added**

#. `#87 <https://github.com/moremoban/pypi-mobans/issues/87>`_: Added tests for
   pipfile generation

0.0.5 - 04-05-2019
--------------------------------------------------------------------------------

**Updated**

#. `#75 <https://github.com/moremoban/pypi-mobans/issues/75>`_: separate flake8
   linting in separate travis job
#. `#72 <https://github.com/moremoban/pypi-mobans/issues/72>`_: project and
   copyright are no longer filled.
#. black style on setup.py, include python 3.7, 3.8 , update gitignore

0.0.4 - 18-02-2019
--------------------------------------------------------------------------------

**Updated**

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

**First release**

#. bug fix on `#60 <https://github.com/moremoban/pypi-mobans/pull/60>`_

0.0.2 - 18-01-2019
--------------------------------------------------------------------------------

**Added**

#. `#60 <https://github.com/moremoban/pypi-mobans/pull/60>`_: codec and locale
   hacks added
#. `#61 <https://github.com/moremoban/pypi-mobans/pull/61>`_: add python
   classifiers

**Updated**

#. `#63 <https://github.com/moremoban/pypi-mobans/pull/63>`_: updated Pipfile
   implementation
#. Synchronize with sphinx doc file at release date

0.0.1 - 05-11-2018
--------------------------------------------------------------------------------

**First release**

#. versioning is applied
#. Pipfile included
