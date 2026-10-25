# Writing Criteria

Every guide in this repo is written to the same
standard. If you're adding or editing a guide —
human or AI — hold it to these.

1. **Plain words, real ideas.** Simple language,
   never dumbed-down concepts. Explain jargon on
   first use; collect terms in the glossary.
2. **No hype.** No marketing adjectives, no
   "revolutionary," no promises about what
   something will do for the reader.
3. **Honest about limits.** Say what the thing
   *can't* do. State uncertainty instead of
   smoothing it over. Validation notes include
   what remains unverified.
4. **No invented numbers.** Benchmarks, defaults,
   and specs are either measured or qualified with
   "depends on your setup." If it wasn't tested,
   say so.
5. **Checkable.** Commands are meant to be run,
   with "Check:" blocks showing what success looks
   like. Sources are linked, not asserted.
6. **Respect the reader's setup.** Call out
   Windows/Mac/Linux differences. Don't assume a
   GPU, a budget, or prior experience.
7. **Safety isn't skipped.** Real risks get
   stated plainly, not buried.
8. **Scoped.** Each guide says what it covers and
   points elsewhere for the rest. No guide
   pretends to be the whole subject.
9. **Structure over prose.** Tables, before/after
   examples, symptom → fix. Scannable beats essay.

## Verification notes for this guide

Built and verified 2026-10-24/25 against
**JupyterLab 4.6.4** and **Notebook
7.6.3** (jupyter_server 2.21.1,
ipykernel 7.4.0, nbconvert 7.17.2,
nbclient 0.11.0, nbformat 5.11.1),
installed with pip into a fresh
virtual environment (Python 3.12.3)
on a 2-CPU, 7.7 GB sandbox machine
running Ubuntu 24.04, with pandas,
matplotlib and bash_kernel installed
the same way.

**Primary sources read, not
remembered:** the installed tools'
own `--help` and `--version`
output; the config file
`jupyter lab --generate-config`
writes (226 commented settings,
quoted in chapter 12); the notebook
files themselves, parsed as JSON;
and the Jupyter Server HTTP API as
the running server answered it.

**The sandbox, declared.** The lab
machine has no display, so the
JupyterLab and Notebook web
interfaces were never opened in a
browser. Nothing in the chapters
depends on pretending otherwise:
the interfaces are the server's
front doors, and every behavioural
claim — execution, outputs, kernels,
restart semantics, exports, token
enforcement — was proven at the
command line and over HTTP against
the real install, which drives the
same server and the same kernel
machinery the browser does.
Interface descriptions (launcher,
menus, buttons) follow the
projects' documentation and are the
guide's documented-only surface,
named as such in the README. The
sandbox user is root, which produced
one refusal a normal reader will
never see (t90, below).

**Ran for real** (transcripts in
`jupyter-lab/transcripts/`):

- t00 — versions of every component;
  `jupyter kernelspec list` before
  (python3 only) and after
  registering the bash kernel with
  `python -m bash_kernel.install
  --sys-prefix` (python3, bash).
- t01 — the lab notebook (8 cells,
  written by `jupyter-lab/
  make_notebook.py` with nbformat)
  executed end to end with
  `jupyter execute --inplace`: file
  grew 3,020 → 96,730 bytes,
  execution counts [1, 2, 3, 4], one
  HTML display output, one PNG plot
  output (present twice — see
  chapter 7), and all five printed
  headline numbers matched an
  independent recount from the CSV
  by a separate checker script.
- t02 — outputs cleared with
  nbconvert's ClearOutputPreprocessor
  (96,730 → 4,282 bytes, counts back
  to none); the cleared copy
  re-executed from a cold kernel and
  its stream output compared with
  the first run's: identical.
- t03 — a kernel driven directly
  through jupyter_client: a variable
  set, used (answer 42), the kernel
  restarted, the same name raising
  NameError. The state lived in the
  kernel, not the file.
- t04 — a two-cell notebook under
  the **bash** kernelspec executed
  the same way: a shell variable set
  in cell 1 spent in cell 2 against
  the real CSV.
- t05 — `nbconvert --to html`
  (379,927 bytes; the numbers and
  the plot present, the plot as
  base64 data inside the page) and
  `--to script`; the exported
  script run as an ordinary program
  and its stdout diffed against the
  notebook's recorded stream text:
  identical.
- t06 — `jupyter lab` started
  headless; over HTTP, `/api`
  answered `{"version": "2.21.1"}`
  with no credentials, `/api/
  contents` answered 403 with no
  token and 403 with a wrong one,
  and with the real token the
  contents listing showed the lab's
  files and `/lab` returned 200.
- t07 — `--generate-config` wrote
  the real config file (41 KB, 226
  commented settings); a password
  hash was produced by
  `jupyter_server.auth.passwd()`
  (argon2id), as chapter 12 shows.

**Kept as found (t90):**
`jupyter execute` *without*
`--inplace` or `--output` executed
the whole notebook and silently
discarded the result (nbclient
0.11.0's default), the trap
chapter 10 is built around; and
the server's refusal to start as
root without `--allow-root`,
which is the sandbox's property
(the lab user is root), not a
reader's — chapter 16 labels it as
such. One scaffolding bug of the
lab's own (a restart demo script
tripping on kernel restart
messages) was fixed before its
transcript was taken and is not
presented as Jupyter behaviour.

**Documented only, and labelled as
such in the chapters:** clicking
through the JupyterLab and Notebook
interfaces (no display — see the
sandbox note); PDF export (no
LaTeX or browser print engine was
installed); the SSH tunnel of
chapter 12 and any two-machine
setup (one machine); JupyterHub
end to end; papermill's
parameterised runs (not installed;
the recipe in chapter 13 rests on
chapter 10's proven execution);
kernels other than Python and bash;
slides export; ipywidgets.

**Fixtures:** both datasets are
invented for this guide — thirty
days of weather readings for a
fictional town, and a bookshop's
week of sales with invented titles.
Nothing is modelled on any real
person, organisation, weather
record or event, and any reader
can regenerate the lab notebook
from `jupyter-lab/make_notebook.py`
and check every number the
chapters quote.
