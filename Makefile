.PHONY: all clean distclean

# Zkompiluje lean studijní PDF (hand-authored sekce v src/sections/).
all:
	cd src && latexmk -pdf -interaction=nonstopmode main.tex
	cp src/main.pdf statnice-priprava.pdf
	@echo "Hotovo: statnice-priprava.pdf"
	@echo "Kontrola pomlček (musí být 0):"
	@pdftotext statnice-priprava.pdf - | grep -c "[–—]" || true

clean:
	cd src && latexmk -c

distclean:
	cd src && latexmk -C
	rm -f statnice-priprava.pdf
