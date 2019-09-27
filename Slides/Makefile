talk_presentation.pdf:

%.toc: %.latex
	pdflatex $<

%.pdf: %.latex %.toc
	pdflatex $<

PHONY: clean

clean:
	rm *.aux *.log *.nav *.out *.snm *.toc talk_presentation.pdf
