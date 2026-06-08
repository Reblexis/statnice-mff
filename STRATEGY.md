# Strategie: minimum času k jisté trojce (>98 %)

Syntéza mé analýzy a nezávislé analýzy Codexu (viz `STRATEGY-CODEX.md`). Obě se
shodují. Cíl není nejlepší známka, ale **nejméně času k velmi spolehlivému průchodu**
(známka 3).

## Bodový rozpočet (proč to funguje)

8 otázek po 0-3 bodech. Průchod = aspoň 12 bodů celkem **a** aspoň 5 ze společných
okruhů (4 otázky) **a** aspoň 7 ze specializace (4 otázky).

- Společné: stačí průměr 1,25/otázku (5/12). Floor, ne hlavní zdroj bodů.
- Specializace: průměr 1,75/otázku (7/12). **Vázaná podmínka = sem dej nejvíc času.**
- 5+7=12 nemá rezervu, proto trénuj na vyšší cíl: společné 7/12, specializace 9/12,
  celkem ~16/24.
- **Hlavní riziko je nula z přidělené otázky**, ne chybějící důkazy. Každé oficiální
  téma proto musí mít aspoň „kostru odpovědi na 1 bod“.

Po dosažení cílového stavu vychází P(průchod) ~99 % (citlivé hlavně na kvalitu
specializace - proto čas navíc patří tam).

## Rubrika zvládnutí (sebehodnocení)

- červená (0): neumím ani definici
- žlutá (1): definice + pár pojmů
- zelená (2): definice + algoritmus/věta + příklad + intuice  <- cílová úroveň
- modrá (3): zelená + přesné podmínky/detail (jen u nejdůležitějších)

Cíl: každé téma aspoň žlutě; společné ~70 % zeleně; specializace ~85 % zeleně,
nejdůležitější modře.

## Rozdělení času

| Část | Podíl | Proč |
|---|---:|---|
| Strojové učení | 32 % | vlastní zaměření, vázaná podmínka 7/12 |
| Základy UI | 28 % | druhá půlka specializace, levné body za postupy |
| Společná informatika | 22 % | jen 2 otázky, ale algoritmy/OS dají body rychle |
| Společná matematika | 18 % | nízký floor; učit na definice a rozpoznání, ne důkazy |

Celkem ~60 % specializace, ~40 % společné.

## Co cíleně NEdělat (bezpečné vynechání)

Mimo rozsah (vůbec): robotika, NLP, neuronové sítě a hluboké učení, databáze, sítě,
grafika, softwarové inženýrství, RSA/FFT, výpočetní geometrie.
Minimalizovat: dlouhé důkazy, plná odvození (SVM/logreg/PCA/EM), jazykové varianty
mimo zvolený jazyk, okrajové varianty algoritmů.
Důvod: průchod nevyžaduje 3 body z každé otázky. Třetí bod z už silného tématu má
nižší výnos než udělat z červeného tématu žluté.

## Formát dokumentu (pro nejrychlejší učení)

Každé téma podle jednotné šablony:
1. **TÉMA** = oficiální požadavek doslova (kotva, co se může zkoušet).
2. **Učivo** = naše přepsané, jasné a intuitivní vysvětlení (ne kopie poznámek).
3. **Intuice** (1-2 věty) + **obrázek**, kde pomůže (viz seznam v `STRATEGY-CODEX.md`).
4. **Odpověď podle bodů**: co stačí na 1 / 2 / 3 body.
5. **Vyzkoušej se**: pár otázek pro aktivní vybavování.
6. **Pozor (past)**: jedna typická chyba.
Plus štítek priority a cílové úrovně. Specializace = plná šablona; společná
matematika = lehčí verze (definice + odpověď na body), ať je dokument lean.

Ukázku formátu viz `src/pilot.tex` / `src/pilot.pdf` (SVM a Toky v sítích).
