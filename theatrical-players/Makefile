help:
	@echo "usage: make test | htmlcov | clean"

test:
	python -m pytest

htmlcov:
	coverage run -m pytest
	coverage html

clean:
	/bin/rm -rf .coverage .pytest_cache __pycache__ htmlcov

