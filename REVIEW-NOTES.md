# Review notes

Cross-review notes for `src/sections/strojove-uceni.tex` and `src/sections/zaklady-ui.tex`.
Only high-confidence factual/clarity corrections were applied directly. Items below are lower-priority or stylistic, so I left the source text unchanged.

## `src/sections/zaklady-ui.tex`
- The MDP Bellman equation uses a transition reward `R(s,a,s')`. Some courses use state reward `R(s)` or action reward `R(s,a)`. The text is correct under its stated convention, but an examiner may use a different notation.
- The second-price auction note says truthful bidding is a dominant strategy in a simple model. This is correct for the standard sealed-bid Vickrey auction with private values, but not a universal fact about every auction informally called "second price".

## `src/sections/strojove-uceni.tex`

- The softmax formula omits explicit conditioning and parameters for brevity. It is fine for exam prep, but a precise version would write `P(y=k\mid x)=...`.
- The hierarchy clustering sentence says `k` is not needed in advance. This is useful intuition because the dendrogram can be cut later, but a final flat clustering still needs a cut level or chosen number of clusters.

## Final pass - 2026-06-08

High-confidence factual and consistency fixes were applied directly. Remaining debatable points:

- The text intentionally keeps several theorem statements compressed for grade-3 exam prep. Examples: Menger's theorem omits the full set-version statement; A* and UCS conditions are stated only at the level needed to avoid the usual exam traps.
- The normal-equation formula in the cheat sheet assumes the intercept has been folded into `X` by a column of ones, as stated in the body.
- The t-test paragraph now mentions independence, rough normality, and Welch's unequal-variance variant, but does not list all small-sample diagnostics or nonparametric alternatives because that would add depth outside the pass-oriented scope.
