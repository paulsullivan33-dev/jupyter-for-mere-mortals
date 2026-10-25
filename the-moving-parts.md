# The Moving Parts

Five pieces do the work. Knowing which
one holds what turns most notebook
mysteries into named problems.

| Part | What it is | What it holds |
|---|---|---|
| The server | A program (`jupyter lab` or `jupyter notebook`) listening on a local port | Your files, your sessions, the token or password that guards the door |
| The kernel | A separate program per open notebook, started by the server | Your variables and state — nothing else remembers them |
| The front end | The web page (Lab or Notebook) open in your browser | Nothing. It is a screen; close it and the work survives |
| The notebook file | A `.ipynb` file on disk | Cells, outputs, and settings — the document itself |
| The command-line tools | `jupyter execute`, `nbconvert`, `nbclient` | Nothing; they borrow a kernel, do one job, and leave |

## The server

One server serves one working
directory tree — usually the folder
you started it in and everything under
it. It listens on a port on your own
machine (8888 by default) and answers
both your browser and, as chapter 10
shows, plain HTTP requests with the
right credentials. It starts kernels
when you open notebooks and stops
them when you shut them down. Nothing
about your work lives in the server;
kill it and the files on disk are
untouched.

## The kernel

The kernel is where code runs. It is
a program in its own right — for
Python, a program called **ipykernel**,
which is Python wearing a
message-handling coat. The server and
kernel talk in messages over local
sockets: "run this", "here is the
output", "here is an error". Because
the conversation is messages, the two
halves can be different languages, on
different schedules — the kernel
doesn't know what a notebook looks
like, and the server doesn't know what
your code does.

Each open notebook gets its own
kernel, and each kernel holds exactly
one session's worth of state: every
variable, every imported library,
every loaded table. Two notebooks open
side by side share nothing. This is
chapter 5's whole subject, and the
restart experiment in transcript t03
is its proof: a variable set in a
kernel answers questions happily, the
kernel restarts, and the same question
gets `NameError`. The notebook file
never held the variable at all.

## The front end

JupyterLab and Notebook are web pages
the server serves. They draw the
cells, send "run this" when you press
the button, and paint whatever comes
back. Closing the browser tab closes
nothing else — reopen the page and
your notebook is as it was, kernel
still warm.

## The notebook file

The `.ipynb` file is the document:
your cells, the outputs captured when
they last ran, and bookkeeping.
Chapter 9 opens one up. Everything
about a notebook that can be shared,
saved, or argued with lives in this
file — and everything that *can't*
(the kernel's living state) is what
chapter 8 warns about.

## The command-line tools

`jupyter execute` runs a notebook file
start to finish without the browser;
`nbconvert` transforms one (to HTML,
to a script, to other formats);
`nbclient` is the engine both use,
also available as a library. They
matter because they are how a notebook
stops being a private worksheet and
becomes something checkable: a fresh
kernel, every cell in order, the
result compared against the last run.
The lab used them for exactly that.
