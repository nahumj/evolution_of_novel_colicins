.PHONY: clean
.PHONY: pep8

clean:
	-rm -r -- __pycache__

pep8:
	pep8 *.py
