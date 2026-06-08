.PHONY: all build clean distclean

# Vygeneruje LaTeX z poznámek a zkompiluje PDF.
all: build
	cd src && latexmk -pdf -interaction=nonstopmode main.tex
	cp src/main.pdf statnice-priprava.pdf
	@echo "Hotovo: statnice-priprava.pdf"

# Jen převod poznámek (Markdown -> LaTeX fragmenty).
build:
	python3 src/build.py

# Smaže pomocné soubory sazby (PDF i vygenerované fragmenty ponechá).
clean:
	cd src && latexmk -c

# Smaže úplně vše vygenerované.
distclean:
	cd src && latexmk -C
	rm -f src/parts/*.tex statnice-priprava.pdf
