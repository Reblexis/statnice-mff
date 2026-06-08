# Kontrola pokryti notes-ipp

Audit porovnal cele soubory z `notes-ipp/statnice` s odpovidajicimi sekcemi v `src/sections`.
Cilem bylo doplnit chybejici zkouskove pojmy minimalne do bonusove urovne, bez rozepisovani
dukazu a bez pridavani pouhych prikladovych jmen.

## Spolecna matematika

### Pridano

- Analyza: povrch rotacni plochy a integralni kriterium konvergence rad.
- Algebra a linearni algebra: grupa, abelovska grupa, teleso, konecna telesa jako mocniny
  prvocisel, permutace, cykly, transpozice, znamenko permutace, souradnice vzhledem k bazi,
  matice prechodu, ortogonalni matice, determinant jako orientovany objem, multiplikativnost
  determinantu a stopa jako soucet vlastnich cisel.
- Diskretni matematika: pocet prostych funkci, pocet bijekci, minimalni a maximalni prvky
  v CUM, vztah vysky a sirky pres soucin aspon `|X|`.
- Grafy: slaba souvislost orientovaneho grafu, eulerovske grafy neorientovane i orientovane,
  Kuratowskiho veta pres deleni `K_5` a `K_{3,3}`, odhad `2v-4` pro rovinne grafy bez
  trojuhelniku.
- Pravdepodobnost a statistika: seznam konkretnich rozdeleni, bodove odhady, nestrannost,
  konzistence, bias, MSE odhadu, metoda momentu, MLE, konfidence a p-hodnota.
- Logika: PNF, Horn-SAT, konzervativni extenze, tablo spornost, korektnost a uplnost
  dokazovacich systemu, Godelova nekompletnost pro silnou aritmetiku.

### Preskoceno

- Epsilon-delta definice, aritmetika limit, detailni vzorce Riemannovych sum, plne odvozovani
  Taylorovy rady a vypoctove postupy substituce/per-partes: jsou bud uz obsazene jadrove pojmy,
  nebo jde o dlouhe derivace a nacvik vypoctu.
- Plne dukazy vet o Hallovi, Eulerove formule, Mengerovi, CLV, kompaktnosti a nekompletnosti:
  majitel chtel pojmy, ne dukazy.
- Konkretni aplikacni priklady jako problem satnarky jsou ponechane jen jako jmeno aplikace,
  ne jako detailni vypocet.

## Spolecna informatika

### Pridano

- Automaty a jazyky: pumping lemma pro regularni jazyky, Myhill-Nerode, pumping lemma pro CFL,
  Chomskeho normalni tvar, PDA prijimani koncovym stavem nebo prazdnym zasobnikem, uzavrenost
  regularnich jazyku a neuzavrenost CFL na prunik.
- Algoritmy: Master theorem, Karacuba, vlastnosti polynomialnich prevodu, konkretni NP-uplne
  problemy, hloubka AVL, dolni mez porovnavaciho trideni.
- Programovaci jazyky: diamantovy problem, `ref`/`out`/`in`, imutabilita, RAII, `using` jako
  `try/finally`, vzory adapter, decorator, factory a visitor.
- Architektura a OS: Harvard vs. von Neumann, dvojkovy doplnek, float reprezentace, endianita,
  zarovnani struktur, syscall, DMA, MMU a page fault, stavy vlaken, planovaci algoritmy,
  semafor, mutex a barrier.

### Preskoceno

- Identifikatory a jmena z prikladu jako `Kachna`, `Fraction`, `Apple`, `Intel`, konkretni
  historie procesoru a ukazkove radky kodu: pouze ilustracni priklady.
- Detailni konstrukce automatu, gramatik a prevodu SAT mezi variantami: prilis dlouhe,
  v materialu zustala zkouskova idea a nazvy metod.
- Implementacni ukoly typu "nacvicit instrukce procesoru" a porty konkretniho zarizeni:
  jde o cviceni, ne o samostatny pojem k doplneni.

## Zaklady umele inteligence

### Pridano

- Prohledavani: typy agentu, atomicke/faktorizovane/strukturovane stavy, greedy best-first.
- CSP: forward checking, prevod n-arnich podminek na binarni, rozdil FC a AC.
- Logicke uvazovani: implementace dopredneho retezeni pres citace predpokladu, vyhoda zpetneho
  retezeni pro cilene dotazy.
- Pravdepodobnostni uvazovani: chain rule, naivni Bayes, likelihood weighting.
- Reprezentace znalosti: Markovuv predpoklad, stacionarita, forward, forward-backward
  a Viterbiho algoritmus.
- Planovani: predpoklad uzavreneho sveta, fluenty a rigidni atomy, akce jako instanciovany
  operator, relevance akce pro cil, possibility a successor-state axiomy.
- MDP: konecnost diskontovaneho uzitku, nezavislost optimalni strategie na pocatecnim stavu,
  policy evaluation a policy improvement.
- Hry: ciste a smisene strategie, dominantni strategie, Pareto optimalita, Vickreyho aukce
  a VCG mechanismus.
- RL prehled: primy odhad utility, TD update, nutnost exploration, q-hodnoty bez prechodoveho modelu.

### Preskoceno

- Story priklady typu vloupani, John/Mary, Lloydova patnactka a konkretni domenove akce:
  jsou ilustrace, ne samostatne pojmy.
- Detailni algebra odvozeni filtering/smoothing rovnic a expected minimax pro POMDP:
  nad ramec kratke zkouskove odpovedi.
- Dlouhe ukazky successor-state axiomu: doplnen byl pojem a ucel, ne formalni priklad.

## Strojove uceni

### Pridano

- Supervised learning: NLL, ROC, AUC, senzitivita, specificita, validacni sada pro hyperparametry,
  filter a wrapper vyber priznaku.
- kNN: vahovani sousedu uniformne, inverzni vzdalenosti a softmaxem, `p`-normy.
- Linearni regrese: batch, online a minibatch gradient descent, bias jako sloupec jednicek.
- Logisticka regrese: invariance softmaxu k pricitani konstanty, sigmoid jako specialni softmax,
  konvexni rozhodovaci oblasti.
- Rozhodovaci stromy: CART, squared error pro regresi, predikce prumerem, reduced error pruning.
- SVM: dualni tvar, predikce pres kernel, slack promenne, hinge loss, interpretace `C`,
  RBF kernel.
- Ensemble: AdaBoost vahy klasifikatoru a hlasovani/prumerovani nahodneho lesa.
- Statisticke testy: stupne volnosti u t-testu, dvouvyberovy a parovy t-test, stupne volnosti
  chi-kvadrat testu.
- Unsupervised learning: k-means loss a lokalni optimum, aglomerativni a divisivni shlukovani,
  dendrogram, SVD a PCA pres centrovana data a prvni sloupce `V`.

### Preskoceno

- Obrazky a externi odkazy z poznamek: nejsou koncepty, navic by bloating material.
- Detailni odvozeni gradientu, Lagrangianu, KKT a SMO: pro zkouskovy tahak staci vysledek
  a interpretace.
- Konkretni priklady pouziti PCA, k-means a EM: ponechany obecny ucel, vynechany pribehy.
- Mimo rozsah zamereni Strojove uceni nebylo z teto casti pridavano nic navic mimo uvedene
  ML okruhy.

## Shrnuti

Do ctyr sekci byly doplneny chybejici zkouskove pojmy z poznamek tak, aby se objevily aspon
v bonusove urovni odpovidajiciho tematu. Preskocene polozky jsou zamerne: prikladova jmena,
dlouhe dukazy, vypoctove drilly, obrazky, externi odkazy a podrobna odvozeni.
