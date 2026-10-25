# Glossary

**base64** — A way of spelling binary
data (a picture, say) in ordinary
text characters, at about a third
again the size; how plots ride inside
a notebook file (chapter 9).

**Cell** — One block of a notebook:
either code (run it) or Markdown
(read it). The unit of notebook work
(chapter 1).

**DataFrame** — pandas' table type:
named columns, typed values, one row
per record; what `read_csv` hands
back (chapter 6).

**Execution count** — The `In [n]:`
number beside a code cell: how many
things this kernel has run since it
started, and the number this cell
was. A notebook's diary of its own
history (chapter 8).

**Front end** — The web interface —
JupyterLab or Notebook — that draws
the cells and sends your Run presses
to the server. A screen, not a store
(chapter 2).

**ipykernel** — The Python kernel:
Python itself, wrapped to speak the
kernel message protocol (chapter 5).

**JupyterHub** — The multi-user
landlord: one login system spawning
a private Jupyter server per user.
Documented only in this guide
(chapter 12).

**JupyterLab** — The fuller of the
two front ends: notebooks, files,
editor and terminals in tabbed panes
(chapter 1).

**Kernel** — The long-running program
that executes a notebook's cells and
holds their variables in its memory.
One per open notebook; dies, and
forgets, on restart (chapter 5).

**Kernelspec** — The small folder and
`kernel.json` that tell the server
how to start a kernel:
`jupyter kernelspec list` shows the
ones on offer (chapter 5).

**Magic** — A line beginning with
`%`: a command to the notebook
system rather than to the language —
`%matplotlib inline` is the famous
one (chapter 7).

**Markdown** — The plain-text
formatting language of writing
cells: `#` headings, `*emphasis*`,
and prose that stays readable raw
(chapter 4).

**MIME type** — A label naming a
kind of content (`text/html`,
`image/png`). A result is stored as
one form per MIME type, and the
front end shows the richest it can
(chapter 7).

**nbclient** — The engine that
executes a notebook file from end to
end without a browser; what
`jupyter execute` drives (chapter
10).

**nbconvert** — The transformer:
notebook to HTML, to a script, to
other formats (chapter 11).

**nbformat** — Two jobs under one
name: the specification of the
`.ipynb` file format, and the
library that reads and writes it
(chapter 9).

**Notebook (the file)** — A `.ipynb`
file: JSON holding cells, outputs,
and metadata — questions, answers,
and writing in one document
(chapter 9).

**Notebook (the interface)** — The
classic, plainer front end; since
version 7 it shares the modern
codebase with Lab (chapter 1).

**Output** — What a run leaves in
the document under a cell: a stream
of printed text, a result, a display,
or an error (chapter 7).

**Server** — The program started by
`jupyter lab` / `jupyter notebook`:
serves the front end, guards the
door with token or password, starts
kernels (chapter 2).

**State** — Everything a kernel
remembers: variables, imports,
loaded tables. Invisible in the
document, erased by a restart
(chapters 5 and 8).

**Token** — The long random string
in the server's startup address: a
one-session password proving you
were the one who started it
(chapter 12).

**Virtual environment (venv)** — A
private folder of Python packages
with its own `python` and `pip`, so
one tool's libraries never fight
another's (chapter 3).
