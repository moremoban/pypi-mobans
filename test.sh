pip freeze
nosetests --with-coverage --cover-package pypi_mobans --cover-package tests  tests docs/source pypi_mobans && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
