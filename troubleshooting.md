# Troubleshooting

Symptom → cause → fix, in rough
order of how often each one ruins
an afternoon.

## The answers are wrong and nothing errored

**Symptom:** numbers that don't
match a fresh pair of eyes, or a
colleague's run. **Cause:** almost
always chapter 8 — cells run out of
order, state left by deleted cells,
an in-place edit applied twice.
**Fix:** restart the kernel, run
all, compare. Read the execution
counts first; they usually confess
before you finish restarting.

## NameError for a variable the notebook "has"

**Symptom:** `NameError: name 'df'
is not defined` in a notebook that
plainly sets `df` higher up.
**Cause:** the kernel restarted (or
never ran that cell in this
session) — the definition exists on
the page, not in the memory.
Transcript t03 is this error,
manufactured on purpose. **Fix:**
run the defining cell; for the
whole notebook, restart and run all.

## A module imports in the terminal but not in the notebook

**Symptom:** `ModuleNotFoundError`
for a package you installed.
**Cause:** two environments — the
package went into one Python, the
kernel is another (chapter 5: the
kernelspec decides). **Fix:** ask
the notebook itself which Python it
is, in a cell —

```python
import sys; sys.executable
```

— and install the package with
*that* interpreter's pip, or pick
the kernel that matches the
environment you meant. The durable
fix is doing chapter 3's install so
the Jupyter environment and the
working environment are the same
one.

## The kernel won't start, or dies at once

**Symptom:** "kernel failed to
start", a dead-kernel notice, a
notebook that opens grey.
**Cause:** the kernelspec points at
an environment that moved or was
deleted; or the kernel's own
dependencies broke. **Fix:** check
the kernelspec's `kernel.json`
(chapter 5) names a Python that
still exists; start that Python by
hand and import `ipykernel` to hear
the real error in the terminal
rather than through the browser.

## The executed run that produced nothing

**Symptom:** a scripted
`jupyter execute` succeeds, and no
output file exists, and the
notebook is unchanged. **Cause:**
transcript t90 — in nbclient
0.11.0, without `--inplace` or
`--output`, the results are
discarded by default. **Fix:** name
the destination, every time, and
have the script check the output
file exists afterwards.

## The browser says the server isn't there

**Symptom:** connection refused on
localhost:8888, though the command
"ran". **Causes, in order:** the
server is running on a different
port (8888 was taken; the log
names the real one — use the
address the log printed); the
server exited — the lab's own
version (transcript t90) was
Jupyter refusing to run as the
root user without `--allow-root`,
a refusal ordinary users will
never trigger because they are
not root; or the token is stale
because the server restarted —
again, the current log is the
source of truth.

## A cell runs forever

**Symptom:** the asterisk
`In [*]:` never resolves.
**Cause:** the kernel is busy —
an infinite loop, a huge
computation, or a cell waiting for
input that a notebook cannot give.
**Fix:** Kernel → Interrupt first
(a polite stop); Restart if it
won't listen. Then find the cause
in a script or a smaller cell —
debugging inside a notebook is
possible but cramped, and chapter
14's neighbours do it better.

## The file is enormous

**Symptom:** a notebook of
megabytes for a few cells.
**Cause:** outputs — plots
especially, possibly stored twice
(chapters 7 and 9) — riding in the
file as base64. **Fix:** clear
outputs (chapter 10's command),
re-run if the answers must ride
along, and keep the data files
beside the notebook instead of
pasted into cells as literal text.
