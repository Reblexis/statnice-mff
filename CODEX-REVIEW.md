# Nezavisla kontrola pokryti pozadavku SZZ

Kontroloval jsem oba PDF dokumenty ve slozce `pozadavky/` pres `pdftotext` a porovnal je proti zdrojovym poznamkam `notes-ipp/statnice/*.md`. Vysledek: poznamky pokryvaji strukturu pozadavku velmi tesne. Nenasel jsem zadne cele povinne tema, ktere by v poznamkach chybelo. Nasel jsem ale nekolik mist, kde audit musi byt opatrnejsi: nektere body jsou v poznamkach jen jako "nacvicit" a Hilbertovsky kalkul je v jednom PDF formulovan mene alternativne nez v druhem.

## A. Chybejici nebo slaba mista

1. **Hilbertovsky kalkul - formalni nejistota podle formulace PDF.**
   - `SZZ_strojove_uceni.pdf` uvadi u dokazatelnosti "dokazovaci systemy (tablo, rezoluce, Hilbertovsky kalkul)".
   - `mff_statnice_informatika_ai_strojove_uceni_pozadavky_predmety.pdf` uvadi "tablo, rezoluce nebo Hilbertovsky kalkul".
   - V poznamkach je dokazatelnost pokryta pres formalni dukaz, zamitnuti, rezoluci a tablo: `notes-ipp/statnice/spolecna-matematika.md:1249`, `:1271`, `:1329`, `:1336`.
   - Slovo `Hilbert` se v poznamkach nevyskytuje. Pokud zkousejici bere druhou formulaci jako seznam prikladu a ne alternativ, je to jedina skutecna obsahova mezera.

2. **PIO obsluha zarizeni - pouze vyzva k nacviceni.**
   - Pozadavky chteji pro zadane adresy a porty implementovat programem rizenou obsluhu zarizeni.
   - Poznamky maji definice role radice/ovladace a OS, ale samotnou implementaci nechavaji jako "implementaci nacvicit": `notes-ipp/statnice/spolecna-informatika.md:1045`.
   - Toto je stejneho typu jako derivace, per-partes nebo prevod konstrukci do instrukci: neni to chybejici definice, ale je to prakticka dovednost potrebna ke zkousce.

3. **Prevod konstrukci vyssiho jazyka do instrukci a z instrukci zpet - pouze "nacvicit".**
   - Pozadavky chteji pri konkretni instrukcni sade implementovat prirazeni, podminku, cyklus a volani funkce a opacne poznat konstrukci z instrukci.
   - Poznamky maji oba body doslova, ale bez postupu: `notes-ipp/statnice/spolecna-informatika.md:1012`, `:1014`.
   - Audit to spravne uvadi jako vypocetni dovednost, ne jako definicni mezeru.

4. **Analyza - nekolik vypocetnich technik je pouze k procviceni.**
   - Derivacni pravidla jsou uvedena jako tema, ale poznamky odkazuji na tabulku/prakticky nacvik: `notes-ipp/statnice/spolecna-matematika.md:95`.
   - Substituce a per-partes jsou zmineny, per-partes ma vzorec, ale postup je oznacen k nastudovani: `notes-ipp/statnice/spolecna-matematika.md:129`, `:135`, `:136`.
   - Odhad souctu rady pres integral ma nerovnost, ale presny postup je k nacviceni: `notes-ipp/statnice/spolecna-matematika.md:153`, `:157`.

5. **Determinant - prakticky vypocet je k nacviceni.**
   - Poznamky pokryvaji definici, vlastnosti, Laplaceuv rozvoj a geometrickou interpretaci v oddilu determinanty.
   - Vlastni vypocet determinantu je oznacen jako dovednost k nacviceni v buildu/auditu, nikoli jako plne rozepsany postup.

## B. Chyby nebo nepresnosti v `src/audit.tex`

1. **Puvodni audit tvrdil "sest mist" k vlastnimu procviceni, ale chybi PIO implementace.**
   - Minimalni korekce je pocitat sedm mist: 4 z analyzy/linearni algebry, 2 z instrukci a 1 z PIO.

2. **Formulace Hilbertovskeho kalkulu byla prilis silna.**
   - V jednom PDF je Hilbertovsky kalkul formulovan alternativne, ve druhem jako soucast zavorky se tremi systemy. Audit by mel rict, ze poznamky pokryvaji tablo a rezoluci, ale Hilbertovsky kalkul sam o sobe v poznamkach neni.

3. **Souhrn "kazde pozadovane tema je obsazene" je prakticky pravdivy na urovni okruhu, ale neni dost skepticky.**
   - Presnejsi je: vsechny okruhy a podtemata jsou dohledatelne, ale vyse uvedene prakticke dovednosti a Hilbertovsky kalkul nejsou v poznamkach rozpracovane.

## C. Potvrzeni pokryti podle okruhu

### I/1 Zaklady diferencialniho a integralniho poctu

Pokryto. Posloupnosti a limity, veta o dvou policajtech, rady, funkce, spojitost, derivace, l'Hospital, prubeh funkce, Tayloruv polynom, Newtonuv a Riemannuv integral, aplikace integralu jsou v `notes-ipp/statnice/spolecna-matematika.md:3-166`. Slabe jen vypocetni techniky uvedene v casti A.

### I/2 Algebra a linearni algebra

Pokryto. Grupy, podgrupy, permutace, telesa vcetne konecnych teles jsou v `spolecna-matematika.md:170-198`. Soustavy, Gauss a Gauss-Jordan jsou v `:200-254`. Vektorove prostory, Steinitz, baze, dimenze, podprostory a maticove prostory jsou v `:256-324`. Linearni zobrazeni, obraz, jadro a isomorfismus jsou v `:325-359`. Skalarni soucin, nerovnosti, Fourierovy koeficienty, Gram-Schmidt a ortogonalni projekce jsou v `:361-421`. Determinanty, vlastni cisla, diagonalizace, spektralni rozklad, pozitivni definitnost a Cholesky jsou v `:423-506`.

### I/3 Diskretni matematika

Pokryto. Relace, ekvivalence, usporadani vcetne vysky/sirky, funkce, permutace, kombinacni cisla, inkluze a exkluze, satnarka, Eulerova funkce, surjekce a Hallova veta jsou v `spolecna-matematika.md:509-726`. Algoritmicky aspekt Hallovy vety je uveden pres polynomicky algoritmus pro maximalni parovani v `:724-726`.

### I/4 Teorie grafu

Pokryto. Zakladni pojmy, priklady, souvislost, stromy, rovinne grafy, Eulerova formule, barevnost, Mengerovy vety, orientovane grafy a toky vcetne existence maximalniho toku a Ford-Fulkersona jsou v `spolecna-matematika.md:728-966`.

### I/5 Pravdepodobnost a statistika

Pokryto. Pravdepodobnostni prostor, jevy, nezavislost, podminena pravdepodobnost, Bayesuv vzorec, nahodne veliciny, distribucni funkce, hustota, stredni hodnota, Markovova nerovnost, rozptyl souctu, konkretni rozdeleni, zakony velkych cisel, CLV, bodove a intervalove odhady a testovani hypotez jsou v `spolecna-matematika.md:969-1174`.

### I/6 Logika

Pokryto s vyjimkou Hilbertovskeho kalkulu. Syntaxe, CNF/DNF/PNF, SAT/DPLL, semantika, modely, splnitelnost, dusledek, extenze teorii, konzervativnost, skolemizace, formalni dukaz, rezoluce, tablo, kompaktnost, uplnost a rozhodnutelnost jsou v `spolecna-matematika.md:1177-1426`. Hilbertovsky kalkul neni v poznamkach dohledatelny.

### II/1 Automaty a jazyky

Pokryto. Regularni jazyky, DFA/NFA, regularni vyrazy, bezkontextove gramatiky, PDA, rekurzivne spocetne jazyky, Turinguv stroj, nerozhodnutelnost a Chomskeho hierarchie jsou v `notes-ipp/statnice/spolecna-informatika.md:3-312`.

### II/2 Algoritmy a datove struktury

Pokryto. Slozitost, P/NP, prevoditelnost, NP-uplnost, rozdel a panuj, Master theorem, Mergesort, nasobeni dlouhych cisel, BST/AVL, trideni, dolni odhad, BFS/DFS, topologicke trideni, Dijkstra, Bellman-Ford, Jarnik, Boruvka a Ford-Fulkerson jsou v `spolecna-informatika.md:315-617`.

### II/3 Programovaci jazyky

Pokryto pro prakticky smer poznamek, primarne C# s presahy do C++ a Java. Abstrakce, zapouzdreni, polymorfismus, tridy, rozhrani, viditelnost, typy, reference, boxing, generika, templates, funkce, lambdy, RAII/using, vyjimky, alokace, destrukce, reference counting, GC, vlakna, synchronizace, VMT, bytecode, JIT/AOT, oddeleny preklad, linkovani a knihovny jsou v `spolecna-informatika.md:620-946`. Pokud si student u zkousky zvoli Javu, je vhodne doplnit jazykove detaily Javy z predmetu, protoze poznamky jsou zretelne nejsilnejsi pro C#.

### II/4 Architektura pocitacu a OS

Pokryto s praktickymi dovednostmi k nacviceni. Architektura, reprezentace cisel a dat, adresy, instrukcni sada, rezimy procesoru, jadro, PIO, preruseni, procesy, vlakna, planovani, virtualni pamet, strankovani, soubory, race conditions, kriticka sekce, vzajemne vylouceni, zamky a aktivni/pasivni cekani jsou v `spolecna-informatika.md:969-1226`. Slabe jsou jen prakticke ulohy uvedene v casti A.

### III Zaklady umele inteligence

Pokryto. Prohledavani, stromove/grafove hledani, DFS/BFS/UCS, A*, heuristiky, CSP, AC-3, MAC, DPLL, Hornovy klauzule, rezoluce, pravdepodobnostni uvazovani, Bayesovske site, enumerace, eliminace promennych, Monte Carlo, rejection sampling, likelihood weighting, situacni kalkulus, problem ramce, HMM/DBN, planovani, MDP, Bellman, value/policy iteration, POMDP, minimax, alfa-beta, Nash, aukce a prehled ML/RL jsou v `notes-ipp/statnice/zaklady-umele-inteligence.md:3-631`.

### IV Strojove uceni

Pokryto. Uceni s ucitelem, klasifikace, regrese, metriky, testovaci data, krizova validace, maximum likelihood, overfitting, regularizace, early stopping, prokleti dimenzionality, kNN, linearni regrese, SGD, logisticka regrese, sigmoid, softmax, rozhodovaci stromy, prorezavani, SVM vcetne neseparabilniho pripadu a jader, multiclass, bagging, boosting, random forest, t-testy, chi-kvadrat, k-means, hierarchicke shlukovani a PCA jsou v `notes-ipp/statnice/strojove-uceni.md:3-491`.
