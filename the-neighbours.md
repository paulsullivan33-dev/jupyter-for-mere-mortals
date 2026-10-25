# The Neighbours

Notebooks sit in a crowded
neighbourhood of ways to work with
code and data. Each neighbour trades
something Jupyter keeps for something
Jupyter lacks.

## Plain scripts and a text editor

The program itself, no intermediary:
a `.py` file, run whole, top to
bottom, every time. **Trades away**
the conversation — no poking at a
half-loaded table, no answers kept
beside questions — **for**
certainty: what you see is literally
all that ran. The mature workflow
uses both: explore in a notebook,
graduate the findings to scripts
(chapter 11), keep the notebook as
the record. Anyone who tells you to
pick one side forever is selling
something.

## VS Code and other editor notebooks

Microsoft's VS Code (and several
other editors) open `.ipynb` files
natively and speak to the same
kernels. Same documents, same state
rules — chapter 8 applies word for
word — with the furniture of a
programmer's editor around them:
better text editing, debugging,
version control in the same window.
The server in the middle is arranged
differently, but nothing in this
guide's mental model changes. If you
live in an editor already, this is
the lowest-friction door into
notebooks.

## Hosted notebooks (Colab and friends)

Google's Colab and its kin run the
server and kernel on someone else's
machine, free or rented, in a
browser tab: nothing to install,
real computing power an arms-length
away, easy sharing by link.
**Trades away** custody — your data
travels to their machines, the
environment is theirs (versions
change when they say), and a
notebook that only runs there is a
dependency, not a document. Splendid
for a first afternoon and for
borrowing a big machine; a poor
place to keep the only copy of
anything.

## R Markdown and Quarto

The publishing-first branch of the
family: documents written prose-first
with code woven in, rendered by
**Quarto** (or knitr, in R's world)
to polished HTML, PDF, and books.
Notebooks are code-first documents
that render adequately; Quarto
documents are manuscripts that
compute. If the deliverable is a
finished report or a book and the
exploration is done, Quarto is the
stronger tool — and it will happily
execute this guide's notebooks as
inputs, which tells you the two are
stages of one workflow more than
rivals.

## The spreadsheet

For a table of numbers with formulas
that must always be current and a
reader who will never read code, the
spreadsheet still wins outright —
chapter 1 said why: it recalculates
everything, always. Notebooks win
when the data is big, the questions
change, the steps need explaining,
or the same job must run again next
month on a new file. Most real work
contains both shapes; recognising
which part is which is most of the
skill this guide exists to teach.
