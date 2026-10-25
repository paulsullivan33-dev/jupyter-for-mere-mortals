# Recipes

Four jobs notebooks are genuinely
good at, each built from the pieces
the earlier chapters verified.

## A monthly report from a CSV

The shape of chapter 6, repeated
forever: a file that arrives monthly,
a notebook that reads whatever
`sales.csv` currently holds, a set
of questions, a plot. Keep the
notebook and the data in one folder;
each month, drop in the new file,
restart, run all, export the HTML
(chapter 11) as the report. With the
repo's other fixture — a bookshop's
week of sales, `book-sales.csv` —
the same skeleton answers shop
questions instead of weather ones:

```python
sales["total"] = sales["copies"] * sales["price_each"]
by_title = sales.groupby("title")["total"].sum().sort_values(ascending=False)
```

The notebook is the template; the
CSV is the month's input; the HTML
is the deliverable. When the
questions stabilise and the monthly
ritual becomes a chore, that is the
sign to graduate the notebook to a
script (chapter 11) and schedule it
— notebooks you still *read* belong
in notebooks.

## A notebook as a lab book

Keep one notebook per investigation,
dated in its first Markdown cell,
with the question written before the
code and the conclusion written
after the results. Because outputs
live in the file, the book is
self-evidencing: six months later
the question, the attempt, and the
answer are one document. The lab's
restart demonstration began life as
exactly such a note —
`jupyter-lab/restart_demo.py` is the
script the chapter 5 experiment was
rehearsed with. Two rules keep a lab
book trustworthy: never delete a
failed attempt (annotate it and move
on — the failure is data), and run
the chapter 8 ritual on any entry
whose numbers you quote elsewhere.

## A parameterised run

When the same notebook must run
against several inputs, put the
changing values in one cell at the
top, tagged `parameters` (in Lab:
the cell's property inspector; in
the file: cell metadata —
chapter 9's territory). Tools in
the **papermill** family then inject
different values from the command
line and file each executed notebook
as a separate record: one weather
notebook, twelve monthly files, no
hand-editing. Papermill wasn't in
the lab's install, so this is a
described recipe rather than a
demonstrated one — but the
precondition it relies on, clean
non-interactive execution, is
chapter 10's, and that one is
proven.

## Tidying a notebook for sharing

Before any notebook leaves your
machine: restart and run all
(chapter 8). Read it top to bottom
as a stranger — does the first
Markdown cell say what this is and
where the data comes from? Delete
the scratch cells that were only
ever for you; strangers read every
cell you ship. Check no output
contains something you didn't mean
to publish — a file path, a token,
a stray print of the whole table.
Then decide the format (chapter 11):
HTML for readers, the file itself
for collaborators, both for the
record. A notebook that passes this
recipe is also, not coincidentally,
one future-you can still understand.
