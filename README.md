# Příprava na bakalářské státnice (MFF UK)

Studijní repozitář pro bakalářské státní závěrečné zkoušky na MFF UK,
obor **Informatika - Umělá inteligence**, zaměření **Strojové učení**.

Výsledkem je jeden přehledný PDF dokument
[`statnice-priprava.pdf`](statnice-priprava.pdf), který pokrývá **všechny**
požadované okruhy a je postavený na poznámkách *notes-ipp* (Vít Kološ).

## Co je uvnitř

```
pozadavky/      oficiální přípravné dokumenty (zdroj požadavků SZZ)
notes-ipp/      submodul s poznámkami (github.com/vitkolos/notes-ipp)
src/
  build.py      převod poznámek (Markdown) -> LaTeX fragmenty
  preamble.tex  sazba, makra, callout boxy
  main.tex      hlavní dokument (titulka, struktura zkoušky, audit, 4 části)
  audit.tex     audit pokrytí požadavků bod po bodu
  parts/        vygenerované LaTeX fragmenty z poznámek
statnice-priprava.pdf   finální studijní text
```

## Pokrytí požadavků

Dokument prošel auditem proti dvěma oficiálním přípravným dokumentům
(`pozadavky/`, verze požadavků SZZ 28. 7. 2025). **Každé požadované téma je
v poznámkách obsažené.** Detaily a výjimky viz sekce *Audit pokrytí* přímo
v PDF:

* Označená místa, kde poznámky odkazují na vlastní procvičení (žluté rámečky).
* Jediná formální výjimka: Hilbertovský kalkul (v požadavcích uveden jen jako
  alternativa k tablu/rezoluci, které pokryté jsou).

## Sestavení PDF

Potřebuješ TeX Live (pdflatex, latexmk) a Python 3.

```bash
git clone --recurse-submodules <repo>
cd statnice-mff
make          # vygeneruje a zkompiluje statnice-priprava.pdf
```

Pokud jsi klonoval bez submodulů:

```bash
git submodule update --init --recursive
```

## Zdroje

* Poznámky: [vitkolos/notes-ipp](https://github.com/vitkolos/notes-ipp)
  (zde jako submodul, obsah je odborně nezměněný).
* Oficiální požadavky: dokumenty ve složce `pozadavky/`.
