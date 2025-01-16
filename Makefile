.PHONY: clean-pyc clean-build

clean-pyc:
	find ./src ./tests ./examples -name '*.pyc' -exec rm -rf {} +
	find ./src ./tests ./examples -name '*.pyo' -exec rm -rf {} +

clean-build:
	rm -rf dist/

init:
	uv install

check:
	uv run ruff check

build:
	uv build

publish:
	make build
	uv publish
	rm -rf dist
