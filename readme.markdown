Cardgen
=======

To build an example, run makefile to generate design pattern cards from intents.txt

To clone this repository, type from your command line (with git installed):

	git clone http://github.com/alexbowe/cardgen.git
	
This will make a folder 'cardgen' in the working directory and populate it.


Cardgen Usage
-------------

For help:

	./cardgen.py -h 

To run:

	./cardgen.py -i inputfile -o outputfile

or using stdin/stdout:

	./cardgen.py < inputfile > outputfile
	

Inputfile Structure
-------------------

	First Card:
	Definition Line 1
	Definition Line 2
	
	Second Card:
	Single Line Definition