.PHONY: clean
.PHONY: pep8

clean:
	-rm -r -- *.pyc __pycache__ >/dev/null 2>&1

pep8:
	pep8 *.py
