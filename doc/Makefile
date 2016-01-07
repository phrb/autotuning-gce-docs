BASE_NAME = relatorio

FILES     = *.tex img/*.pdf

LATEX     = latex
PDFLATEX  = xelatex
BIBTEX    = bibtex

pdf: $(BASE_NAME).pdf
ps: $(BASE_NAME).ps

$(BASE_NAME).pdf: $(BASE_NAME).tex  abstract.tex introduction.tex related.tex opentuner.tex methodology.tex normalization.tex experiments.tex results.tex future.tex conclusion.tex acknowledgements.tex
	$(PDFLATEX) -shell-escape $<
	$(BIBTEX) $(BASE_NAME)
	$(PDFLATEX) -shell-escape $< 
	$(PDFLATEX) -shell-escape $<
	$(PDFLATEX) -shell-escape $<

$(BASE_NAME).ps: $(BASE_NAME).tex abstract.tex introduction.tex related.tex opentuner.tex methodology.tex normalization.tex experiments.tex results.tex future.tex conclusion.tex acknowledgements.tex
	$(LATEX) $<
	$(BIBTEX) $(BASE_NAME) 
	$(LATEX) $< 
	$(LATEX) $<
	$(LATEX) $<
	
clean:
	rm -f $(BASE_NAME)*.ps $(BASE_NAME)*.dvi *.log \
	      *.aux *.blg *.toc *.brf *.ilg *.ind \
	      missfont.log $(BASE_NAME)*.bbl $(BASE_NAME)*.pdf $(BASE_NAME)*.out \
		  $(BASE_NAME)*.lof $(BASE_NAME)*.lot 
