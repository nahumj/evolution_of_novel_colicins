#Makefile for evolution of novel colicins
.PHONY: clean
.PHONY: pep8
.PHONY: test

run: 
	python3 main.py

test:
	python3 -m unittest discover -b

clean:
	-rm -r -- __pycache__

pep8:
	pep8 *.py
