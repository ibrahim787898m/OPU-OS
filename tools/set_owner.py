#!/usr/bin/env python3
"""Set (or change) the OPU/OS owner passphrase.

Run it from the repo root in your own terminal:

    python3 tools/set_owner.py

It asks for the passphrase twice (nothing is shown while you type), then writes a
salted PBKDF2-SHA256 hash into index.html. Only the hash goes into the file, never the
passphrase. Commit and push afterwards. The browser checks your passphrase against this
hash with the same settings.
"""
import getpass, hashlib, os, re, sys

ITERATIONS = 600_000          # must match OWNER.iter in index.html
MIN_LEN = 10                  # the hash is public, so a long passphrase matters

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index.html")
html = open(path, encoding="utf-8").read()
pattern = re.compile(r"const OWNER=\{salt:'[^']*',iter:\d+,hash:'[^']*'\};")
if not pattern.search(html):
    sys.exit("Couldn't find the OWNER line in index.html. Nothing changed.")

pw = getpass.getpass("New owner passphrase: ")
if len(pw) < MIN_LEN:
    sys.exit(f"Too short: use at least {MIN_LEN} characters (a few random words works well). Nothing changed.")
if getpass.getpass("Type it again: ") != pw:
    sys.exit("The two entries don't match. Nothing changed.")

salt = os.urandom(16)
digest = hashlib.pbkdf2_hmac("sha256", pw.encode("utf-8"), salt, ITERATIONS).hex()
line = f"const OWNER={{salt:'{salt.hex()}',iter:{ITERATIONS},hash:'{digest}'}};"
open(path, "w", encoding="utf-8").write(pattern.sub(line, html, count=1))
print("Done. index.html now holds the hash of your new passphrase.")
print("Next: open index.html to check you can unlock, then commit and push.")
