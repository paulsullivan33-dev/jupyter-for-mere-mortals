# Plots and Rich Output

When a kernel runs a cell, the result
comes back not as one thing but as a
**bundle of forms** of the thing, and
the front end shows the richest form
it knows how to draw. One result, in
the lab notebook, exists in the file
like this:

- the `df.head()` table: a
  `text/html` form (a real little
  table, styled) and a `text/plain`
  form (the fixed-width text a
  terminal would show);
- the printed answers: a **stream**
  output — plain text, captured from
  what the code printed;
- the plot: an `image/png` form (the
  picture as bytes, encoded as text —
  chapter 9 looks at the encoding)
  and a `text/plain` form that merely
  names it,
  `<Figure size 800x300 with 1 Axes>`.

This is why the same notebook looks
polished in a browser and still makes
sense as text: every claim the
notebook makes is stored in a
plain form too, and tools that can't
draw can still read.

## Making the plot

The lab's picture is drawn with
matplotlib, the standard Python
plotting library, in the explicit
style:

```python
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(df["date"], df["high_c"], marker="o", label="High")
ax.plot(df["date"], df["low_c"], marker="o", label="Low")
ax.set_ylabel("Degrees C")
ax.legend()
fig
```

Build a **figure**, draw on its
**axes**, and end the cell with the
figure itself so the notebook
displays it. Readers who meet
notebooks elsewhere will also see the
older spelling, a first line
`%matplotlib inline` — a *magic
command* that chooses how figures are
delivered. Modern kernels deliver
figures inline by default, so the
lab's notebook omits it; the magic
still matters when you want a
different delivery (a separate
window, an interactive plot), and
magics generally — lines starting
with `%` — are small commands to the
notebook system rather than to
Python itself.

## An honest wart, kept

The lab's plot cell produced the
picture *twice* in the file: once as
the cell's result (because the cell
ends with `fig`, and a final
expression is a result) and once as
a display output (because the inline
delivery publishes every figure when
its cell finishes). The page shows it
once; the file, all 96 KB of it,
carries it twice. The fix, when file
size matters, is to end the cell with
a statement instead of the bare
figure — `plt.show()` states the
intent and stores it once. The lab
kept the duplication and this
paragraph instead of quietly fixing
it, because it's the kind of thing
you will meet in real notebooks and
wonder about.

## What outputs can be

The full menagerie, briefly: streams
(printed text, including the
red-tinted **stderr**), results (a
cell's final value), display outputs
(things a cell publishes mid-run — a
progress table, a second plot), and
**errors**, which arrive as a
traceback and stop nothing by
themselves: the kernel lives, later
cells can still run, and the
notebook will faithfully keep the
error in the document until the cell
is re-run. That last point surprises
script-thinkers twice over: an error
in a notebook is an *output*, filed
like any other, and a notebook full
of old errors and new successes is a
perfectly possible — and perfectly
confusing — document. Chapter 8
again: the counts and a clean
re-run are how you know which
outputs to believe.
