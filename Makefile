all: test cleanup

cleanup:
	@find ./ -name __pycache__ | xargs rm -rf
	@find ./ -name '*.pyc' | xargs rm -rf

test:
	python3 -m unittest discover tests/dry
	python3 -m unittest discover tests/demo
