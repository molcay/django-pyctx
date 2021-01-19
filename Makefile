.PHONY: clean-pyc clean-build
clean:
	rm -rf build dist .egg django_pyctx.egg-info
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {}

init:
	pip install poetry --upgrade
	poetry install

check:
	pip install 'twine>=1.5.0'
	twine check dist/*

build:
	python setup.py sdist bdist_wheel
	make check

publish:
	make build
	twine upload dist/*
	make clean
