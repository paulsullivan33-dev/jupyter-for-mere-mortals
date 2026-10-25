# Not a Program

This is the chapter the whole guide
leans on. A notebook looks like a
program — code, in order, in a file —
and behaves like one just often enough
to earn your trust. It is not one,
and the differences are not quirks.
They are the design.

## A program has an order. A notebook has a history.

A program file means: *these lines,
in this order, from a cold start.*
That is all it can mean, and the
machine honours it every time.

A notebook means something weaker:
*these cells exist, and each output
in it is a record of the last time
that cell ran — in whatever order
life actually happened.* The kernel
remembers; you explore. You run cell
4, notice something, fix cell 2, run
it, run cell 5, run cell 4 twice.
The document shows five outputs.
Which sequence of kernel states
produced them? The document does not
say. *You* know, today. Next month
the notebook alone cannot tell you,
and a notebook whose answers depend
on an unrecorded history is not a
result — it is a rumour with good
formatting.

The notebook does keep one piece of
the history in plain sight: the
**execution counts**. `In [1]`,
`In [2]`, `In [3]` are the kernel's
own numbering of everything it has
run since it started, in the order
it ran them. Read a notebook's counts
before you read its answers:

- Counts that climb steadily down
  the page (the lab's are 1, 2, 3, 4)
  are consistent with a single
  top-to-bottom run.
- Counts out of order — a 7 above a
  3 — prove the cells were *not* last
  run in page order. The answers may
  still be right. They are not
  *shown* to be right.
- A gap (1, 2, 5) means other cells
  ran in between and were deleted,
  or this kernel served experiments
  that never made the page.
- A fresh `In [1]` low on the page
  means the kernel restarted there —
  everything above it belongs to a
  previous life.

## State is invisible

A program's inputs are written in the
file: files read, arguments passed.
A notebook's true input is the
kernel's memory — variables set by
cells since deleted, a library
imported in a cell now rewritten, a
table edited in place by three cells
that each looked harmless. Chapter 5
showed where that state lives and
how completely a restart erases it.
Nothing in the document lists it.
The classic notebook disaster is
therefore not an error message; it
is a *correct-looking answer* that a
fresh run cannot reproduce — the
colleague (often you, later) who
runs the notebook top to bottom and
gets different numbers, or a
`NameError` from a cell that "always
worked".

## The discipline that fixes it

None of this argues against
notebooks. Exploration *is*
out-of-order; that is its value. The
argument is for a closing ritual,
small and non-negotiable:

1. **Restart the kernel.** Empty the
   memory on purpose.
2. **Run all cells, top to bottom.**
   The front ends both have the
   command (Kernel → Restart & Run
   All; in classic Notebook, Cell →
   Run All after a restart).
3. **Read the counts.** They should
   climb 1, 2, 3 … without gaps or
   surprises.
4. **Only now believe the outputs** —
   and only now share the file.

A notebook that survives this is a
*result*: anyone's fresh kernel, fed
the cells in page order, reaches the
same answers. The lab held its own
notebook to exactly this standard
without the browser (chapter 10):
outputs cleared to nothing, the file
re-run from a cold kernel, and the
new answers compared against the
old — identical (transcript t02).

Two working habits support the
ritual. Keep cells small and
re-runnable: a cell that *adds* a
column can run twice safely, a cell
that *divides a column in place*
cannot (chapter 6 met both). And
load data in the open, in an early
cell, from files named in the
notebook — never from a state only
your kernel remembers.

Notebooks are where you find things
out. This chapter is how what you
found out stays true.
