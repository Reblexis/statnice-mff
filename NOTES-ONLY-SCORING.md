# Notes-only scoring estimate

Knowledge source used: only `notes-ipp/statnice/*.md`. Exam PDFs were converted with `pdftotext -layout` and read from `/tmp/statnice-exams-text/zkouska-*.txt`. I ignored `src/sections`, requirements, outside knowledge, and out-of-scope old specialization pools.

Scoring: `A/R/P` means achievable, realistic, pessimistic, each on `0..3`. Pass rule for full current UI-SU sittings: total `>= 12`, common `>= 5`, specialization `>= 7`. For 2019-2022, there are no current UI-SU specialization questions, so only common-scope questions are scored and the full sitting cannot be simulated.

## 2019 jaro

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Automata, closure of regular languages | 3/2.5/2 | none |
| 2 | Sorting with BST, lower bound, integer-pair sorting | 2/1.5/0.5 | [ALGO] exact linear-time pair sorting over `{1..n}^2` is not in notes |
| 4 | Programming languages, expression object model | 1.5/1/0.5 | [IMPL] full OO API design, error propagation, and DAG sharing are not trained |
| 5 | Processes, threads, scheduling states | 2.5/2/1 | [DEF] notes use a simplified state vocabulary and do not give the exact READY/RUNNING/WAITING transition diagram |
| 17 | Function derivative, limits, graph sketch | 2.5/2/1 | [COMP] graph-sketch execution and derivative practice are deferred |
| 18 | Riemann integral definition and computation | 2.5/2/1 | [COMP] concrete integral computation practice is thin |
| 23 | Inclusion-exclusion | 2.5/2/1 | [COMP] problem-solving variants are not worked out |
| 24 | Graphs | 2.5/2/1 | [COMP] concrete graph proofs depend on exercise skill |
| 25 | Logic | 2.5/2/1 | [COMP] formal manipulation practice is thin |

Representative simulated common total, using 2 informatics plus 2 math questions: `A 10.5`, `R 8.5`, `P 4.5`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2019 leto

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | CFG, PDA, nonregularity proof | 2.5/2/1 | [COMP] custom PDA construction and pumping/Nerode proof execution |
| 2 | P, NP, NP-completeness | 3/2.5/2 | none |
| 4 | Object model and serialization hooks | 1.5/1/0.5 | [IMPL] concrete OO design and file-output API details are not in notes |
| 5 | Binary data, alignment, endian, file reading | 2/1.5/0.5 | [IMPL] byte-level parser implementation is not trained |
| 30 | Vectors | 2.5/2/1 | [COMP] concrete vector computation practice |
| 32 | Matrices | 2.5/2/1 | [COMP] matrix computation practice |
| 33 | Sequences and limits | 2.5/2/1 | [COMP] limit exercises |
| 38 | Logic | 2.5/2/1 | [COMP] formal proof/calculation practice |

Representative common total: `A 9.5`, `R 7.5`, `P 4`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2019 podzim

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Regular languages and grammars | 2.5/2/1 | [COMP] exact regularity proof by construction/Nerode |
| 2 | BFS and bipartiteness | 3/2.5/2 | none |
| 4 | OO GUI framework | 1.5/1/0.5 | [IMPL] event/callback framework design is not in notes |
| 5 | Instruction-level translation | 1/0.5/0 | [IMPL] compiling Pascal-like code to a toy CPU is not covered |

Representative common total: `A 8`, `R 6`, `P 3.5`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2020 jaro

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Automata and grammars | 2.5/2/1 | [COMP] construction/proof practice |
| 4 | OOP and threads | 1.5/1/0.5 | [IMPL] complete code-level OO/thread solution |
| 5 | Computer architecture | 2/1.5/0.5 | [IMPL] instruction-level/code details are only signposted as "practice" |

Representative common total: `A 6`, `R 4.5`, `P 2`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2020 leto

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Automata and grammars | 2.5/2/1 | [COMP] construction/proof practice |
| 2 | Algorithms and data structures | 2.5/2/1 | [COMP] exact DS algorithms need exercise practice |
| 4 | Programming | 1.5/1/0.5 | [IMPL] concrete API and code design |
| 5 | Computer architecture | 2/1.5/0.5 | [IMPL] low-level reading and endian/alignment computations |

Representative common total: `A 8.5`, `R 6.5`, `P 3`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2020 podzim

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Automata and grammars | 2.5/2/1 | [COMP] construction/proof practice |
| 2 | Topological ordering | 2.5/2/1 | [COMP] exact algorithm proof/application |
| 4 | Object design | 1.5/1/0.5 | [IMPL] full OO design implementation |
| 5 | Architecture and FAT | 1.5/1/0.5 | [IMPL] FAT/file-system concrete layout computations are not covered |
| 15 | Perfect matching | 2/1.5/0.5 | [DEF] Hall/perfect matching details are only partially in graph notes |

Representative common total: `A 8`, `R 6`, `P 3`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2021 leto

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Chomsky hierarchy | 3/2.5/2 | none |
| 2 | Heaps | 2.5/2/1 | [ALGO] exact heap operation proofs and variants are brief |
| 4 | Programming contest ranking | 1.5/1/0.5 | [IMPL] concrete program design/problem implementation |
| 5 | Architecture and OS | 2/1.5/0.5 | [IMPL] exact low-level scenarios |

Representative common total: `A 9`, `R 7`, `P 4`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2021 podzim

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Chomsky hierarchy | 3/2.5/2 | none |
| 2 | Minimum spanning trees | 2.5/2/1 | [ALGO] MST algorithms are present, but proof/application detail is limited |
| 4 | Object design of card game | 1.5/1/0.5 | [IMPL] full OO model design |
| 5 | Architecture | 2/1.5/0.5 | [IMPL] exact binary/assembly-level reasoning |

Representative common total: `A 9`, `R 7`, `P 4`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2022 leto

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | PDA | 2.5/2/1 | [COMP] custom PDA construction |
| 2 | Binary search trees | 2.5/2/1 | [ALGO] exact operation bounds/proofs are brief |
| 4 | Processor emulator | 1/0.5/0 | [IMPL] emulator implementation is not covered |
| 5 | Compilation of high-level constructs | 1/0.5/0 | [IMPL] toy instruction translation is not covered |

Representative common total: `A 7`, `R 5`, `P 2`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2022 podzim

Relevant current-scope common questions only.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Intersection of regular expressions | 2.5/2/1 | [COMP] automaton construction exercise |
| 2 | Strong connectivity | 2.5/2/1 | [ALGO] exact SCC algorithm/proof details are thin |
| 4 | Programming graphs | 1.5/1/0.5 | [IMPL] concrete program design |
| 5 | Virtual memory | 2.5/2/1 | [COMP] address-translation examples need practice |

Representative common total: `A 9`, `R 7`, `P 3.5`. Specialization: N/A. Full UI-SU pass: not simulatable, treated as fail for total/spec thresholds.

## 2023 jaro

Mixed old/current format. Current-scope common and AI/ML study-focus questions only; not enough current specialization questions to simulate a full sitting.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Concatenation of palindromes | 2/1.5/0.5 | [COMP] exact language construction/proof not practiced |
| 2 | Sorting | 2.5/2/1 | [COMP] exact algorithm variants |
| 4 | Object design | 1.5/1/0.5 | [IMPL] concrete OO design |
| 5 | Process memory organization | 2/1.5/0.5 | [IMPL] exact OS memory-layout reasoning |
| 16 | Reinforcement learning | 2.5/2/1 | [DEF] notes cover ADP/TD/Q-learning/SARSA, but not all exam phrasing and comparisons |

Available common/spec total: `A 10.5`, `R 8`, `P 3.5`. Full UI-SU pass: not simulatable, treated as fail for missing full specialization set.

## 2023 leto

Full current-style simulation from 4 common plus 4 AI/ML study-focus questions.

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Mergesort and k-way merge | 2.5/2/1 | [ALGO] k-way merge with heap and exact `O(n log k)` adaptation is not explicit |
| 2 | CFG to PDA | 2.5/2/1 | [COMP] constructing the specific grammar for `2i=3j` needs practice |
| 3 | Linear algebra matrices | 2.5/2/1 | [COMP] determinant/linear-map calculations need practice |
| 4 | Linearity of expectation | 3/2.5/2 | none |
| 5 | HMM filtering | 2.5/2/1 | [COMP] notes give the recurrence, but not this two-step numeric filtering drill |
| 6 | ROC and precision | 2.5/2/1 | [ML-FORMULA] precision/TPR/FPR formulas are present, but ROC-from-constant-precision plotting is not explicit |
| 7 | Decision tree entropy split | 2.5/2/1 | [COMP] entropy information-gain arithmetic is only partially practiced |
| 8 | K-means and hierarchical clustering | 2.5/2/1 | [COMP] manual centroid and dendrogram outcome computation |

Totals: common `A 10.5`, spec `A 10`, total `A 20.5`, pass. Realistic: common `8.5`, spec `8`, total `16.5`, pass. Pessimistic: common `5`, spec `5.5`, total `10.5`, fail.

## 2023 podzim

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Race condition in stack | 2/1.5/0.5 | [IMPL] exact synchronized/lock code and line-level race scenario are not in notes |
| 2 | PDA | 2.5/2/1 | [COMP] custom PDA for imbalance plus parity |
| 3 | Menger theorem and cuts | 2.5/2/1 | [COMP] applying Menger to the concrete graph |
| 4 | Geometric series | 3/2.5/2 | none |
| 28 | CSP and Sudoku model | 3/2.5/2 | none |
| 29 | Chi-square test | 3/2.5/2 | none |
| 30 | Bagging, boosting, random forest | 3/2.5/2 | none |
| 31 | Binary-classification metrics | 3/2.5/2 | none |

Totals: common `A 10`, spec `A 12`, total `A 22`, pass. Realistic: common `8`, spec `10`, total `18`, pass. Pessimistic: common `4.5`, spec `8`, total `12.5`, fail by common threshold.

## 2024 jaro

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Representation of context-free language | 2.5/2/1 | [COMP] exact construction details |
| 2 | Disk-controller driver | 1/0.5/0 | [IMPL] PIO driver code for device ports is explicitly deferred to practice |
| 3 | Scalar product | 2.5/2/1 | [COMP] matrix/vector arithmetic |
| 4 | Discontinuity of function | 2.5/2/1 | [COMP] exact epsilon/limit classification practice |
| 26 | One-sample t-test | 3/2.5/2 | none |
| 27 | Linear regression and L2 update | 2.5/2/1 | [COMP] full-batch gradient arithmetic with regularization |
| 28 | K-means clustering | 3/2.5/2 | none |
| 32 | Informed search, A* | 3/2.5/2 | none |

Totals: common `A 8.5`, spec `A 11.5`, total `A 20`, pass. Realistic: common `7`, spec `10`, total `17`, pass. Pessimistic: common `4`, spec `7`, total `11`, fail by total/common.

## 2024 leto

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Divide and conquer, Master theorem, median | 2.5/2/1 | [ALGO] median of two sorted arrays is absent |
| 2 | Semaphore synchronization | 1.5/1/0.5 | [IMPL] exact two-semaphore program and schedule enumeration |
| 3 | Steinitz exchange and diagonalization | 2.5/2/1 | [COMP] coordinate computations in eigen-bases |
| 4 | Model of theory | 2.5/2/1 | [COMP] formal model construction/proof by tableau/resolution |
| 28 | Bayesian networks | 2.5/2/1 | [COMP] exact posterior arithmetic from CPD tables |
| 29 | PCA | 2.5/2/1 | [COMP] visual PCA direction and downstream kNN effect |
| 30 | SVM | 2.5/2/1 | [COMP] geometric support-vector boundary reasoning |
| 31 | Least squares | 2.5/2/1 | [COMP] hand OLS and MSE computation |

Totals: common `A 9`, spec `A 10`, total `A 19`, pass. Realistic: common `7`, spec `8`, total `15`, pass. Pessimistic: common `3.5`, spec `4`, total `7.5`, fail.

## 2024 podzim

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Complement of regex language | 3/2.5/2 | none |
| 2 | Type representation and visitor | 2/1.5/0.5 | [IMPL] full class/interface declarations and traversal code |
| 3 | Primitive functions and integration per partes | 2.5/2/1 | [COMP] definite integration execution |
| 4 | Graph coloring | 3/2.5/2 | none |
| 28 | Minimax and alpha-beta | 2.5/2/1 | [COMP] hand alpha-beta tree evaluation |
| 29 | Logistic regression | 3/2.5/2 | none |
| 30 | Binary classifier evaluation | 3/2.5/2 | none |
| 31 | Decision tree | 2.5/2/1 | [COMP] information-gain arithmetic and pruning example |

Totals: common `A 10.5`, spec `A 11`, total `A 21.5`, pass. Realistic: common `8.5`, spec `9`, total `17.5`, pass. Pessimistic: common `5.5`, spec `6`, total `11.5`, fail by total/spec.

## 2025 jaro

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Intersection of CFL and regular language | 2.5/2/1 | [COMP] product PDA construction detail |
| 2 | Matrix library, sparse matrix, factory | 1.5/1/0.5 | [IMPL] sparse formats, API implementation, factory code |
| 3 | Matrices, kernel, similarity, diagonalization | 2.5/2/1 | [COMP] eigenvalue and kernel computations |
| 4 | Eulerian graphs | 2.5/2/1 | [COMP] custom graph degree/connectivity derivation |
| 27 | DPLL and perfect matching encoding | 2.5/2/1 | [COMP] SAT encoding for perfect matching is not explicit |
| 28 | k-nearest neighbors | 3/2.5/2 | none |
| 29 | Logistic regression derivation | 3/2.5/2 | none |
| 30 | Bayesian learning | 2.5/2/1 | [COMP] posterior and Bayes-optimal prediction arithmetic |

Totals: common `A 9`, spec `A 11`, total `A 20`, pass. Realistic: common `7.5`, spec `8.5`, total `16`, pass. Pessimistic: common `3.5`, spec `6`, total `9.5`, fail.

## 2025 leto

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | DFA language construction | 2.5/2/1 | [COMP] prefix/suffix automaton construction |
| 2 | Simple heap allocator | 1/0.5/0 | [IMPL] byte-level allocator implementation and hexdump |
| 3 | Scalar product and positive definiteness | 2.5/2/1 | [COMP] Sylvester/Cholesky execution |
| 4 | Central limit theorem | 2.5/2/1 | [COMP] normal approximation arithmetic |
| 29 | Bellman utility equation | 2.5/2/1 | [COMP] policy-evaluation equation system details |
| 30 | Linear regression | 2.5/2/1 | [COMP] explicit solution vs SGD comparison is present but light on SVD/validation detail |
| 31 | K-means | 3/2.5/2 | none |
| 32 | EM algorithm | 2/1.5/0.5 | [COMP] one EM parameter update for a Bayesian-network model is not worked out |

Totals: common `A 8.5`, spec `A 10`, total `A 18.5`, pass. Realistic: common `7`, spec `8`, total `15`, pass. Pessimistic: common `3`, spec `5.5`, total `8.5`, fail.

## 2025 podzim

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | P, NP, reductions, NP-completeness | 3/2.5/2 | none |
| 2 | Binary file reader | 1/0.5/0 | [IMPL] complete binary parser design, offsets, endian conversion |
| 3 | Analysis and area minimization | 2.5/2/1 | [COMP] derivative/minimization execution |
| 4 | Binary relations | 2.5/2/1 | [COMP] counting equivalence relations and constructing counterexamples |
| 27 | One-shot games | 2.5/2/1 | [COMP] payoff-matrix analysis beyond definitions |
| 28 | Binary classifier evaluation | 3/2.5/2 | none |
| 29 | Tabular-data prediction | 2/1.5/0.5 | [ML-FORMULA] MAE/RMSE and preprocessing recipes are not fully in notes; [ALGO] gradient boosting/XGBoost absent |
| 30 | Linear regression and L2 regularization | 2.5/2/1 | [COMP] OLS/ridge graph and coefficient-direction reasoning |

Totals: common `A 9`, spec `A 10`, total `A 19`, pass. Realistic: common `7`, spec `8`, total `15`, pass. Pessimistic: common `4`, spec `5.5`, total `9.5`, fail.

## 2026 jaro

| Q | Topic | A/R/P | Gap on lost points |
|---|---|---:|---|
| 1 | Modular-hash DFA | 2.5/2/1 | [COMP] parametric automaton construction with modular arithmetic |
| 2 | Process-to-process semaphore stream | 2/1.5/0.5 | [IMPL] exact send/receive code and semaphore invariants |
| 3 | Matrix row space, determinant, Gram-Schmidt | 2.5/2/1 | [COMP] Gram-Schmidt arithmetic |
| 4 | Planar graphs | 2.5/2/1 | [COMP] triangulation edge counts and existence construction |
| 27 | CSP and AC-3 | 2.5/2/1 | [COMP] step-by-step AC-3 domain pruning |
| 28 | K-means convergence | 3/2.5/2 | none |
| 29 | Model combinations and ensemble accuracy | 2.5/2/1 | [COMP] correlation/disjoint-error reasoning for ensemble accuracy |
| 30 | Decision tree | 2.5/2/1 | [COMP] entropy/Gini arithmetic and pruning |

Totals: common `A 9.5`, spec `A 10.5`, total `A 20`, pass. Realistic: common `7.5`, spec `8.5`, total `16`, pass. Pessimistic: common `3.5`, spec `5.5`, total `9`, fail.

## Gap catalog

| Category | Gap | Frequency | Recommendation |
|---|---|---:|---|
| [IMPL] | Code-level API/class design, callbacks/visitor/factory, OO modeling, concrete declarations | 11 | fill |
| [IMPL] | Byte-level implementation: endian parsing, heap allocator, sparse matrix storage, toy CPU/emulator/driver code | 10 | fill if common informatics risk matters |
| [IMPL] | Semaphore/thread code with exact schedules, invariants, locks, race fixes | 5 | fill |
| [COMP] | Automata/PDA/CFG construction for novel languages, product constructions, modular automata | 11 | fill |
| [COMP] | Linear algebra hand computations: kernels, diagonalization, bases, Gram-Schmidt, OLS matrices | 10 | fill |
| [COMP] | Calculus/probability/statistics computations: integrals, derivatives, CLT, HMM, chi-square/t-tests | 9 | fill |
| [COMP] | Graph proof/application computations: Menger, Eulerian/planar counts, coloring, matching | 8 | fill |
| [COMP] | ML arithmetic: entropy/information gain, K-means centroids, Bayes posterior, EM updates, PCA/SVM geometry | 13 | fill |
| [ALGO] | Specific algorithms absent or only sketched: k-way merge, two-array median, SCC/topological variants, heap/MST details | 8 | fill |
| [ALGO] | Gradient boosting/XGBoost/LightGBM and practical tabular-model recommendations | 1 | optional |
| [ML-FORMULA] | MAE/RMSE and practical regression metric set beyond MSE | 1 | fill |
| [DEF] | Exact old-style state diagrams, Hall/perfect matching, some theorem statements in exam wording | 4 | optional |
| [SCOPE] | Databases, networking, graphics, LP/optimization, coding theory, web, NLP/deep learning UI-ZPJ-only | many ignored | skip-out-of-scope |

## Overall summary

For the 9 current full or near-current UI-SU simulations from 2023-leto through 2026-jaro, the average totals are approximately:

| Scenario | Average total out of 24 | Passes among 9 full simulations |
|---|---:|---:|
| Achievable | 20.1 | 9/9 |
| Realistic | 16.2 | 9/9 |
| Pessimistic | 9.9 | 0/9 |

Estimated notes-only pass probability: about 70 percent for a student who genuinely mastered the notes. The notes are strong enough for conceptual AI/ML and common theory, but the pass margin depends heavily on not drawing an implementation-heavy common informatics question and not losing too much on arithmetic-heavy subparts.

Highest-value gaps to fill:

1. Implementation drills for common informatics: binary parsing, small allocators, semaphore code, visitor/factory/class declarations.
2. Automata and PDA construction practice: product constructions, custom language automata, modular/state-tracking DFAs.
3. ML computation drills: decision-tree entropy, K-means by hand, Bayes posterior/Bayes-optimal prediction, EM one-step update.
4. Linear algebra and graph computation drills: Gram-Schmidt, diagonalization, OLS matrices, Menger/Euler/planarity counts.
5. Practical tabular ML: MAE/RMSE, one-hot encoding, normalization, random forests vs boosting, basic model-selection language.
