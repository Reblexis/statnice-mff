# Strategie minimalni pripravy na znamku 3

Autoritativni rozsah je `pozadavky/detailni-pozadavky.pdf`, verze 28. 7. 2025. Cil neni maximalizovat znamku, ale minimalizovat cas k velmi spolehlivemu pruchodu: znamka 3, tedy aspon 12 bodu celkem, aspon 5 bodu ze spolecnych okruhu a aspon 7 bodu ze specializace. Zkouska je prehledova, proto maji nejvyssi vynos presne definice, zakladni tvrzeni, terminologie, algoritmicke kroky a jeden kratky priklad.

## 1. Bodovy rozpocet a pravdepodobnost

Struktura: 8 otazek po 0 az 3 bodech. Spolecne okruhy maji 4 otazky, specializace 4 otazky.

Minimalni prumery:

| Cast | Otazek | Maximum | Podminka | Prumer na otazku |
|---|---:|---:|---:|---:|
| Spolecna matematika + informatika | 4 | 12 | aspon 5 | 1.25 |
| Specializace: Zaklady UI + Strojove uceni | 4 | 12 | aspon 7 | 1.75 |
| Celkem | 8 | 24 | aspon 12 | 1.50 |

Vazane podminky:

- Spolecna cast je floor, ne hlavni zdroj bodu. Na pruchod staci 5/12, tedy napr. 2 + 1 + 1 + 1. Hlavni riziko je nula z pridelene otazky, ne nedostatek hlubokych dukazu.
- Specializace je vazana podminka. 7/12 znamena prumer 1.75, tedy typicky 2 + 2 + 2 + 1. Jedna nula uz vyzaduje skoro plne zvladnuti zbytku, proto je hlavni investice v specializaci.
- Celkovych 12 bodu neni samostatna rezerva: 5 + 7 = 12 presne. Pokud se ucime jen na hranici, jakakoli odchylka znamena fail. Prakticky cil musi byt vyssi: spolecne 7/12, specializace 9/12, celkem 16/24 v treninku.
- No-zeros risk je centralni. Jedna otazka za 0 v common casti jeste nemusi zabit vysledek, ale dve nuly temer ano. Ve specializaci je jedna nula velmi draha, proto kazde oficialni tema musi mit aspon "kostru odpovedi" na 1 bod.

Pracovni bodova rubrika pro minimalni pripravu:

| Stav znalosti tematu | Typicky skore | Co musi jit rict |
|---|---:|---|
| Cervena | 0 | Tema nepoznas nebo nedas definici. |
| Zluta | 1 | Definice + 2 az 4 klicove pojmy, bez spolehliveho pouziti. |
| Zelena | 2 | Definice + algoritmus/tvrzeni + typicky priklad + hlavni intuice. |
| Modra | 3 | Zelena + presne podminky, detaily, jednoducha aplikace nebo nacrt dukazu. |

Cil pro > 98 %:

- Kazde oficialni tema aspon zlute. To minimalizuje nuly u pridelovanych otazek.
- V common casti aspon 70 % velkych temat zelene, zbytek zlute. Treninkovy cil: 7/12.
- Ve specializaci aspon 85 % temat zelene, nejdulezitejsi algoritmy a modely modre. Treninkovy cil: 9/12.

Kvantifikace pravdepodobnosti: pouzijeme konzervativni model po dosazeni vyse uvedeneho stavu. Pro jednu common otazku predpokladej pravdepodobnosti skore `P(0)=0.005, P(1)=0.10, P(2)=0.60, P(3)=0.295`. Pro jednu specializacni otazku `P(0)=0.003, P(1)=0.05, P(2)=0.57, P(3)=0.377`. Nezavislost neni dokonala, ale model je uzitecny pro kalibraci.

Presnym sectenim vsech kombinaci 4 common a 4 specializacnich otazek vychazi:

- `P(common >= 5) = 99.94 %`.
- `P(specializace >= 7) = 99.09 %`.
- `P(common >= 5 a specializace >= 7 a celkem >= 12) = 99.04 %`.

To je nad 98 %, ale jen pokud jsou specializacni otazky opravdu vetsinou na 2 body. Slabsi specializacni model `P(0)=0.005, P(1)=0.08, P(2)=0.58, P(3)=0.335` dava pruchod jen asi 97.6 %. Zaver: cas navic patri nejdrive do specializace, ne do hlubsi matematiky.

## 2. Prioritizace temat a casovy plan

Doporuceny relativni casovy rozpocet pri libovolnem celkovem case:

| Cast | Podil casu | Proc |
|---|---:|---|
| Strojove uceni | 32 % | Vlastni zamereni, vysoka pravdepodobnost specializacnich otazek, potreba 7/12 ze specializace. |
| Zaklady umele inteligence | 28 % | Druha polovina specializace, mnoho samostatnych algoritmu, levne body za definice a postupy. |
| Spolecna informatika | 22 % | Jen 2 otazky, ale prakticke algoritmy a OS umi rychle dat 2 body. |
| Spolecna matematika | 18 % | Siroke, ale floor je nizky. Ucit na definice a rozpoznani, ne na dlouhe dukazy. |

Pokud mas napriklad 100 hodin, rozdel je 32 h ML, 28 h Zaklady UI, 22 h informatika, 18 h matematika. Pokud mas 40 hodin, ber stejne pomery: 13 h ML, 11 h UI, 9 h informatika, 7 h matematika.

### Strojove uceni - 32 %

Must-know na 2 az 3 body:

- Uceni s ucitelem: klasifikace vs. regrese, metriky, testovaci data, krizova validace, maximum likelihood, preuceni, regularizace L1/L2, early stopping, generalizacni chyba, prokleti dimenzionality.
- Linearni regrese: model, MSE, analyticke reseni metodou nejmensich ctvercu, role matice designu, SGD jako iterativni alternativa.
- Logisticka regrese: sigmoid, log-loss, binarni klasifikace, softmax pro vice trid, trenovani gradientne.
- Rozhodovaci stromy: uceni stromu, kriteria vetveni, entropie/Gini, prorezavani.
- SVM: linearne separabilni pripad, maximalni margin, slack pro neseparabilni tridy, jadrove funkce, multiclass strategie.
- Ensemble metody: bagging, boosting, random forest, rozdil variance vs. bias.
- Uceni bez ucitele: k-means, hierarchicke shlukovani, PCA jako projekce do hlavnich komponent.
- Statisticke testy: jednovyberovy a dvouvyberovy t-test, chi-kvadrat test dobre shody, nulova hypoteza, p-hodnota.

Skim:

- Detailni odvozovani gradientu a maticove optimalizace.
- Jemne varianty multiclass SVM.
- Presne implementacni detaily hierarchickeho shlukovani mimo zakladni linkage intuici.

Minimum odpovedi pro kazdy model: "co resi", "jak vypada model", "jak se trenuje", "kdy selhava", "jedna metrika".

### Zaklady umele inteligence - 28 %

Must-know na 2 az 3 body:

- Reseni uloh prohledavanim: formulace ulohy, stavovy prostor, stromove vs. grafove prohledavani, DFS, BFS, uniform-cost search, A*, pripustna a konzistentni heuristika.
- CSP: promenne, domeny, omezujici podminky, hranova konzistence, AC-3, MAC.
- Logicke uvazovani: CNF/DNF, DPLL, Hornovske klauzule, dopredne a zpetne retezni, rezoluce.
- Pravdepodobnostni uvazovani: uplna sdruzena distribuce, nezavislost, Bayesovo pravidlo, vyscitani, normalizace.
- Bayesovske site: konstrukce, faktorizace spolecne distribuce, exaktni odvozovani enumeraci a eliminaci promennych, aproximace Monte Carlo, zamitani, vazeni verohodnosti.
- Markovske modely: filtrace, predikce, vyhlazovani, nejpravdepodobnejsi pruchod, HMM vs. dynamicka Bayesovska sit.
- Planovani a MDP: operator, dopredne/zpetne planovani, MDP, uzitek, strategie, Bellmanova rovnice, iterace hodnot, iterace strategii, POMDP zakladne.
- Hry: minimax, alfa-beta prorezavani, veznovo dilema, Nashovo ekvilibrium, zakladni typy aukci.
- ML prehled v UI: druhy uceni, rozhodovaci stromy, regrese, SVM, Bayesovske uceni, EM, pasivni a aktivni reinforcement learning, ADP, TD, Q-uceni, SARSA.

Skim:

- Sitaucni kalkulus a problem ramce jen definicne a s jednim prikladem.
- Mechanism design jen typy aukci a motivace.
- POMDP jen definice a rozdil proti MDP.

Vysoky vynos maji diagramy stavoveho prostoru, CSP grafu, Bayesovske site, HMM a MDP. Tyto obrazky nahrazuji dlouhy text.

### Spolecna informatika - 22 %

Must-know:

- Automaty a jazyky: regularni gramatiky, DFA/NFA, regularni vyrazy, bezkontextove gramatiky, zasobnikovy automat, Turinguv stroj, nerozhodnutelnost, Chomskeho hierarchie. Cilem je umet zaradit jazyk a navrhnout automat/gramatiku v jednoduchych pripadech.
- Algoritmy a datove struktury: asymptoticka notace, P/NP, NP-tezkost a NP-uplnost, divide and conquer, Master theorem, mergesort, nasobeni dlouhych cisel, BST/AVL, trideni, dolni odhad trideni porovnanim, BFS/DFS, topologicke trideni, Dijkstra, Bellman-Ford, Jarnik, Boruvka, Ford-Fulkerson.
- Programovaci jazyky: abstrakce, zapouzdreni, polymorfismus, tridy, rozhrani, dedicnost, viditelnost, primitivni a objektove typy, generika, lambda, zdroje a vyjimky, zivotni cyklus objektu, GC, vlakna, synchronizace, vtable, bytecode, JIT/AOT, linkovani. Zvol jeden jazyk a drz se ho, idealne C# podle sily poznamek, nebo dopln Java specifika, pokud chces odpovidat v Jave.
- Architektura a OS: adresy, pamet, reprezentace cisel, instrukce pro prirazeni/podminku/cyklus/volani, privilegovany rezim, jadro, PIO, preruseni, procesy, vlakna, kontext, planovani, virtualni pamet, strankovani, soubory, race condition, kriticka sekce, zamky, aktivni/pasivni cekani.

Skim:

- Plne dukazy uzaverovych vlastnosti automatu.
- Detailni implementace AVL rotaci nad ramec definice a operaci.
- Jazykove varianty C++/Java/C# mimo zvolenou variantu. Staci vedet, ze existuji, ale do odpovedi pouzij jeden jazyk.

Levne body jsou v algoritmickych kostrach: vstup, invariant, kroky, slozitost, kdy algoritmus neplati.

### Spolecna matematika - 18 %

Must-know:

- Diferencialni a integralni pocet: posloupnosti, limity, dve policajti, rady, geometricka a harmonicka rada, limita funkce, spojitost, mezihodnoty, maximum, derivace, l'Hospital, monotonie, konvexita, Tayloruv polynom, primitivni funkce, Riemannuv integral, zakladni aplikace integralu.
- Algebra a linearni algebra: grupy, podgrupy, permutace, telesa, Gauss/Gauss-Jordan, matice, hodnost, inverze, vektorovy prostor, linearni nezavislost, baze, dimenze, Steinitz, podprostory, linearni zobrazeni, obraz, jadro, skalarni soucin, Gram-Schmidt, projekce, determinant, vlastni cisla, diagonalizace, spektralni rozklad, pozitivni definitnost, Cholesky.
- Diskretni matematika: relace, ekvivalence, castecna usporadani, funkce, permutace, kombinacni cisla, binomicka veta, inkluze a exkluze, Hallova veta.
- Grafy: zakladni pojmy, souvislost, stromy, rovinne grafy, Eulerova formule, barevnost, Menger, orientovane grafy, toky.
- Pravdepodobnost a statistika: pravdepodobnostni prostor, podminena pravdepodobnost, Bayes, nahodne veliciny, distribucni funkce/hustota, stredni hodnota, Markovova nerovnost, rozptyl, konkretni rozdeleni, zakon velkych cisel, CLV, odhady, testovani hypotez.
- Logika: syntaxe, CNF/DNF/PNF, semantika, model, splnitelnost, dusledek, skolemizace, tablo, rezoluce, kompaktnost, uplnost, rozhodnutelnost.

Skim:

- Dlouhe dukazy vet. U prehledove zkousky staci zneni, predpoklady, priklad pouziti a hlavni intuice.
- Technicke vypocty integralu a derivaci nad zakladni nacvik. Procvi jen tak, aby nehrozila nula.
- Hilbertovsky kalkul jen jako pojistka: axiomova schemata, modus ponens, dukaz jako posloupnost formuli, veta o dedukci. Tablo a rezoluce jsou pokryte a lepsi pro rychle body.

## 3. Co zamerne nestudovat

Nestudovat vubec, protoze to neni v rozsahu zamereni Strojove uceni:

- Robotika.
- Zpracovani prirozeneho jazyka.
- Databaze, SQL, webove programovani, pocitacove site.
- Pocitacova grafika a videni mimo to, co se nahodne objevi jako zdroj ML prikladu.
- Softwarove inzenyrstvi, navrhove vzory, nastroje pro vyvoj software.
- Neuronove site, hluboke uceni, perceptron, MLP, CNN, word embeddings, transformers. Tyto veci jsou v pozadavcich NLP, ne v tomto zamereni.
- RSA, FFT, vypocetni geometrie, pokrocile algoritmy mimo spolecnou informatiku.

Studovat jen minimalne:

- Dlouhe dukazy v matematice. Bezpecne je to proto, ze common floor je 5/12 a zkouska je prehledova. Definice a pouziti maji lepsi vynos.
- Plne odvozovani SVM, logisticke regrese, PCA a EM. Potrebujes princip, optimalizacni cil, vstupy/vystupy a intuici.
- Jazykove detaily vsech tri jazyku C#, C++, Java. Vyber jednu variantu a tu um dobre.
- Okrajove varianty algoritmu, pokud uz umis zakladni postup, slozitost a podminky pouziti.

Proc je to bezpecne: pruchod nevyzaduje 3 body z kazde otazky. Plan ciluje na 2 body u vetsiny pridelenych otazek a na 1 bod u slabsich. Cas straveny na treti bod z uz silneho tematu ma nizsi vynos nez cas, ktery z cerveneho tematu udela zlute.

## 4. Format studijniho dokumentu pro minimalni cas uceni

Kazde tema ma mit stejnou sablonu. Cilem je rychle najit oficialni zneni, naucit se nasi kratkou odpoved a umet se vyzkouset.

Doporucena struktura jednoho tematu:

1. `TOPIC`: oficialni tema presne podle pozadavku, verbatim, vizualne oddelene. Nemenit formulaci. To je kontrolni kotva, ze se ucis to, co se muze zkusit.
2. `LEARNING MATERIAL`: nase prepsane vysvetleni. Nema kopirovat poznamky, ma byt kratsi, jasnejsi a orientovane na odpoved u zkousky.
3. `MINIMALNI ODPOVED ZA 1 BOD`: 3 az 5 vet nebo odrazek. Definice a terminologie.
4. `ODPOVED ZA 2 BODY`: definice + hlavni veta/algoritmus + priklad + intuice.
5. `BONUS NA 3 BODY`: jen pokud je levny. Podminky, okrajovy pripad, nacrt dukazu, slozitost nebo jeden vypocet.
6. `AKTIVNI RECALL`: 3 az 6 otazek bez odpovedi. Napr. "Kdy je heuristika konzistentni?", "Co faktorizuje Bayesovska sit?", "Proc L2 regularizace zmensuje vahy?"
7. `TYPICKA PAST`: jedna veta. Napr. "Nezamenuj generativni Bayesovsky model s logistickou regresi."

Uroven detailu:

- Jedna oficialni podotazka ma typicky zabrat 0.5 az 1.5 strany, ne vice.
- Definice musi byt presne, ale vysvetleni ma byt lidske. Ne "encyklopedie", ale odpoved na tabuli.
- Kazdy algoritmus: vstup, vystup, kroky, invariant nebo intuice, slozitost, kdy funguje.
- Kazdy model v ML: uloha, predpoklady, modelova rovnice, loss/trenovani, metrika, selhani.
- Kazda matematicka veta: zneni, predpoklady, priklad pouziti, jen kratky dukazovy napad.

TikZ a obrazky pouzivat jen tam, kde usetri cas:

- Prohledavani: maly strom/graf s poradim expanze pro BFS, DFS, UCS, A*.
- CSP: graf promennych a skrtani domen pri AC-3.
- Bayesovska sit: 4 az 6 uzlu a pod ni faktorizace distribuce.
- HMM/DBN: retezec skrytych stavu a pozorovani.
- MDP: 3 stavy se sipkami, odmenami a jednou Bellmanovou aktualizaci.
- Minimax: maly strom s hodnotami a alfa-beta skrty.
- Linearni/logisticka regrese: bodovy graf s primkou, sigmoid krivka.
- SVM: dve tridy, margin, support vectors, slack body.
- Rozhodovaci strom: 2 az 3 vnitrni uzly, listy, prorezavani.
- k-means/PCA: body, centroidy, hlavni osa projekce.
- OS: virtualni adresa rozdelena na cislo stranky a offset, preklad pres tabulku.
- Automaty: DFA/NFA a zasobnikovy automat jen pro archetypicke jazyky.

Kdy diagram nema cenu:

- Pokud jen dekoruje definici.
- Pokud by zabral vic casu nez tri vety.
- Pokud by vyzadoval presnost, ktera se nezkousi.
- Pokud opakuje stejny typ obrazku uz potreti.

Jak drzet dokument lean:

- V kazdem tematu explicitne oznacit `CUT`: veci, ktere se pro znamku 3 neuci.
- Neprepisovat dlouhe dukazy z poznamek, jen odkaz nebo jednovetou intuici.
- Nepouzivat vice nez jeden priklad na tema, pokud druhy nepridava novy typ chyby.
- Udrzet konzistentni jazyk: "definice", "intuice", "algoritmus", "pozor".
- Na zacatek kazde casti dat checklist se stavem cervena/zluta/zelena/modra.

Nejrychlejsi ucici cyklus:

1. Precist oficialni tema.
2. Zakryt material a rict 1bodovou odpoved nahlas.
3. Doplnit na 2 body: algoritmus/tvrzeni/priklad.
4. Vyresit jednu miniotazku nebo jeden diagram z pameti.
5. Oznacit stav tematu. Cervena temata maji prednost pred modrenim zelenych.

## 5. Rizika pro > 98 % a levne mitigace

Riziko: specializace spadne pod 7/12.

Mitigace: Neucit ML a UI jako dve velke kapitoly, ale jako seznam 18 odpovednich karet. Kazda karta musi mit 2bodovou kostru. Pred zkouskou udelat 2 simulace po 4 specializacnich otazkach. Pokud simulace nema aspon 9/12, dalsi cas jde jen do specializace.

Riziko: nula z nahodne prideleného common tematu.

Mitigace: Pro kazde z 10 common temat mit 1bodovou kartu. To je levnejsi nez se ucit analyzu nebo linearni algebru do hloubky. Minimalni karta: definice, 5 klicovych pojmu, jeden priklad.

Riziko: prakticka dovednost bez nacviku.

Mitigace: Jednou nacvicit sedm znamych slabych mist: derivacni pravidla, substituce, per partes, odhad souctu rady pres integral, vypocet determinantu, preklad konstrukci do instrukci a zpet, PIO obsluha zarizeni. Ne do mistrovstvi, jen aby odpoved nebyla prazdna.

Riziko: jazykova varianta v programovacich jazycich.

Mitigace: Zvolit jednu variantu predem. Pokud C#, pouzit silu poznamek. Pokud Java, doplnit moduly, interfaces/default methods, boxing, try-with-resources, generika, effectively final capture. Nemichat jazyky v odpovedi.

Riziko: preuceni detailu misto pokryti.

Mitigace: Zakaz ucit 3bodovy detail u tematu, ktere uz je zelene, dokud existuje cervene tema. To je nejdulezitejsi casove pravidlo.

Riziko: zamena rozsahu specializace.

Mitigace: V dokumentu jasne oznacit, ze pro zamereni Strojove uceni se neuci Robotika ani NLP. Neuralni site a hluboke uceni nepatri do teto pripravy, pokud nejsou jen okrajovym prikladem.

Riziko: stres snizi vybaveni odpovedi.

Mitigace: U kazdeho tematu mit prvni vetu odpovedi naucenou doslova. Prvni veta nastavi terminologii a casto staci k rozjeti 1bodove odpovedi.

Minimalni kontrola pred zkouskou:

- Common: 10/10 velkych temat aspon zlute, 7/10 zelene.
- Specializace: 18/18 karet aspon zlute, 15/18 zelene, nejdulezitejsich 6 modre.
- Simulace: ze 3 nahodnych sad po 8 otazkach zadna pod 14/24, zadna specializace pod 8/12, zadna common cast pod 6/12.
- Pokud neco selze, neopravovat vse. Opravit nejlevnejsi cervene nebo zlute tema, ktere muze pridat 1 bod.
