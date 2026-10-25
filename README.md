# Jupyter for Mere Mortals

A **notebook** is a document that holds
code, the results of running that code,
and your own writing about both — in
that order, in one file. You work in
small pieces called **cells**: run one,
look at what came back, write a sentence
about it, run the next. **Jupyter** is
the open-source machinery that makes
documents like that: a small server you
talk to through a web browser, and
behind it a **kernel** — an ordinary
program that actually runs your code
and remembers your variables between
cells. This guide explains notebooks
in those terms, how to install Jupyter
and run your first one, how kernels
work, how to work with real data and
draw real plots, how to turn a notebook
into a page or a program, and how to
share it — with the limits stated
plainly, including the big one, which
gets a chapter of its own: a notebook
is not a program, and treating it like
one is where almost all notebook
trouble comes from.

The lab behind this guide ran the real
thing: **JupyterLab 4.6.4** and the
classic **Notebook 7.6.3**, installed
with pip into a fresh virtual
environment on a small Linux machine
(Python 3.12.3). A working notebook
was built around a month of invented
weather readings: it loads a CSV file,
computes the month's shape, and draws
a plot — and it was exercised end to
end. It was executed without the
browser and its printed answers were
checked against an independent recount
from the CSV; its outputs were cleared
and the whole thing re-run from
nothing, producing identical results;
it was exported to an HTML page and to
a plain Python script, and the script
was run and its output compared word
for word. A second kernel — the shell
itself — was registered and drove the
same machinery. The server was started
headless and interrogated over HTTP,
token and all. One variable was even
killed on purpose, by restarting its
kernel, to prove where notebook state
really lives.

What the lab could not do, it did not
fake. There was no screen, so clicking
through the JupyterLab and Notebook
interfaces is taught from the
documentation and labelled as such
wherever it appears; everything the
chapters claim about behaviour —
execution, outputs, kernels, exports,
the server — was proven at the command
line and over HTTP against the real
install, which is possible because the
browser screens and the command-line
tools drive the same server. Sharing a
server with a whole class or team
(JupyterHub) is likewise documented
only. `criteria.md` keeps the full
ledger of what was run and what was
only read.

## What this guide covers

- [**What Jupyter is**](what-jupyter-is.md) —
  the mental model: a document of cells,
  some code and some writing, with the
  answers kept inside; what a notebook
  is not (a program, a spreadsheet, an
  app)
- [**The moving parts**](the-moving-parts.md) —
  the server, the kernel, the two front
  ends, the notebook file, and the
  command-line tools: what each holds,
  and what breaks when each stops
- [**Installing Jupyter**](installing-jupyter.md) —
  the virtual environment, the pip
  install, checking the pieces, and
  where everything lands on disk
- [**Your first notebook**](your-first-notebook.md) —
  starting the server, the token in the
  address, cells, running them, saving,
  and the notebook the lab built
- [**Kernels and languages**](kernels-and-languages.md) —
  what a kernel actually is, how the
  server finds them, the bash kernel as
  a second example, and what a restart
  really does
- [**Working with data**](working-with-data.md) —
  loading a CSV with pandas, asking it
  questions, and reading the answers the
  notebook shows you
- [**Plots and rich output**](plots-and-output.md) —
  tables that render as tables, plots
  that live inside the file, and the
  several forms one result can take
- [**Not a program**](not-a-program.md) —
  the chapter to read twice: state,
  out-of-order cells, hidden answers,
  and the restart-and-run-all habit
  that keeps a notebook honest
- [**The notebook file**](the-notebook-file.md) —
  a `.ipynb` opened up: JSON, cells,
  outputs, a picture stored as text,
  and why version control grumbles
- [**Running without the browser**](running-without-the-browser.md) —
  `jupyter execute` and nbclient: whole
  notebooks run from the command line,
  including the run that leaves no
  trace at all
- [**Converting and sharing**](converting-and-sharing.md) —
  nbconvert to a web page and to a
  plain script, what each keeps and
  what each drops, and how other
  people read what you made
- [**Running it for real**](running-it-for-real.md) —
  a password instead of a token, the
  config file, reaching the server from
  another machine, and the safety talk
  that is not optional
- [**Recipes**](recipes.md) — a monthly
  report from a CSV, a notebook as a
  lab book, a parameterised run, and
  tidying a notebook for sharing
- [**The neighbours**](the-neighbours.md) —
  scripts and editors, VS Code's
  notebooks, hosted notebooks, and
  Quarto: what each trades away
- [**Limits**](limits.md) — big data,
  real-time work, production pipelines,
  and the notebook-shaped holes it is
  not worth forcing
- [**Troubleshooting**](troubleshooting.md) —
  the kernel that will not start, the
  cell that "did nothing", the import
  that fails in the notebook but not
  the terminal, and the traps this
  guide's lab fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

JupyterHub — one server shared by a
class or a team, with logins and
per-user machinery — is its own
subject and gets a pointing-at, not a
tutorial. So do the hundreds of
extension packages, the widget system
(ipywidgets) beyond a mention, and
debugging inside cells. Teaching any
particular language or library —
Python, pandas, plotting — is pointed
at too: this guide teaches the
notebook, using small pieces of those
as its examples. Hosting a notebook
server on the public internet gets a
warning and a safer shape, not a
walkthrough.

## How to use this guide

Read chapter 1 for the model and
chapter 2 before installing anything —
knowing which part holds what turns
later confusion into a named problem.
Chapters 3 and 4 get a notebook
running in one sitting. Chapter 8,
*Not a program*, is not the optional
chapter: read it before your second
notebook, not after your first
mysterious wrong answer. Chapter 12
is the other one not to skip if the
server will ever be reachable from
another machine. The lab's transcripts
live in `jupyter-lab/transcripts/`;
its notebook and data are
`jupyter-lab/fixtures/`; its notes are
`examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Python for Mere Mortals](https://paulsullivan33-dev.github.io/python-for-mere-mortals/)
- [DuckDB for Mere Mortals](https://paulsullivan33-dev.github.io/duckdb-for-mere-mortals/)
- [SQL for Mere Mortals](https://paulsullivan33-dev.github.io/sql-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/jupyter-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/jupyter-for-mere-mortals/blob/main/LICENSE-CODE).
