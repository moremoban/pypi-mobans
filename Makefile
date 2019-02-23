all: upstreaming

upstreaming:
	moban -m mobanfile

lint: flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
