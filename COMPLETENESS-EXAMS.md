# Completeness audit against real exams for UI-SU

Scope: UI-SU / Machine Learning student. I counted modern `(společné okruhy)`,
`(specializace UI-SU)` and shared UI-SU questions. For the 2019-2022 files, which
predate the UI-SU specialization, I counted only questions whose topic is in the
current UI-SU common scope: common mathematics, automata and languages, algorithms
and data structures, programming languages, computer architecture and operating
systems. I ignored old specialization material and current out-of-scope areas:
databases/SQL, networking, graphics, compilers beyond automata, coding theory,
optimization/LP, computational geometry, advanced set theory, MA2/metric spaces,
web and software engineering.

Verdict after fixes: the materials are now sufficient to answer all relevant
questions below from the included sources alone. The remaining risk is not
missing theory, but ordinary exam execution: doing arithmetic carefully and
recognizing which template applies.

## zkouska-2019-jaro.pdf

- Q1 Automaty - COVERED. Closure of regular languages under intersection, reversal and length modulo constraints is in `spolecna-informatika`.
- Q2 Třídění - COVERED. BST sorting, comparison lower bound and linear-time bucket/counting style sorting for bounded pairs are in `spolecna-informatika`.
- Q4 Programovací jazyky - COVERED. OO expression-tree design, interfaces, exceptions and shared-subexpression representation are derivable from `spolecna-informatika`.
- Q5 Procesy, vlákna, plánování - COVERED. Process/thread states, scheduler transitions and processor limits are in `spolecna-informatika`.
- Q17 Funkce - COVERED. Derivatives, limits and graph-shape reasoning are in `spolecna-matematika`.
- Q18 Riemannův integrál - COVERED. Upper/lower sums, Riemann integral and piecewise integration are in `spolecna-matematika`.
- Q20 Lineární zobrazení - COVERED. Linear maps, matrices, rank, invertibility and surjectivity are in `spolecna-matematika`.
- Q21 Pozitivně definitní matice - COVERED. Positive definiteness, pivot/eigenvalue criteria and Cholesky are in `spolecna-matematika`.
- Q22 Algebraická tělesa - COVERED. Fields, characteristic, finite fields and regularity of matrices are in `spolecna-matematika`.
- Q23 Princip inkluze a exkluze - COVERED. Inclusion-exclusion for finite sets is in `spolecna-matematika`.
- Q24 Grafy - COVERED. Planar graphs, low-degree vertices and induced forests follow from the graph section in `spolecna-matematika`.
- Q25 Logika - COVERED. Completeness of theories, models and skolemization/conservative extensions are in `spolecna-matematika`.

Ignored as out of current scope: Q3 databases, Q6 routing, Q7 linear programming, Q8-Q10 NLP, Q11-Q13 graphics, Q14-Q16 web/databases.

## zkouska-2019-leto.pdf

- Q1 Automaty a gramatiky - COVERED. CFG/PDA conversion, nonregularity tools and Chomsky hierarchy are in `spolecna-informatika`.
- Q2 Algoritmy a datové struktury - COVERED. Decision problems, P, NP, NP-completeness and examples are in `spolecna-informatika`.
- Q4 Programování - COVERED. C#/Java/C++ object modeling, interfaces and multiple-inheritance tradeoffs are in `spolecna-informatika`.
- Q5 Architektury - COVERED. Data alignment, endianity, binary files and byte-level parsing are in `spolecna-informatika`.
- Q14 Základy teorie informace - COVERED. Entropy and entropy under changed support/probabilities are in `spolecna-matematika`.
- Q21 Synchronizace na multiprocesorech - COVERED. Spinlocks, race conditions and atomic read-modify-write primitives are in `spolecna-informatika`.
- Q22 Interní struktura systémů souborů - COVERED. File-system block representation, FAT/inode concepts and extents are derivable from `spolecna-informatika`.
- Q23 Princip mechanismu RPC - COVERED. Interfaces, generated stubs, serialization and server threading are covered by programming/OS material in `spolecna-informatika`.
- Q30 Vektory - COVERED. Span, orthogonality, scalar product and matrix of a linear map are in `spolecna-matematika`.
- Q31 Grupy - COVERED. Groups, matrices, determinant and inverse are in `spolecna-matematika`.
- Q32 Matice - COVERED. Determinant, similarity and quadratic forms are in `spolecna-matematika`.
- Q33 Posloupnosti a limity - COVERED. Definition and computation of sequence limits are in `spolecna-matematika`.
- Q35 Plocha a objem - COVERED. Integral area and volume by rotation are in `spolecna-matematika`.
- Q36 Grafy - COVERED. Vertex/edge connectivity and counterexample reasoning are in `spolecna-matematika`.
- Q38 Logika - COVERED. Independence in a theory and propositional models are in `spolecna-matematika`.

Ignored as out of current scope: Q3 databases, Q6 networking, Q7 optimization/LP, Q8 compilers beyond automata, Q9 coding theory, Q10 set theory beyond basics, Q11 edge-coloring specialization, Q12-Q13 NLP, Q15-Q17 graphics, Q18-Q20 networking, Q24-Q29 databases/web/software engineering/testing, Q34 MA2 total differential, Q37 finite projective planes.

## zkouska-2019-podzim.pdf

- Q1 Automaty a gramatiky - COVERED. Regular-language definitions, grammars and regularity arguments are in `spolecna-informatika`.
- Q2 Prohledávání do šířky - COVERED. Adjacency lists, BFS, complexity and bipartiteness by BFS are in `spolecna-informatika`.
- Q4 OO návrh GUI frameworku - COVERED. C#/Java/C++ class/interface design and callbacks/events are in `spolecna-informatika`.
- Q5 Překlad - COVERED. Stack frames, machine instructions, jumps and code generation patterns are in `spolecna-informatika`.
- Q16 Základy teorie informace - COVERED. Independence, entropy and mutual information are in `spolecna-matematika`.
- Q26 Rozhraní pro synchronizaci - COVERED. Semaphores, mutexes, condition variables and interprocess synchronization are in `spolecna-informatika`.
- Q27 Garbage collection - COVERED. Generational hypothesis, reachability and object lifetime reasoning are in `spolecna-informatika`.
- Q28 Rozhraní pro práci se soubory - COVERED. File descriptors, read/write variants and OS/hardware separation are in `spolecna-informatika`.

Ignored as out of current scope: Q3 databases, Q6 optimization/LP, Q7 routing, Q8 approximation algorithms, Q9 computational geometry, Q10/Q13 coding theory, Q11 set theory beyond basics, Q12 Turan theorem specialization, Q14-Q15 NLP, Q17-Q19 graphics, Q20-Q22 networking, Q23-Q25 web/databases, Q29 testing.

## zkouska-2020-jaro.pdf

- Q1 Automaty a gramatiky - COVERED. Kleene theorem, regular expressions/automata and closure by complement/intersection are in `spolecna-informatika`.
- Q2 Toky v sítích - GAP -> Missing: Edmonds-Karp via shortest augmenting paths and the vertex-capacity split were not explicit. Root cause: flow notes stated Ford-Fulkerson and max-flow/min-cut but not common exam variants. Added: shortest augmenting path complexity and vertex-capacity reduction to `src/sections/spolecna-informatika.tex`.
- Q4 Objektově orientované programování a vlákna - COVERED. Virtual dispatch, comparers/delegates and parallel mergesort structure are in `spolecna-informatika`.
- Q5 Architektura počítačů - COVERED. Endianity, bit fields, alignment, memory dumps and load/store instruction manipulation are in `spolecna-informatika`.
- Q9 Základy teorie informace - COVERED. Entropy and conditional entropy are in `spolecna-matematika`.
- Q13 C++ traits a policies - COVERED. Generic programming patterns and policy-style design are derivable from `spolecna-informatika`.
- Q14 Návrhový vzor Decorator - COVERED. Interfaces, inheritance/delegation and stream-style wrappers are in `spolecna-informatika`.
- Q16 Spouštění procesů a volací konvence - COVERED. Process address space, stack frames and calling convention basics are in `spolecna-informatika`.
- Q18 Zasílání zpráv - COVERED. Message passing, callbacks and thread handling are covered by OS/programming notes in `spolecna-informatika`.

Ignored as out of current scope: Q3 databases, Q6 TCP/IP architecture, Q7-Q8 NLP, Q10-Q12 graphics, Q15 web authentication, Q17 version control.

## zkouska-2020-leto.pdf

- Q1 Automaty a gramatiky - COVERED. CFG, Chomsky normal form, derivation trees and grammar transformations are in `spolecna-informatika`.
- Q2 Algoritmy a datové struktury - GAP -> Missing: DFS edge classification and the "cycle cannot consist only of back edges" reasoning were not explicit. Root cause: graph traversal notes had DFS mechanics but not the directed-edge taxonomy. Added: DFS edge classes and the relevant cycle fact to `src/sections/spolecna-informatika.tex`.
- Q4 Programování - COVERED. Expression trees, symbolic derivation, factories and extensible function registries are in `spolecna-informatika`.
- Q5 Architektura počítačů - COVERED. Race conditions, critical sections and locking around shared list mutations are in `spolecna-informatika`.
- Q18 Základy teorie informace - COVERED. Entropy and mutual information are in `spolecna-matematika`.
- Q28 Synchronizace na multiprocesorech - COVERED. Spinlocks, compare-and-swap and load-linked/store-conditional are in `spolecna-informatika`.
- Q29 Správa paměti - COVERED. Heap allocation, block headers, alignment and first-fit reasoning are in `spolecna-informatika`.

Ignored as out of current scope: Q3 databases, Q6 transport/TCP/IP, Q7 computational geometry, Q8 approximation algorithms, Q9/Q15 coding theory, Q10-Q12 databases/web/security, Q13 set theory beyond basics, Q14 edge-coloring specialization, Q16-Q17 NLP, Q19-Q21 graphics, Q22-Q24 networking, Q25-Q27 web/XML/semantic web, Q30 design patterns.

## zkouska-2020-podzim.pdf

- Q1 Automaty a gramatiky - COVERED. Pumping lemma for CFLs, grammar construction and Chomsky hierarchy placement are in `spolecna-informatika`.
- Q2 Topologické uspořádání - GAP -> Missing: the linear-time filter for vertices on a path from `u` to `v` in a DAG was not stated. Root cause: topological sort was covered, but the reachability-intersection trick was absent. Added: DAG path-vertex criterion and two-search algorithm to `src/sections/spolecna-informatika.tex`.
- Q4 Objektový návrh - COVERED. Controller interfaces, stateful/stateless objects and factory construction are in `spolecna-informatika`.
- Q5 Architektura počítačů a systém souborů FAT - COVERED. Little endian parsing, file-system allocation tables and block-chain reasoning are in `spolecna-informatika`.
- Q19 Základy teorie informace - COVERED. Entropy units, independence and binary entropy bounds are in `spolecna-matematika`.
- Q26 Garbage collection - COVERED. Mark-and-sweep, roots and stop-the-world reasoning are in `spolecna-informatika`.
- Q27 Rozhraní pro práci se soubory - COVERED. Memory mapping, pages, virtual/physical memory and shared/private mappings are in `spolecna-informatika`.

Ignored as out of current scope: Q3 databases, Q6 transport protocols, Q7 optimization/polyhedra, Q8 approximation algorithms, Q9 computational geometry, Q10/Q16 coding theory, Q11-Q13 databases/web, Q14 set theory beyond basics, Q15 advanced matching/Tutte, Q17-Q18 NLP, Q20-Q22 graphics, Q23-Q25 web/software engineering, Q28 program verification.

## zkouska-2021-leto.pdf

- Q1 Chomského hierarchie - COVERED. Hierarchy placement and corresponding automata are in `spolecna-informatika`.
- Q2 Haldy - GAP -> Missing: heap implementation, ExtractMin and Heapsort were not explicit. Root cause: heaps appeared only indirectly as priority queues for Dijkstra/MST. Added: binary heap representation, operations and Heapsort to `src/sections/spolecna-informatika.tex`.
- Q4 Pořadí v týmové soutěži - COVERED. C#/Java/C++ object model, interfaces, generic criteria and reusable strategy-style design are in `spolecna-informatika`.
- Q5 Architektura počítačů a operačních systémů - COVERED. Shared mutable state, race conditions, critical sections and locks are in `spolecna-informatika`.
- Q19 Základy teorie informace - COVERED. Binary entropy, conditional entropy, joint entropy and mutual information are in `spolecna-matematika`.
- Q29 Rozhraní pro synchronizaci - COVERED. Mutexes, deadlock, possible interleavings and processor-count effects are in `spolecna-informatika`.
- Q30 Heap alokátory - COVERED. Heap allocation, size classes, alignment and allocator overhead are in `spolecna-informatika`.

Ignored as out of current scope: Q3 databases, Q6 routing, Q7 optimization/LP, Q8 approximation algorithms, Q9 computational geometry, Q10 coding theory, Q11-Q13 databases/web, Q14-Q15 advanced graph theory, Q16 set theory beyond basics, Q17-Q18 NLP, Q20-Q22 graphics, Q23-Q25 networking, Q26-Q28 JSON/web/semantic web, Q31 middleware.

## zkouska-2021-podzim.pdf

- Q1 Chomského hierarchie - COVERED. CFG definitions and hierarchy classification are in `spolecna-informatika`.
- Q2 Minimální kostry - COVERED. MST definition, Jarnik/Prim, Boruvka, cut lemma and update after edge decrease are in `spolecna-informatika`.
- Q4 Objektový návrh karetní hry - COVERED. Strongly typed OO interfaces, extensibility and attach/detach effects are derivable from `spolecna-informatika`.
- Q5 Architektura počítačů - COVERED. Memory-mapped device registers, PIO, polling, bit masks and driver loops are in `spolecna-informatika`.
- Q19 Základy teorie informace - COVERED. Entropy inequalities and mutual information are in `spolecna-matematika`.
- Q29 Synchronizační primitiva - COVERED. Semaphores, passive waiting, wakeup races and bounded waiting are in `spolecna-informatika`.

Ignored as out of current scope: Q3 SQL, Q6 transport protocols, Q7 optimization/LP, Q8/Q14 coding theory, Q9 computational geometry, Q10 approximation algorithms, Q11-Q13 databases/web/XML, Q15 edge-coloring specialization, Q16 set theory beyond basics, Q17-Q18 NLP, Q20-Q22 graphics, Q23-Q25 networking, Q26-Q28 web/software engineering/parallel programming beyond common, Q30-Q31 version control/design patterns.

## zkouska-2022-leto.pdf

- Q1 Zásobníkový automat - COVERED. PDA definition and CFG-to-PDA construction are in `spolecna-informatika`.
- Q2 Binární vyhledávací stromy - GAP -> Missing: successor in an unbalanced BST was not stated. Root cause: BVS operations covered find/insert/delete but omitted the common successor template. Added: successor algorithm and complexity to `src/sections/spolecna-informatika.tex`.
- Q4 Emulátor procesoru - COVERED. Instruction interfaces, memory access, endianity and emulator-style dispatch are in `spolecna-informatika`.
- Q5 Překlad konstrukcí vyššího jazyka - COVERED. Branches, loops, comparisons and assembly/C correspondence are in `spolecna-informatika`.
- Q22 Spouštění procesů a relokace - COVERED. Absolute/relative addressing, relocation and position dependence are in `spolecna-informatika`.
- Q23 Rozhraní pro synchronizaci - COVERED. Condition variables and bounded producer-consumer synchronization are in `spolecna-informatika`.

Ignored as out of current scope: Q3 databases, Q6 networking/routing, Q7 approximation algorithms, Q8 max-cut specialization, Q9 computational geometry, Q10 databases, Q11-Q12 web/CSS, Q13 set theory beyond basics, Q14 Ramsey theory, Q15 edge-coloring specialization, Q16-Q18 NLP, Q19-Q21 graphics, Q24 middleware.

## zkouska-2022-podzim.pdf

- Q1 Průnik regulárních výrazů - COVERED. Regular expressions, Kleene theorem and product/intersection construction are in `spolecna-informatika`.
- Q2 Silná souvislost - GAP -> Missing: SCC algorithm and the condensation-DAG characterization of "good" vertices were not explicit. Root cause: common graph theory defined strong connectivity but the algorithmic SCC hook was missing. Added: Kosaraju/Tarjan and terminal-component characterization to `src/sections/spolecna-informatika.tex`.
- Q4 Programování - grafy - COVERED. Generic OO graph interfaces and component labeling by graph traversal are in `spolecna-informatika`.
- Q5 Virtuální paměť - COVERED. Page tables, page attributes, dirty/accessed bits and address translation are in `spolecna-informatika`.
- Q19 Základní koncepty profilování výkonu - COVERED. Instruction-level parallelism, IPC and parallel speedup reasoning are in `spolecna-informatika`.
- Q20 Paralelismus a synchronizace - COVERED. Spinlocks, recursive locks, atomics and passive waiting are in `spolecna-informatika`.

Ignored as out of current scope: Q3 SQL, Q6 routing, Q7 approximation algorithms, Q8 computational geometry/Voronoi, Q9-Q10 coding theory, Q11-Q12 advanced graph theory, Q13-Q15 NLP, Q16-Q18 graphics, Q21 testing, Q22-Q24 databases/web, Q25-Q27 XML/software engineering/version control.

## zkouska-2023-jaro.pdf

- Q1 Konkatenace palindromů - COVERED. Automata, grammars and Chomsky hierarchy are in `spolecna-informatika`.
- Q2 Třídění - COVERED. BST sorting, AVL complexity and comparison sorting lower bound are in `spolecna-informatika`.
- Q5 Organizace paměti procesu - COVERED. Stack, heap, static allocation, process address space and alignment are in `spolecna-informatika`.
- Q7 Základy teorie informace - GAP -> Missing: entropy, conditional entropy, mutual information and the inequalities `H(X) >= H(X|Y)`, `H(X,Y) <= H(X)+H(Y)` were not derivable from the probability section. Root cause: the materials used entropy only inside decision trees, not as a probability concept. Added: entropy, conditional entropy, mutual information and the two inequalities to `src/sections/spolecna-matematika.tex`.

Ignored: NLP, graphics, databases, ORM/MVC and networking specialization questions.

## zkouska-2023-leto.pdf

- Q1 Třídění sléváním - COVERED. Mergesort and divide-and-conquer recurrences are in `spolecna-informatika`.
- Q2 Převod bezkontextové gramatiky na automat - COVERED. CFG, PDA and conversion CFG to PDA are in `spolecna-informatika`.
- Q3 Lineární algebra - COVERED. Matrices, scalar product, linear maps, inverse matrices and determinant/geometric scaling are in `spolecna-matematika`.
- Q4 Pravděpodobnost - COVERED. Linearity of expectation and indicator-style computations are in `spolecna-matematika`.
- Q5 Skrytý Markovův model - COVERED. HMM definition, Markov assumption, filtering, prediction and smoothing formulas are in `zaklady-ui`.
- Q6 Testování binárního klasifikátoru - GAP -> Missing: formulas connecting TPR/FPR/precision to counts under a known class prior were implicit, so the constant-precision ROC subquestion required external algebraic recall. Root cause: metrics were defined individually but not tied to confusion-matrix reconstruction. Added: `TP`, `FN`, `FP`, `TN` from `TPR`, `FPR`, and precision inversion to `src/sections/strojove-uceni.tex`.
- Q7 Rozhodovací stromy - COVERED. Greedy tree induction, entropy/Gini and separability by leaves are in `strojove-uceni`.
- Q8 Shlukování - COVERED. k-means iterations and hierarchical clustering are in `strojove-uceni`.

Ignored: graphics, networks, OS specialization, databases, advanced math outside common scope.

## zkouska-2023-podzim.pdf

- Q1 Architektura počítačů a operačních systémů - COVERED. CPU, OS, virtual memory and process/thread basics are in `spolecna-informatika`.
- Q2 Zásobníkový automat - COVERED. PDA definitions and constructions are in `spolecna-informatika`.
- Q3 Souvislost grafů - COVERED. Connectivity, components and graph traversal are in `spolecna-matematika` and `spolecna-informatika`.
- Q4 Geometrická řada - COVERED. Series convergence and geometric sum are in `spolecna-matematika`.
- Q28 CSP - COVERED. CSP definition, backtracking, arc consistency, forward checking, look ahead/MAC and Sudoku modeling are in `zaklady-ui`.
- Q29 Chí-kvadrát test - COVERED. Goodness-of-fit statistic, hypotheses, degrees of freedom and critical-value decision are in `strojove-uceni`.
- Q30 Kombinace více modelů - COVERED. Bagging, boosting, AdaBoost idea, random forest and tree/forest comparison are in `strojove-uceni`.
- Q31 Evaluační metriky - COVERED. Accuracy, precision, recall, F1, class imbalance and fraud/anomaly tradeoffs are in `strojove-uceni`.

## zkouska-2024-jaro.pdf

- Q1 Reprezentace bezkontextového jazyka - COVERED. CFG, PDA and language representations are in `spolecna-informatika`.
- Q2 Ovladač pro řadič disku - COVERED. PIO, device controller, driver, polling/interrupts and port-level service pattern are in `spolecna-informatika`.
- Q3 Skalární součin - COVERED. Scalar product, orthogonality, norm and Gram-Schmidt/projection facts are in `spolecna-matematika`.
- Q4 Nespojitost funkce - COVERED. Limits, continuity and discontinuity reasoning are in `spolecna-matematika`.
- Q26 Statistické testy - t-test - COVERED. One-sample, two-sample, Welch and paired t-tests are in `strojove-uceni`.
- Q27 Lineární regrese a regularizace - COVERED. Normal equations, SGD and L2 regularization are in `strojove-uceni`.
- Q28 Shlukování - COVERED. k-means, kmeans++, loss and hierarchical clustering are in `strojove-uceni`.
- Q32 Informované prohledávání - COVERED. A*, admissibility, consistency, dominance and graph-search conditions are in `zaklady-ui`.

Ignored: UI-ZPJ-only NLP/deep-learning questions.

## zkouska-2024-leto.pdf

- Q1 Algoritmy rozděl a panuj - COVERED. Divide-and-conquer and Master theorem are in `spolecna-informatika`.
- Q2 Semafor - COVERED. Semaphores, passive waiting, counters and producer/consumer-style synchronization are in `spolecna-informatika`.
- Q3 Báze vektorových prostorů - COVERED. Basis, dimension, linear independence and coordinates are in `spolecna-matematika`.
- Q4 Model teorie - COVERED. Predicate logic, structures/models and satisfaction are in `spolecna-matematika`.
- Q28 Bayesovské sítě - COVERED. BN definition, factorization, construction and inference are in `zaklady-ui`.
- Q29 PCA analýza - COVERED. PCA, SVD, covariance, projection and approximation are in `strojove-uceni`.
- Q30 SVM - COVERED. Hard/soft margin, support vectors, kernels, RBF and `C` are in `strojove-uceni`.
- Q31 Metoda nejmenších čtverců - COVERED. Least squares, normal equations and singular/regularized cases are in `strojove-uceni`.

## zkouska-2024-podzim.pdf

- Q1 Doplněk regulárního výrazu - COVERED. Regular languages, DFA construction and complement are in `spolecna-informatika`.
- Q2 Reprezentace typů - COVERED. Primitive and composite type representation, alignment and object/runtime notes are in `spolecna-informatika`.
- Q3 Integrály a primitivní funkce - COVERED. Primitive function, Newton/Riemann integral and basic techniques are in `spolecna-matematika`.
- Q4 Barevnost grafů - COVERED. Chromatic number, cliques, bipartiteness and bounds are in `spolecna-matematika`.
- Q28 Minimax - COVERED. Minimax, alpha-beta and game assumptions are in `zaklady-ui`.
- Q29 Logistická regrese - COVERED. Sigmoid, likelihood/NLL, gradient and SGD are in `strojove-uceni`.
- Q30 Evaluace binárního klasifikátoru - COVERED. Confusion matrix, precision, recall, F1 and imbalance reasoning are in `strojove-uceni`.
- Q31 Rozhodovací strom - COVERED. Tree induction, split criteria, entropy/Gini and pruning are in `strojove-uceni`.

## zkouska-2025-jaro.pdf

- Q1 Průnik bezkontextového a regulárního jazyka - COVERED. CFG/PDA and automata constructions are in `spolecna-informatika`.
- Q2 Knihovna pro výpočty s maticemi - COVERED. Matrix operations and programming-language abstractions/classes are in `spolecna-matematika` and `spolecna-informatika`.
- Q3 Matice - COVERED. Matrix rank, inverse, determinant, eigenvalues and diagonalization facts are in `spolecna-matematika`.
- Q4 Eulerovské grafy - COVERED. Eulerian graph criteria and graph basics are in `spolecna-matematika`.
- Q27 DPLL a párování - COVERED. DPLL, unit propagation, pure literals and matching/SRR basics are in `zaklady-ui` and `spolecna-matematika`.
- Q28 k-nejbližších sousedů - COVERED. kNN classification/regression, training, prediction and cross-validation for `k` are in `strojove-uceni`.
- Q29 Logistická regrese pro binární klasifikaci - COVERED. Prediction, train/dev/test split, NLL derivative, SGD and anti-overfitting are in `strojove-uceni`.
- Q30 Bayesovské učení - COVERED. Maximum likelihood hypotheses, priors/posteriors and Bayes-optimal prediction are in `zaklady-ui`.

Ignored: UI-ZPJ-only language-model question.

## zkouska-2025-leto.pdf

- Q1 Deterministické konečné automaty - COVERED. DFA definition, language and construction patterns are in `spolecna-informatika`.
- Q2 Jednoduchý správce paměti - COVERED. Heap allocation, address spaces and synchronization/building blocks are in `spolecna-informatika`.
- Q3 Skalární součin - COVERED. Scalar product, orthogonality and projection are in `spolecna-matematika`.
- Q4 Centrální limitní věta - COVERED. CLT statement and normalization are in `spolecna-matematika`.
- Q29 Bellmanova rovnice užitku - COVERED. MDP definition, utility, policy and Bellman equations are in `zaklady-ui`.
- Q30 Lineární regrese - COVERED. Linear model, least squares and normal equations are in `strojove-uceni`.
- Q31 Shlukování - COVERED. k-means steps, loss, initialization and local minima are in `strojove-uceni`.
- Q32 EM algoritmus - GAP -> Missing: EM was described conceptually, but not with the responsibility formula and expected-count updates needed to compute one update in a Bayes net with hidden `Cluster`. Root cause: overview-level EM text omitted the computational pattern. Added: responsibility formula and categorical parameter updates to `src/sections/zaklady-ui.tex`.

## zkouska-2025-podzim.pdf

- Q1 Třídy složitosti - COVERED. P, NP, reductions, NP-hardness and NP-completeness are in `spolecna-informatika`.
- Q2 Ukládání dat v binárním souboru - COVERED. Binary representation, alignment, structures and file abstraction are in `spolecna-informatika`.
- Q3 Základy analýzy - COVERED. Limits, continuity, derivatives and integrals are in `spolecna-matematika`.
- Q4 Binární relace - COVERED. Relations, equivalences, orders and examples are in `spolecna-matematika`.
- Q27 Jednotahové hry - COVERED. Dominant strategies, Nash equilibrium and Pareto optimality are in `zaklady-ui`.
- Q28 Evaluace binárního klasifikátoru - GAP -> Same root cause as 2023-leto Q6: the old metrics text did not explicitly teach reconstructing counts from partial marketing metrics under class imbalance. Added formulas in `src/sections/strojove-uceni.tex`.
- Q29 Predikce pomocí tabulárních dat - GAP -> Missing: categorical/continuous preprocessing, one-hot encoding, imputation/scaling rules and regression metrics MAE/RMSE were not explicit. Root cause: supervised-learning section focused on model theory and binary metrics, not end-to-end tabular workflow. Added preprocessing rules, robust tabular model choices and MAE/RMSE to `src/sections/strojove-uceni.tex`.
- Q30 Lineární regrese, L2 regularizace - COVERED. OLS, normal equations, L2 objective and shrinkage direction are in `strojove-uceni`.

## zkouska-2026-jaro.pdf

- Q1 Porovnání modulárních hashů - COVERED. DFA definition and construction ability are in `spolecna-informatika`; the modular update rule is given in the question and is directly usable with DFA states.
- Q2 Semafor mezi procesy - COVERED. Semaphores, producer/consumer counters, passive waiting and invariants are in `spolecna-informatika`.
- Q3 Matice - COVERED. Matrix operations, rank/inverse/determinant/eigen facts are in `spolecna-matematika`.
- Q4 Rovinné grafy - COVERED. Planarity, Euler formula, edge bounds and Kuratowski are in `spolecna-matematika`.
- Q27 CSP - COVERED. Binary CSP, arc consistency, AC-3, local-vs-global consistency and counterexamples are in `zaklady-ui`.
- Q28 Shlukování pomocí K-means - COVERED. k-means steps, kmeans++, objective, monotone loss decrease and local minima are in `strojove-uceni`.
- Q29 Kombinace modelů - COVERED. Bagging, boosting, random forest and the need for diverse/uncorrelated errors are now derivable from the ensemble text; the exact best/worst majority-vote cases follow from comparing error sets.
- Q30 Rozhodovací strom - COVERED. Entropy/Gini split criteria, greedy construction and pruning are in `strojove-uceni`.

## Observations across all 20 exams (2019-2026)

Format evolution: 2019-2022 files are broad pre-specialization collections. They mix common informatics, old specialization blocks and appended math questions, and they do not contain UI-SU or ML specialization questions. From 2023 onward the files use modern labels such as `(společné okruhy)` and `(specializace UI-SU)`, so a UI-SU student sees a much cleaner split: 2 common math, 2 common informatics and 4 UI/ML specialization questions.

High-yield recurring common topics: automata and grammars appear almost every term, especially regular languages, CFG/PDA and Chomsky hierarchy classification. Algorithms repeatedly ask graph traversal, topological sorting, MST, flows, heaps/BSTs and sorting. OS/architecture repeatedly asks memory layout, endianity/alignment, virtual memory, device registers, synchronization and heap/file-system mechanics. In common math, the most repeated useful topics are linear algebra, single-variable analysis, graph basics, probability/information-theory quantities and logic definitions.

High-yield UI-SU topics in 2023-2026: evaluation metrics, regression, clustering, decision trees, ensembles, SVM/PCA, Bayesian networks/HMM/EM, CSP/search and basic game/MDP reasoning. These recur more often than exotic ML methods and usually reward exact definitions plus a short computational pattern.

Typical question anatomy: first subquestion asks for a definition, theorem or algorithm statement; the middle asks for construction, pseudocode, proof sketch or a small calculation; the last asks for a boundary case, counterexample, complexity, or an applied design. The easiest reliable points come from definitions and named invariants; the third point usually needs recognizing the template and applying it carefully.

Final verdict: after the fixes listed below, the materials in `src/sections/*.tex` are sufficient for every in-scope question across all 20 exams. The older exams add pressure on common graph algorithms, OS synchronization and low-level representation, but not on ML specialization content. The modern exams add the actual UI-SU requirements, and those are now covered as well.

## Generalized gaps

1. Probability concepts used by ML were split across sections.
   - Symptom: entropy appeared for trees, but conditional entropy and mutual information were absent.
   - Fix: added entropy, conditional entropy, mutual information and the standard inequalities to common probability.
   - Other checks implied: decision-tree entropy and Bayesian reasoning still remain covered in the ML/UI sections.

2. Metrics were defined but not always connected to count reconstruction.
   - Symptom: ROC/precision/recall questions with class imbalance required reconstructing `TP`, `FP`, `TN`, `FN`.
   - Fix: added formulas from `TPR`, `FPR`, class counts and fixed precision to `strojove-uceni`.
   - Other checks implied: fraud/anomaly evaluation questions and ROC questions are now derivable without outside formulas.

3. End-to-end tabular ML workflow was thinner than model theory.
   - Symptom: the 2025-podzim tabular regression question asked for preprocessing and metrics, not just a model definition.
   - Fix: added one-hot encoding, scaling, imputation, model choices for tabular regression, MAE and RMSE.
   - Other checks implied: kNN/SVM/PCA scale sensitivity and random-forest robustness are now explicit.

4. EM was conceptual but not computational.
   - Symptom: an EM question required one numeric update for a hidden cluster in a Bayes net.
   - Fix: added responsibilities and expected-count updates for categorical latent-variable models.
   - Other checks implied: Bayes learning and HMM/Bayes-net inference already had enough probability machinery.

Final verdict: after these additions, every relevant real exam question in `zkousky/zkouska-*.pdf` is covered or made derivable from `src/sections/*.tex` alone, in UI-SU scope, without relying on external learning material.
