# The Notebook File

A `.ipynb` file is **JSON** — a text
format of lists, dictionaries, and
strings that any programming language
can read. You can open a notebook in
a plain text editor and understand
everything in it; no Jupyter required.
That ordinariness is a feature worth
a chapter, because it explains both
what notebooks are good at and the
one thing they are famously bad at.

## Anatomy

The file has three parts:

- **`metadata`** — the notebook's
  settings. Chief among them the
  **kernelspec** (which kernel this
  notebook asks for — the lab
  notebook's says `python3`, the bash
  notebook's says `bash`) and the
  language info.
- **`nbformat`** — two numbers, the
  format's version (the lab's files
  are 4.x, written by nbformat
  5.11.1). Tools check it before
  trusting the rest.
- **`cells`** — the list, in page
  order. Each cell is a dictionary:
  its `cell_type` (`code` or
  `markdown`), its `source` (a list
  of lines — your writing, verbatim),
  and for code cells an
  `execution_count` and `outputs`.

An output, in turn, is a dictionary:
an `output_type` (`stream`,
`execute_result`, `display_data`,
`error`) and the bundle of forms from
chapter 7 under a `data` key, one per
**MIME type** — `text/plain`,
`text/html`, `image/png`.

## A picture, as text

JSON holds text, so the plot's PNG
bytes ride inside the file as
**base64** — the picture spelled out
in letters and digits, about a third
larger than the picture itself. This
is the honest arithmetic behind the
lab notebook's sizes:

| State of the file | Bytes |
|---|---|
| Written, never run | 3,020 |
| Outputs cleared after running | 4,282 |
| Executed, plot stored twice (chapter 7) | 96,730 |

Ninety-some kilobytes is nothing —
until a notebook grows a dozen plots
and a habit of being emailed around,
at which point outputs are the file.
Clearing them is one command
(chapter 10 shows it), and many teams
clear before saving to version
control for exactly this reason.

## Why version control grumbles

Git and its kin compare files line by
line. A notebook's JSON spends most
of its lines on output machinery and
base64, so changing one number high
in a notebook can rewrite hundreds of
lines below it, and re-running a
notebook rewrites counts everywhere.
Diffs become noise; merges become
lotteries. The honest mitigations,
in rising order of machinery: clear
outputs before committing (the
answers are reproducible — chapter 8
made them so — so clearing loses
nothing but bulk); commit the
*exports* (chapter 11) alongside,
which diff beautifully; or use a
notebook-aware tool such as `nbdiff`
(from the nbdime project) that
compares cell by cell. What does not
work is pretending the problem away:
a repository of raw, output-laden
notebooks is a repository nobody can
review.

## Writing notebooks without Jupyter

Because the format is plain JSON, a
program can *author* one. The lab's
notebook was built by
`jupyter-lab/make_notebook.py` using
**nbformat**, the format's own
library: make cells, set the
kernelspec, write the file. Thirty
lines, fully reproducible, no
clicking. That is worth knowing even
if you never do it: report generators
and test harnesses build notebooks
exactly this way, run them with
chapter 10's tools, and file the
executed result as the report. The
notebook stops being a worksheet and
becomes an output format — one with
a rather good story, since it carries
its own evidence inside it.
