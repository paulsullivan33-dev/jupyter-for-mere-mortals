# What Jupyter Is

A notebook is a document with a
peculiar property: parts of it can be
*run*. The document is a list of
**cells**. Most cells are one of two
kinds:

- **Code cells** hold a few lines of
  code — a calculation, a question
  asked of some data.
- **Markdown cells** hold writing:
  headings, explanations, the story
  that connects the code.

Run a code cell and its result appears
directly underneath it, inside the
document, and *stays* there when you
save. A table comes back as a table. A
plot comes back as a picture. The file
you save holds the questions, the
answers, and your notes about both.
That is the whole idea, and it is
genuinely useful: a notebook is a lab
book that fills in its own results.

**Jupyter** is the machinery behind
the document. It has two halves, and
keeping them separate in your head
will save you most of the confusion
beginners meet:

- A **server** runs on your machine.
  You talk to it through a web browser —
  the browser is just the screen and
  keyboard. The server holds your
  files and passes work back and forth.
- A **kernel** is an ordinary program
  that runs your code. When you run a
  cell, the server sends its contents
  to the kernel; the kernel executes
  it, remembers any variables it made,
  and sends the result back to be
  written into the document.

The remembering matters. Run one cell
that loads a table of data, and the
next cell can use that table without
loading it again. A notebook is a
conversation with a program that has
a memory — which is exactly what makes
it pleasant for exploring, and exactly
what makes it treacherous in ways
chapter 8 spends itself on.

## The two front doors

The server offers two interfaces,
both shipped in this guide's install:

- **JupyterLab** is the fuller one:
  notebooks open in tabs alongside a
  file browser, a text editor, and
  terminals, like a small workshop.
- **Notebook** (the "classic" style,
  now in its version 7 form) is the
  plainer one: a file list, and one
  notebook open at a time, nothing
  else competing for attention.

Same server, same kernels, same
files. Which door you walk through
changes the furniture, not the work.
This guide uses the names loosely
except where the difference is the
point.

## What a notebook is not

- **Not a program.** A program is a
  list of instructions executed in
  order, top to bottom, every time.
  A notebook's cells can be run in
  any order, repeatedly, or not at
  all — and the document will happily
  show you answers that no top-to-
  bottom run would produce. Chapter 8
  is devoted to this.
- **Not a spreadsheet.** A spreadsheet
  recalculates everything whenever
  anything changes, so what you see
  is always current. A notebook shows
  you the results from whenever each
  cell last ran. Stale answers look
  exactly like fresh ones.
- **Not an app builder.** A notebook
  is a fine place to work something
  out and a poor place to ship it.
  When a piece of notebook code grows
  up, it moves into a script or a
  program (chapter 11 shows the
  export), and the notebook becomes
  the record of how it got there.

## Where it came from, briefly

The name is a homage to three
languages — Julia, Python, and R —
the scientific-computing trio the
project grew up around. The kernels
for those came first; the design
turned out to be language-agnostic,
and kernels now exist for dozens of
languages, the shell included
(chapter 5 runs one). The notebook
format itself is an open standard,
which is why other tools — editors,
code-hosting sites — can open the
same files.
