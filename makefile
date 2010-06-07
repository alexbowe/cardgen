intents.pdf: intents.tex
	pdflatex intents.tex
	
intents.tex: intents.txt
	python cardgen.py -i intents.txt -o intents.tex
	
clean:
	rm -rf *.log *.aux intents.tex *.pdf