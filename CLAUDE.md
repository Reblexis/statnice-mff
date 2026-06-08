# CLAUDE.md - statnice-mff

Project guidance for Claude Code. Read this first when working in this repo.

## Point of this repo

Build one polished Czech study PDF (`statnice-priprava.pdf`) to prepare for the
MFF UK bachelor state final exam (statnice), program **Informatika - Umělá
inteligence**, zaměření **Strojové učení**. The PDF must cover every required
exam topic, stay faithful to the source notes, and clearly mark anything that is
missing, only an alternative, or left to self-practice.

**Primary objective: learn as time-efficiently as possible.** Optimize for the
LEAST study time needed to reliably PASS, i.e. reach grade 3 ("dobře", the lowest
passing grade) with > 98 % probability. This supersedes any "get an A" framing:
maximizing the grade is not the goal, minimizing time-to-pass is. Practical
consequences for how to shape the material:

- Pass thresholds (see "Struktura zkoušky" in the PDF): at least 5 points from
  the common areas AND at least 7 from the specialization; 12 points total = grade 3.
  Prioritize broad, shallow coverage that secures these minimums over deep mastery
  of any single topic.
- Favor crisp definitions, key statements, and the one-line "why" over long
  derivations and proofs (the exam has přehledový charakter anyway).
- Keep it lean: do not add depth or topics beyond the requirements. Anything that
  does not move the needle on passing is bloat and should be cut.
- When trimming or expanding, ask "does this raise the probability of passing per
  minute of study?" If not, leave it out.

Owner: Viktor Číhal. GitHub account: **Reblexis** (private repo
`github.com/Reblexis/statnice-mff`). Local unix user is `cihalvi`.

## Approach (current)

The deliverable is a LEAN, hand-authored study PDF (not a verbatim copy of the
notes). Each topic is REWRITTEN for clarity/intuition and laid out by a fixed
template (see `src/sections/*`): a gray `tema` box with the official requirement
VERBATIM, then `\ucivo` explanation, an `intuice` box, a TikZ diagram where it
helps, an `odpoved` answer-ladder (1/2/3 points), a `recall` box, and a `\past`
trap line. Goal: minimum time to pass. notes-ipp is now only a reference, not the
source of the text.

## What is stored where

```
pozadavky/
  detailni-pozadavky.pdf   <-- AUTHORITATIVE source of truth (official MFF
                               "Témata bakalářské SZZ", v2025-07-28). Anchor to this.
  SZZ_strojove_uceni.pdf, mff_statnice_...pdf   condensed derived overviews
notes-ipp/                 git submodule (vitkolos/notes-ipp). REFERENCE only now;
                           do NOT edit the submodule.
src/
  main.tex       the lean deliverable: title, strategy, scope, then \input sections/*
  preamble.tex   packages + ALL design macros (tema, defbox, intuice, odpoved+\bod,
                 recall, \past, \priorita; infobox/gapbox; tikz+pgfplots). Edit
                 design here; do not redefine macros in sections.
  sections/
    zaklady-ui.tex       Část III (authored; co-authored with Codex)
    strojove-uceni.tex   Část IV (authored)
    (spolecna-matematika.tex, spolecna-informatika.tex  = TODO, common areas)
  build.py, parts/, audit.tex   LEGACY notes->LaTeX pipeline (superseded by
                 sections/; kept only in git history if removed). Not used by main.
STRATEGY.md          agreed pass strategy (synthesis of Claude + Codex)
STRATEGY-CODEX.md    Codex's raw strategy analysis
CODEX-REVIEW.md      Codex's earlier coverage verification of the old doc
statnice-priprava.pdf  the deliverable (committed at repo root)
Makefile, README.md, .gitignore
```

## Build order / status
Specialization first (it carries the 7/12 floor): Část III + IV are done. Common
math + informatika (Část I + II) are TODO in the same template, lighter depth.

## Exam scope (what to include / exclude)

For zaměření Strojové učení the exam covers ONLY: společná matematika (6),
společná informatika (4), Téma 1 = Základy UI, Téma 3 = Strojové učení. The PDF
contains exactly these four parts. Deliberately OUT of scope (do not add):
Robotika (Téma 2), NLP (Téma 4), all other specializations; therefore no neural
nets / deep learning, networks, databases, RSA/FFT, computational geometry, etc.
The scope box is in `main.tex` (`\ref{sec:rozsah}`).

## Build

```bash
make            # latexmk on src/main.tex; outputs statnice-priprava.pdf
make distclean  # remove generated files
```
Requires TeX Live (pdflatex, latexmk, pgfplots, tikz). Engine is pdflatex with
UTF-8 + babel czech. After cloning, run `git submodule update --init --recursive`.

## Conventions / constraints

- Content is REWRITTEN for clarity (not copied from notes). It may differ from
  notes-ipp; correctness against the official requirements is what matters.
- Edit content in `src/sections/*`; edit shared design/macros in `preamble.tex`
  (do not redefine boxes inside sections).
- NO en-dashes or em-dashes anywhere in prose (use a hyphen). WARNING: never run
  a blind `s/--/-/` over .tex - inside `tikzpicture` `--` is the path operator and
  must stay; only `-` belongs in prose. Check `pdftotext main.pdf - | grep` for
  dash chars after changes.
- Per topic use: `tema` (official verbatim) / `\ucivo` / `intuice` / TikZ diagram /
  `odpoved` ladder with `\bod{1..3}` / `recall` / `\past`. Specialization = full
  template; common math = lighter (tema + ladder).
- Stay in scope (see Exam scope). Specialization carries the 7/12 floor, so depth
  goes there; common areas only need breadth (5/12 floor).
- After any change, run `make`, confirm zero LaTeX errors AND zero dash chars in
  the PDF before committing.
- C# is the strongest language in the notes; if answering in Java, supplement Java.
