# Limits

Plainly stated, the edges of the
tool — several of them met before,
collected here so they can be found
again.

**A notebook is not a program.**
Ordering, hidden state, stale
outputs — the whole of chapter 8.
The limit underneath every other
limit: a notebook's answers are
only as trustworthy as the
discipline of its last run.

**Big data outgrows the
conversation.** A kernel holds its
tables in memory, in one process,
on one machine. Files of a few
hundred megabytes are comfortable;
past a few gigabytes the
load-it-and-poke-it style stops
working, and the right move is a
tool that queries data where it
lives — a database, or a streaming
library — with the notebook demoted
to asking small questions and
showing small answers. That is a
legitimate pattern, but it is a
different book from this one.

**Not a deployment shape.** A
notebook server is an interactive
workshop. It is not how you serve a
website, run a business's nightly
pipeline, or take requests from the
public: those want programs,
schedulers, and services, with
notebooks upstream as the place the
logic was worked out. Scheduled
*executions* of a fixed notebook
(chapter 10) sit honestly on the
border — fine for a report nobody's
pay depends on, and a smell past
that.

**Concurrency is one pair of hands.**
A kernel runs one cell at a time,
and a notebook assumes one editor
at a time. Two people in one
notebook is two cursors in one
document and one shared memory —
possible in hosted tools, awkward
everywhere, and never the
collaboration it looks like. The
unit of sharing is the file,
passed back and forth, or the
export, read by many.

**Reproducibility has a floor.**
Chapter 8's ritual makes a notebook
re-runnable on *an* environment.
Making it re-runnable on *any*
environment — same library versions,
same everything — needs environment
machinery (pinned requirements,
containers) that this guide only
points at. A notebook plus "it
worked in June" is not a
reproducible result, however clean
its counts.

**The security shape is fixed.**
A Jupyter server exists to run code.
There is no read-only mode worth
the name for the living file, no
sandbox per cell, no permission
system inside a notebook. Every
deployment decision in chapter 12
flows from accepting that, not
from configuring around it.
