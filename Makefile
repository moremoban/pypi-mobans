all: upstreaming

upstreaming:
	moban -m mobanfile

lint: flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long

push:
	git config user.email "travis@travis-ci.org"
	git config user.name "traviscibot"
	git commit -am "Sync templates [skip ci]"
	git push https://moremoban:${GITHUB_TOKEN}@github.com/moremoban/pypi-mobans HEAD:moban -f
