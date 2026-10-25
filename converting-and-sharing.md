# Converting and Sharing

A notebook file is readable by anyone
with Jupyter and a working copy of
your environment — a smaller set of
people than it sounds. **nbconvert**
exists to widen the audience: it
transforms a notebook into formats
that need nothing but a browser, or
nothing at all.

## To a web page

```bash
~/jupyter-venv/bin/jupyter nbconvert --to html weather-lab.ipynb
```

One self-contained HTML file comes
out — the lab's weighed 379,927
bytes — with the writing formatted,
the code shown, and the outputs
already rendered inside it,
including the plot, carried as data
in the page (transcript t05). The
recipient needs no Python, no
Jupyter, no data file. This is the
format for *sending a result*: a
report, an attachment, a page on an
internal site. Its honesty is
chapter 8's though — HTML shows
whatever outputs were in the file,
fresh or stale, so convert *after*
the restart-and-run-all, never
instead of it.

## To a program

```bash
~/jupyter-venv/bin/jupyter nbconvert --to script weather-lab.ipynb
```

produces `weather-lab.py`: the code
cells in order, the Markdown cells
as comments, the magics (if any)
translated. The lab ran its export
as an ordinary program, and its
output was **identical, word for
word, to the notebook's recorded
printed output** (transcript t05).
Two honest caveats. What a script
keeps is the *printed* story: rich
displays — the notebook's habit of
showing a cell's final value —
become silent expressions in a
script, which prints nothing unless
told. And the script inherits the
notebook's order-dependence: it is
the cells in page order, which is a
fine program exactly when the
notebook was a disciplined one.

The script export is also the
growth path: when notebook work
turns into a tool other people rely
on, export it, then edit the result
into a real program — functions,
arguments, no leftovers. The
notebook remains the lab book that
explains where the program came
from.

## Other doors

- **PDF** — nbconvert can aim at PDF,
  through one of three engines
  (a LaTeX installation, or a
  headless browser printing the
  HTML). None was installed in the
  lab, so this guide does not
  pretend to have tested it; expect
  the HTML route plus a browser's
  Print-to-PDF to be the path of
  least resistance.
- **Slides** — mark cells as slides
  and nbconvert builds a slideshow
  page. A fine party trick that is
  occasionally exactly right for a
  results talk.
- **Just the file** — code-hosting
  sites render `.ipynb` directly in
  the browser, outputs and plots
  included, and services like
  nbviewer do the same for a file
  anywhere on the web. Sharing a
  link beats sharing an attachment
  when the notebook lives somewhere
  public anyway.

## Sharing the living thing

Sending the `.ipynb` itself shares
the *worksheet*, not just the
result: the recipient can re-run,
change a number, ask their own
questions. That is the right gift
for a collaborator and the wrong one
for an audience, because it asks
them to reproduce your environment —
the same libraries, the data files
beside the notebook, a kernel that
matches. If you send the living
thing, send the data with it and say
what to install (chapter 3's list,
in the lab's case). And re-run it
clean first. Always re-run it clean
first.
