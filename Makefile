install:
	poetry install

test:
	poetry run pytest
pytestinstall:
	pip install pytest
test-coverage:
	poetry run pytest

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

build: check
	poetry build

.PHONY: install test lint selfcheck check build