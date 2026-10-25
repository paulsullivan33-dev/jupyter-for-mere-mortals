# Kernels and Languages

A **kernel** is the program that runs
your cells. It is an ordinary,
long-running process: it starts when
you open a notebook, sits waiting
between cells, and holds — in its own
memory — every variable your cells
have made. The server never sees your
variables. The notebook file never
holds them either. They live in the
kernel, and only there.

That one fact explains most kernel
behaviour:

- **Restarting a kernel forgets
  everything.** The Restart button
  kills the process and starts a
  fresh one: same notebook, same
  cells, empty memory. The lab proved
  it by talking to a kernel directly
  (transcript t03):

  ```
  run  x = 41            -> (no output)
  run  print(x + 1)      -> 42
  --- kernel restarts ---
  run  print(x)          -> NameError: name 'x' is not defined
  ```

- **A busy kernel is busy.** While a
  cell runs, the kernel answers
  nothing else; the queue of cells you
  pressed Run on waits its turn.
- **Kernels are per notebook.** Two
  notebooks, two processes, two
  separate memories. Closing a
  notebook's tab does not stop its
  kernel — *Shutdown* does, from the
  file browser or the Kernel menu,
  and the distinction matters on a
  small machine: idle kernels are
  idle processes holding real memory.

## How the server finds kernels

A kernel announces itself with a
**kernelspec**: a folder containing
`kernel.json`, which names the command
that starts it. Ask what the server
can offer:

```bash
~/jupyter-venv/bin/jupyter kernelspec list
```

The lab's answer, before and after
chapter 3's extra install
(transcript t00):

```
Available kernels:
  python3    …/share/jupyter/kernels/python3
  bash       …/share/jupyter/kernels/bash
```

The Python kernelspec's `kernel.json`
says, in essence, "start this
environment's Python with
`-m ipykernel_launcher`" — which is
why *which* environment a notebook
runs in is decided by which kernel
starts it, and why "the package is
installed but the notebook can't
import it" almost always means the
package and the kernel live in
different environments (chapter 16
returns to this).

## A second kernel: the shell

The Python kernel is one program among
many because the contract is small:
accept code, run it, report back,
remember. `bash_kernel` implements it
for the shell itself. Registering it
was one command in the lab:

```bash
~/jupyter-venv/bin/python -m bash_kernel.install --sys-prefix
```

after which a notebook can choose
*Bash* as its kernel and its cells are
shell commands, with shell variables
persisting from cell to cell in
exactly the Python way. The lab's
two-cell proof (transcript t04) sets
a variable in cell one —

```bash
STATION=Millbrook
YEAR=2026
```

— and spends it in cell two:

```
The Millbrook diary, 2026
31
date,high_c,low_c,rain_mm
```

Same server, same document format,
same Execute machinery — a different
language behind the message protocol.
Kernels exist on the same pattern
for R, Julia, and dozens more; the
installation shape is always these
two steps: install the package, and
(if it doesn't happen automatically)
register its kernelspec.

## Switching and choosing

A notebook names its kernel in its
own metadata (chapter 9 shows where),
so a file remembers what it was
written for, and opening it starts
that kernel if it still exists. The
front ends let you switch a notebook
to a different kernel from the Kernel
menu — the state does not travel
with it; the new kernel starts empty,
and the old one's memory is gone.
Treat a kernel switch as a restart
that also changed the language.
