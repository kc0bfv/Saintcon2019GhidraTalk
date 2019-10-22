talk_presentation.pdf:

%.pdf: %.latex
	pdflatex $< || (rm $@ && false)
	pdflatex $< || (rm $@ && false)

PHONY: clean

clean:
	rm *.aux *.log *.nav *.out *.snm *.toc talk_presentation.pdf
