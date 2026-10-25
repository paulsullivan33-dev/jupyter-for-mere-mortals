# Installing Jupyter

Jupyter is Python software, installed
with Python's package tool, `pip`. The
one decision that matters is *where*
it lands. Install it into a **virtual
environment** — a private folder of
Python packages with its own `python`
and `pip` — and the notebook world
stays in its box: upgrade it, break
it, delete it, and nothing else on
the machine notices. Installing into
the system Python works until the day
two tools want two versions of the
same library, and then it works
nowhere. The lab used a virtual
environment; so should you.

On a Debian or Ubuntu machine, the
environment machinery itself is one
package:

```bash
sudo apt install python3-venv
python3 -m venv ~/jupyter-venv
```

Then install into it. There is no need
to "activate" the environment if you
call its programs by their full paths,
which is the style this guide uses:

```bash
~/jupyter-venv/bin/pip install --upgrade pip
~/jupyter-venv/bin/pip install jupyterlab notebook
```

That is the headline. It pulls in the
server, both front ends, the Python
kernel, and the converters — in the
lab, some ninety packages all told.
Three more earn their place for this
guide's later chapters:

```bash
~/jupyter-venv/bin/pip install pandas matplotlib bash_kernel
```

`pandas` is the table-handling library
chapter 6 works with; `matplotlib` is
the plotting library of chapter 7;
`bash_kernel` is the second kernel of
chapter 5.

Check:

```bash
~/jupyter-venv/bin/jupyter --version
```

One command reports every piece. The
lab's answer (transcript t00):

```
IPython          : 9.17.1
ipykernel        : 7.4.0
jupyter_client   : 8.10.0
jupyter_server   : 2.21.1
jupyterlab       : 4.6.4
nbclient         : 0.11.0
nbconvert        : 7.17.2
nbformat         : 5.11.1
notebook         : 7.6.3
```

Your numbers will be newer; every
command in this guide works the same.
Two names in that list repay a second
look: `jupyter_server` is the actual
server both front ends share, and
`nbformat` is the library that reads
and writes notebook files (chapter 9
meets it again).

## Where everything lands

Inside the environment, three places
matter:

- `bin/` — the commands: `jupyter`,
  and under it the subcommands
  (`jupyter lab`, `jupyter execute`,
  `jupyter nbconvert`, …).
- `share/jupyter/kernels/` — one
  folder per kernel the environment
  knows about, each holding a small
  `kernel.json` that says what to
  start. Chapter 5 reads one.
- `lib/python3.12/site-packages/` —
  the libraries themselves.

Your own configuration and runtime
files live elsewhere, under your home
directory (`~/.jupyter`,
`~/.local/share/jupyter`) — which is
why deleting the environment never
deletes your notebooks or settings.

## Windows and macOS

The same pip route works on both:
install Python from python.org (or,
on macOS, with Homebrew), make the
environment, install the same package
names. The differences are the usual
ones — path separators, and on
Windows, running the commands from
PowerShell or the terminal app of
your choice. Nothing in this guide's
later chapters depends on the
operating system, because everything
interesting happens between a browser,
a server, and a kernel.
