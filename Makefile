DOCS = docs

.PHONY: all check-style fix-style check-type test-coverage create-docs clean

all: check-style fix-style check-type test-coverage create-docs clean

check-style:
	flake8 .

fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .

check-type:
	mypy --disallow-untyped-defs --strict .

unittest:
	pytest -v .

test-coverage:
	pytest -v --color=yes --cov --cov-report term-missing --cov-report=html:$(DOCS)/htmlcov tests/

kattistest:
	kattis test

create-docs:
	mkdir -p $(DOCS)
	pdoc --output-dir $(DOCS)/docs src/

clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf `find . -type d -name .hypothesis`
	rm -rf `find . -name .coverage`
