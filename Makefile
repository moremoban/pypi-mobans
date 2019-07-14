upstreaming:
	moban -m mobanfile

git-diff-check:
	git diff
	git diff --ignore-blank-lines | while read line; do if [ "$line" ]; then exit 1; fi; done

install_test:
	pip install -r tests/requirements.txt

lint:
	flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
	yamllint .

push:
	git config user.email "travis@travis-ci.org"
	git config user.name "traviscibot"
	git commit -am "Sync templates [skip ci]"
	if [ $? -eq 0 ]
	then
		git push https://moremoban:${GITHUB_TOKEN}@github.com/moremoban/pypi-mobans HEAD:moban -f
	fi
