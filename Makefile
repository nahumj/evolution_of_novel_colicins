.PHONY: clean
.PHONY: pep8
.PHONY: test

test:
	python3 -m unittest discover -b

clean:
	-rm -r -- __pycache__

pep8:
	pep8 *.py
