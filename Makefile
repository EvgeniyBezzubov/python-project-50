install:
	poetry install

test:
	poetry run pytest
pytestinstall:
	pip install pytest
test-coverage:
	poetry run pytest --cov tests/

lint:
	poetry run flake8 hexlet_python_package

selfcheck:
	poetry check

build: check
	poetry build

.PHONY: install test lint selfcheck check build