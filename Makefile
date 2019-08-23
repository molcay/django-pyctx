.PHONY: clean-pyc clean-build
clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {}
clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

init:
	pip install pipenv --upgrade
	pipenv install --dev

check:
	pip install 'twine>=1.5.0'
	twine check dist/*

publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg django_pyctx.egg-info
