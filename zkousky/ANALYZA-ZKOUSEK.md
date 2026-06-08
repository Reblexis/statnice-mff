# Analýza minulých státnic (2023-2026)

Podklad: 10 reálných zadání z termínů jaro/léto/podzim 2023 až jaro 2026
(`zkousky/zkouska-*.pdf`). Cíl: zjistit, jak zkouška reálně vypadá, a podle toho
vyladit přípravu na minimum času pro jisté složení na 3.

## Formát zkoušky (potvrzeno ze zadání)

- Každý termín = velká **sada otázek pro všechna zaměření**. Otázka je označena
  okruhem: `(společné okruhy)` nebo `(specializace UI-SU)` apod. Pro zaměření
  Strojové učení je tvoje značka **UI-SU** (a sdílené `UI-SU, UI-ZPJ`).
- Ty dostaneš **8 otázek**: 2 společná matematika, 2 společná informatika,
  4 specializace (Základy UI + Strojové učení). Každá otázka za **0-3 body**.
- Každá otázka má **3-4 podotázky**. Skoro vždy: (1) přesná definice / znění věty,
  (2) použití / výpočet / „rozhodněte a zdůvodněte“, (3) těžší výpočet nebo okrajový
  případ. Body se dávají po částech (parciální kredit).

## Nejdůležitější zjištění: DEFINICE SE ZKOUŠEJÍ

Slovo **„Definujte“ se v 10 zadáních objevuje 68×**, plus „Zformulujte větu“,
„Uveďte definice“, „Formulujte“. Skoro každá otázka **začíná přesnou definicí nebo
zněním věty**. To jsou nejlevnější a nejjistější body.

Odpověď na otázku „nevadí, že chybí přesné definice (posloupnost apod.)?“:
**Vadí.** Neformální popis na „Definujte X“ nestačí. Proto v učivu míří **kostra na
1 bod = přesná definice** daného pojmu. Příklady reálně zadaných definic v rozsahu:
geometrická řada, primitivní funkce, (ne)spojitost funkce, ekvivalence (podmínky),
podobné matice (a co zachovávají), Steinitzova věta, barevnost grafu, silná
souvislost a kondenzace, eulerovský graf, P a NP, redukce, NP-úplnost, Mergesort
(pseudokód), Bayesovská síť, binární CSP (vstup/výstup), HMM, maximálně věrohodná
hypotéza, chybová funkce s L2, evaluační metriky (accuracy/recall/precision).

## Společné okruhy (matematika + informatika): definice + reálný výpočet

Pozdější podotázky často chtějí **skutečný výpočet nebo program**:
- analýza: spočítat obsah přes integrál, najít minimum přes derivaci, vyšetřit spojitost;
- lineární algebra: diagonalizace, řešení soustav, skalární součin;
- grafy: barevnost, souvislost, eulerovskost, toky;
- informatika: sestrojit/popsat automat, napsat třídu (parsování binárního souboru),
  ovladač zařízení, správce paměti, složitost.

Strategie: stačí 5/12. Vezmi jistou definici/znění věty (1 b) u každé společné
otázky a u některých dotáhni jeden výpočet na 2 b. Nehnat se za 3. bodem.

## Specializace UI-SU: spíš pochopení než počítání

Specializační otázky jsou výrazně **konceptuální**: „popište, jak funguje“,
„vysvětlete“, **„nemusíte nic počítat“**, „zakreslete přibližně“. Příklad (SVM 2024):
popiš princip a trénink, nakresli přibližnou hranici, vysvětli vliv přidaného bodu,
kdy pomůže RBF jádro. To přesně sedí na naše konceptuální učivo. Sem dej těžiště
(potřebuješ 7/12).

Časté specializační okruhy (vysoký výnos): lineární/logistická regrese
(+ regularizace, nejmenší čtverce) velmi často, shlukování (3×), evaluační
metriky / matice záměn (3×), SVM, PCA, Bayesovské sítě, rozhodovací stromy,
CSP a prohledávání, HMM, kombinace modelů, t-test, minimax.

## Co z toho plyne pro přípravu (min. čas, jistá 3)

1. **U každého tématu umět přesnou definici / znění hlavní věty zpaměti** = kostra na
   1 bod a nejlevnější body. Tohle je teď v učivu zdůrazněné.
2. **Specializaci umět konceptuálně do hloubky** (popsat princip, trénink, chování,
   nakreslit) - tam padá 7/12 a otázky jsou konceptuální.
3. **U společné matematiky/informatiky stačí breadth**: definice + jeden výpočet.
   Natrénovat pár typových výpočtů (integrál, derivace/extrém, diagonalizace,
   sestrojení automatu) jen tak, aby odpověď nebyla prázdná.
4. **Past:** nepodcenit, že i „přehledová“ zkouška chce skutečně přesné formulace.
   Spíš se nauč míň témat pořádně (definice + princip) než všechno mlhavě.
