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

## What is stored where

```
pozadavky/
  detailni-pozadavky.pdf   <-- AUTHORITATIVE source of truth (official MFF
                               "Témata bakalářské SZZ", v2025-07-28, all
                               specializations). Anchor every decision to this.
  SZZ_strojove_uceni.pdf        condensed derived overview (same content)
  mff_statnice_...pdf           condensed derived overview (same content)
notes-ipp/                 git submodule = study notes by Vít Kološ
                           (github.com/vitkolos/notes-ipp). The PDF is built
                           FROM notes-ipp/statnice/*.md. Content is authoritative
                           study material; do NOT edit the submodule.
src/
  build.py     Markdown -> LaTeX converter. Reads notes-ipp/statnice/*.md,
               writes src/parts/*.tex. Also injects yellow "Procvičit" callout
               boxes (CALLOUTS dict) and drops dead cross-file links.
  preamble.tex packages, macros (\gt \lt \set \braket), list nesting, callout
               box definitions (practicebox / gapbox / infobox), styling.
  main.tex     master doc: title page, exam structure+grading, "Jak se
               efektivně učit", \input{audit}, then the 4 parts.
  audit.tex    hand-written coverage audit: scope section, per-topic checklist,
               practice spots, the Hilbert exception.
  parts/       GENERATED LaTeX from the notes. Do not hand-edit (overwritten by make).
CODEX-REVIEW.md  Codex's independent coverage verification.
statnice-priprava.pdf  the deliverable (committed at repo root).
Makefile, README.md, .gitignore
```

## Exam scope (what to include / exclude)

For zaměření Strojové učení the exam covers ONLY: společná matematika (6),
společná informatika (4), Téma 1 = Základy UI, Téma 3 = Strojové učení. The PDF
contains exactly these four parts. Deliberately OUT of scope (do not add):
Robotika (Téma 2), NLP (Téma 4), all other specializations; therefore no neural
nets / deep learning, networks, databases, RSA/FFT, computational geometry, etc.
Verified that the notes contain no out-of-scope topics. See `\ref{sec:rozsah}`
in audit.tex.

## Build

```bash
make            # build.py then latexmk; outputs statnice-priprava.pdf
make distclean  # remove all generated files
```
Requires TeX Live (pdflatex, latexmk) and Python 3. Engine is pdflatex with
UTF-8 + babel czech. After cloning, run `git submodule update --init --recursive`.

## Conventions / constraints

- The notes content is faithful and odborně unchanged. To change generated
  output, edit `build.py`, never `src/parts/*.tex` directly. To change scope,
  edit the requirement-derived audit, not the notes.
- NO en-dashes or em-dashes (the owner dislikes them). Use a hyphen. build.py
  already maps any source dashes to hyphens; keep authored .tex dash-free.
- Callout boxes: yellow `practicebox` = computational skill the notes leave to
  self-practice (not a gap); red `gapbox` = missing / alternative / out-of-scope;
  blue `infobox` = info/summary.
- After any change, run `make` and confirm zero LaTeX errors before committing.
- Coverage status: every required sub-topic is in the notes. Only Hilbert
  calculus is absent (an alternative to tablo/resolution, both covered). Seven
  spots are self-practice skills, all marked.
- C# is the strongest language in the programming-languages notes; if the exam
  answer will be in Java, supplement Java specifics.
