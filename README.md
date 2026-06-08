# Příprava na bakalářské státnice (MFF UK)

Studijní repozitář pro bakalářské státní závěrečné zkoušky na MFF UK,
obor **Informatika - Umělá inteligence**, zaměření **Strojové učení**.

Výsledkem je jeden přehledný PDF dokument
[`statnice-priprava.pdf`](statnice-priprava.pdf), který pokrývá **všechny**
požadované okruhy a je postavený na poznámkách *notes-ipp* (Vít Kološ).

## Co je uvnitř

```
pozadavky/
  detailni-pozadavky.pdf   ZÁVAZNÝ oficiální zdroj požadavků SZZ (anchor)
  SZZ_strojove_uceni.pdf, mff_statnice_...pdf   odvozené přehledy (z téhož zdroje)
notes-ipp/      submodul s poznámkami (github.com/vitkolos/notes-ipp)
src/
  build.py      převod poznámek (Markdown) -> LaTeX fragmenty
  preamble.tex  sazba, makra, callout boxy
  main.tex      hlavní dokument (titulka, struktura zkoušky, audit, 4 části)
  audit.tex     audit pokrytí požadavků bod po bodu
  parts/        vygenerované LaTeX fragmenty z poznámek
statnice-priprava.pdf   finální studijní text
```

## Pokrytí a rozsah

Závazným zdrojem pravdy je `pozadavky/detailni-pozadavky.pdf` (oficiální
požadavky SZZ, verze 28. 7. 2025). Dokument je proti němu auditovaný:
**každé požadované téma je v poznámkách obsažené** a zároveň **nic mimo
požadavky se neučí**.

Rozsah = přesně zaměření **Strojové učení**: společná matematika, společná
informatika, Základy UI (téma 1) a Strojové učení (téma 3). **Záměrně
vynecháno** (nezkouší se pro toto zaměření): Robotika a NLP, neuronové
sítě / hluboké učení, počítačové sítě, databáze, grafika a další
specializace. Detaily, výjimky a místa k procvičení viz sekce *Audit
pokrytí* přímo v PDF (Hilbertovský kalkul je jediná formální výjimka,
uvedená v požadavcích jen jako alternativa k tablu/rezoluci).

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
