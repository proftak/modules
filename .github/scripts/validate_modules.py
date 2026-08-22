#!/usr/bin/env python3
"""Structural checks for the module library and the sequence files.

Catches the kinds of drift that are invisible until a reader hits them:
a link to a module that does not exist, a prerequisite pointing at nothing,
a sequence naming a module by a title the module no longer has.

Run:  python3 .github/scripts/validate_modules.py
Exits non-zero and prints one line per problem.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
MODULE_SRC = sorted(list(ROOT.glob("[0-9][0-9][0-9][0-9]/mdModule.md"))
                    + list(ROOT.glob("[0-9][0-9][0-9][0-9]/index.md")))
SEQUENCES = sorted(ROOT.glob("sequences/*.md"))

# ../NNNN/name.html  ->  NNNN/name.md
REL = re.compile(r"\.\./(\d{4})/([A-Za-z0-9_-]+)\.html")
LINK = re.compile(r"\[([^\]]+)\]\(\.\./(\d{4})/([A-Za-z0-9_-]+)\.html\)")
TITLE = re.compile(r'^title:\s*"(.*)"\s*$', re.M)

problems = []


def note(path, msg):
    problems.append(f"{path.relative_to(ROOT)}: {msg}")


def title_of(mod_dir):
    for stem in ("mdModule", "index"):
        p = ROOT / mod_dir / f"{stem}.md"
        if p.exists():
            m = TITLE.search(p.read_text(encoding="utf-8"))
            if m:
                return m.group(1).replace('\\"', '"')
    return None


def target_exists(num, stem):
    return (ROOT / num / f"{stem}.md").exists()


# 1. every relative module link resolves
for path in MODULE_SRC + SEQUENCES:
    for num, stem in REL.findall(path.read_text(encoding="utf-8")):
        if not target_exists(num, stem):
            note(path, f"link to ../{num}/{stem}.html but {num}/{stem}.md does not exist")

# 2. every Prerequisites entry resolves and names a real module
for path in MODULE_SRC:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if not re.match(r"\s*-\s+Prerequisites:", line):
            continue
        for num in re.findall(r"\b(\d{4})\b", line):
            if not (ROOT / num).is_dir():
                note(path, f"prerequisite {num} does not exist")
        # a bare number with no link is easy to write by accident
        bare = set(re.findall(r"(?<![/\[])\b\d{4}\b(?!\])", re.sub(r"\[[^\]]*\]\([^)]*\)", "", line)))
        for num in sorted(bare):
            note(path, f"prerequisite {num} is not a link")

# 3. sequences: targets must exist, carry an About block, and be named correctly
for path in SEQUENCES:
    for text_label, num, stem in LINK.findall(path.read_text(encoding="utf-8")):
        src = ROOT / num / f"{stem}.md"
        if not src.exists():
            continue  # already reported by check 1
        body = src.read_text(encoding="utf-8")
        if "# About this module" not in body:
            note(path, f"{num} is sequenced but has no '# About this module' block")
        actual = title_of(num)
        if actual is None:
            note(path, f"{num} has no title in its front matter")
            continue
        expected = re.sub(r"^Module\s+", "", actual)
        if text_label.strip() != expected.strip():
            note(path, f"{num} link text is {text_label!r} but the module title is {expected!r}")

if problems:
    print(f"{len(problems)} problem(s) found:\n")
    for p in problems:
        print("  " + p)
    sys.exit(1)

print(f"OK - {len(MODULE_SRC)} modules, {len(SEQUENCES)} sequence file(s), no problems.")
