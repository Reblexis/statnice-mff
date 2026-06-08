# Review notes

Cross-review notes for `src/sections/strojove-uceni.tex` and `src/sections/zaklady-ui.tex`.
Only high-confidence factual/clarity corrections were applied directly. Items below are lower-priority or stylistic, so I left the source text unchanged.

## `src/sections/zaklady-ui.tex`

- The Bayes net factorization uses `parents(x_i)` in the formula. More standard notation is `pa_i` or values of `Parents(X_i)`. The current version is understandable and exam-safe.
- The MDP Bellman equation uses a transition reward `R(s,a,s')`. Some courses use state reward `R(s)` or action reward `R(s,a)`. The text is correct under its stated convention, but an examiner may use a different notation.
- The second-price auction note says truthful bidding is a dominant strategy in a simple model. This is correct for the standard sealed-bid Vickrey auction with private values, but not a universal fact about every auction informally called "second price".

## `src/sections/strojove-uceni.tex`

- The t-test assumptions are compressed to "roughly normal data". For a fuller answer, mention independent samples and, for the classical two-sample t-test, equal variances; Welch's t-test relaxes equal variances.
- The softmax formula omits explicit conditioning and parameters for brevity. It is fine for exam prep, but a precise version would write `P(y=k\mid x)=...`.
- The hierarchy clustering sentence says `k` is not needed in advance. This is useful intuition because the dendrogram can be cut later, but a final flat clustering still needs a cut level or chosen number of clusters.
