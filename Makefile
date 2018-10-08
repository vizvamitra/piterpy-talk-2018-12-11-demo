test:
	python3 -m unittest discover tests/dry
	@find ./tests -name __pycache__ | xargs rm -rf

all: test
