# Your First Notebook

Start the server from the folder you
want to work in — it can only see
that folder and below:

```bash
cd ~/notebooks
~/jupyter-venv/bin/jupyter lab
```

The command prints a short report and
an address like:

```
http://localhost:8888/lab?token=9f2c…(a long string of hex)
```

Open that address in your browser.
The **token** in it is a one-time
password the server generated at
startup and printed in its own log:
whoever has it controls the server,
and the server can run code as you —
so it is a real credential, not a
formality. Chapter 12 replaces it
with a password you choose. If port
8888 is taken, the server picks the
next free one and the printed address
says which; the address in the log is
always the true one. Stop the server
with Ctrl-C in its terminal.

For the classic interface instead,
the same folder and a different word:

```bash
~/jupyter-venv/bin/jupyter notebook
```

## Making a notebook

In the page that opens, create a new
notebook (Lab: the launcher's
*Notebook* tile; classic: *New* →
*Python 3 (ipykernel)*). A new notebook
is one empty code cell and a waiting
cursor. Type:

```python
print("hello from a cell")
```

and press Shift-Enter. Three things
happen: the cell runs, its output
appears beneath it inside the
document, and a fresh empty cell
opens below. The small number that
appeared beside your cell —
`In [1]:` — is its **execution
count**: this kernel has now run one
thing. Counts are the notebook's own
diary of what ran, in what order, and
chapter 8 teaches you to read them
with suspicion.

Add a Markdown cell (the cell-type
dropdown, or Esc then M in Lab's
command mode), write a heading and a
sentence, run it the same way: it
renders as formatted text. Save with
Ctrl-S and give the file a name. You
now own the whole loop every later
chapter uses: write, run, read, write
about what you read.

## The lab's notebook

The notebook this guide's lab built —
`jupyter-lab/fixtures/weather-lab.ipynb`
in the repo — asks questions of a
month of invented weather readings
(a CSV file, `weather.csv`, beside
it): eight cells, alternating writing
and code. It was written by a small
script rather than by clicking,
because a script is reproducible —
`jupyter-lab/make_notebook.py` is
kept in the repo and is worth a read
after chapter 9 — and it was first
run without the browser at all
(chapter 10 tells that story). But
nothing about it is special: the same
file opens in the browser like any
other, the cells run with the same
button, and its outputs — a table, a
set of printed answers, a plot — are
the ones chapters 6 and 7 take apart.
Open it, run it top to bottom, and
you have done everything this chapter
asks.

Check: your run's printed answers
should include *Hottest day:
2026-06-21 at 33 C* and *Total rain:
39.4 mm*. If they differ, the file
you have is not the file the lab
checked — see chapter 16.
