# Running Without the Browser

Everything the browser does — start a
kernel, feed it cells in order,
collect outputs into the file — can
be done from the command line. This
is more than a convenience. It is how
a notebook gets *checked*: by a
fresh kernel, in page order, with
nobody's memory involved, exactly
the standard chapter 8 demands.

## jupyter execute

```bash
~/jupyter-venv/bin/jupyter execute --inplace weather-lab.ipynb
```

executes every cell in the file and
writes the outputs back into it. The
engine underneath is **nbclient**,
which starts the kernel named in the
notebook's metadata, runs the cells
top to bottom, and stops at the first
error. The lab's run took about ten
seconds, most of it the kernel and
libraries starting (transcript t01);
what it wrote was then checked
against an independent recount from
the CSV, and every number matched.

Two flags decide where results go,
and the lab learned their importance
the memorable way (transcript t90).
With `--inplace`, the executed
notebook overwrites the input. With
`--output NAME`, it is written to a
new file. With **neither**, in the
version the lab ran (nbclient
0.11.0), the notebook still executes
— kernel starts, cells run, ten
seconds pass — and the result is
**quietly discarded**. No error, no
file. A scheduled job built on the
bare command would report success
forever while producing nothing. Run
one bare execution yourself and look
for the missing file; it is the
cheapest lesson in this guide.

## Clearing outputs

The reverse operation, through
nbconvert:

```bash
~/jupyter-venv/bin/jupyter nbconvert --to notebook \
  --ClearOutputPreprocessor.enabled=True \
  --output cleared.ipynb weather-lab.ipynb
```

The lab's file went from 96,730 bytes
of answered notebook to 4,282 of pure
questions, every `execution_count`
back to nothing (transcript t02).
Re-executing the cleared copy from a
cold kernel then reproduced the
original's printed output
*identically* — the reproducibility
proof in full: clear, run, compare.

Two more switches earn their keep in
scripts: `--allow-errors` (keep going
past a failing cell and file the
errors as outputs — right for a
health-check notebook, wrong for a
report) and `--timeout` (a ceiling in
seconds per cell, so one stuck cell
cannot hang a nightly run forever).

## Safety, plainly

Executing a notebook **runs code** —
the code in every cell, as you, with
your permissions. A notebook from a
stranger is a program from a
stranger, except friendlier-looking.
The lab's kernel printed a warning of
its own about this during scripted
runs: the server–kernel conversation
travels over local sockets without
encryption by default. On a single
machine that is a reasonable trade;
it is one more reason chapter 12
treats a reachable Jupyter server
with respect.
