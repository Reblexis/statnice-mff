# Completeness audit against real exams for UI-SU

Scope: UI-SU / Machine Learning student. I counted modern `(společné okruhy)`,
`(specializace UI-SU)` and shared UI-SU questions. For older 2023 mixed files I
counted common-theory and AI/ML questions, and ignored DB, networking, graphics,
NLP-only and software-engineering specialization material.

Verdict after fixes: the materials are now sufficient to answer all relevant
questions below from the included sources alone. The remaining risk is not
missing theory, but ordinary exam execution: doing arithmetic carefully and
recognizing which template applies.

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
