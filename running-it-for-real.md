# Running It for Real

Chapter 4's server — a token in a
printed address, on your own machine,
for an afternoon — is the right
default. This chapter is for when the
server becomes furniture: started
often, reached from another machine,
left running. Every step here was
checked in the lab at the level the
sandbox allows; where a step needs a
second machine, it says so, and the
safety reasoning does not depend on
the sandbox anyway.

## What the token is doing

The server the lab started was
interrogated over HTTP (transcript
t06), and the results describe the
security shape exactly:

- `GET /api` — the version ping —
  answers **anyone**, with nothing:
  `{"version": "2.21.1"}`. Harmless,
  and a reminder that the server
  announces itself.
- `GET /api/contents` — the file
  list, the door that matters —
  answers **403** with no token, and
  403 with a wrong one.
- With the token, in a header or in
  the address, everything answers:
  the file list shows your files,
  and `/lab` loads.

Understand what the token guards: a
Jupyter server is, by design, a
machine for running arbitrary code
as its user. The token is not
protecting your notebooks. It is
protecting your *account*. Treat the
printed token URL like a password —
because it is one — and never paste
it into shared places.

## A password instead

For a server you keep, swap the
rotating token for a password you
choose. Jupyter stores only a hash;
making one is a lab-verified
one-liner (transcript t07):

```bash
~/jupyter-venv/bin/python -c \
  "from jupyter_server.auth import passwd; print(passwd())"
```

It asks for the password and prints
an `argon2:…` hash — a one-way
scramble; the server checks guesses
against it and the password itself
is never written down. Put the hash
in the config file (below) as
`c.ServerApp.password`, and logins
become a password prompt instead of
a token hunt.

## The config file

```bash
~/jupyter-venv/bin/jupyter lab --generate-config
```

writes `~/.jupyter/jupyter_lab_config.py`
— in the lab, 41 KB holding **226
commented-out settings**, each with
its explanation (transcript t07).
The pattern is: find the line, remove
the `#`, set the value. The handful
that matter:

```python
c.ServerApp.password = 'argon2:…'   # the hash, never the password
c.ServerApp.ip = 'localhost'        # who can reach it — see below
c.ServerApp.port = 8888
c.ServerApp.open_browser = False    # servers don't open browsers
```

## Reaching it from another machine

The cautious way, and the one this
guide recommends: don't expose the
server at all. Leave `ip` at
localhost, and let SSH carry you —
an **SSH tunnel** forwards a port on
your laptop to the server:

```bash
ssh -L 8888:localhost:8888 your-server
```

then browse to `localhost:8888` as
if the server were local. The
password or token still applies; SSH
adds encryption and its own login in
front. (The lab had one machine, so
the tunnel itself is described, not
demonstrated.)

The bolder way — `c.ServerApp.ip =
'0.0.0.0'` so the server listens on
the network — makes the token or
password the *only* lock on a
code-running service. On a trusted
home network, with a real password,
that is a defensible choice people
make every day. On the public
internet it is not: use the tunnel,
or a proper reverse proxy with HTTPS
in front, which is beyond this
guide's scope and deliberately so.

## Running it for a household

One server is one user's server —
files, kernels, and all. The moment
several people need notebooks at
once, each with their own login and
their own space, the tool changes
name: **JupyterHub** spawns a
separate server per user and manages
the logins centrally. It is the
standard answer for classes and
teams, it is documented-only in this
guide, and everything you have
learned about notebooks, kernels,
and files carries over unchanged —
Hub is a landlord, not a different
kind of house.
