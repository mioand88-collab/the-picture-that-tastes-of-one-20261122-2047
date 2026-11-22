"""Tonkotsu Ramen — the picture that tastes of one ingredient.

Writes the entry image to /output/entry.png.

The picture itself (a steaming bowl of tonkotsu ramen: glossy broth, wavy
noodles, jammy soft egg, chashu, spring onions, nori and chopsticks on a
warm wooden table) was rendered in the builder session and ships beside
this program as entry.png. This program simply copies it to the output
path, so the run is deterministic and needs no network.

Standard library only. Never removes /output itself: in the grader it is
a mount point, so only its contents are ever touched.
"""

import hashlib
import os
import shutil
import sys


def _sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    if os.path.abspath(source) == os.path.abspath(target):
        return 0
    shutil.copyfile(source, target)
    # Self-check: the written file must be byte-identical to the source.
    if _sha256(source) != _sha256(target):
        print("error: output differs from entry.png", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
