#!/usr/bin/env python3
"""The 4AM Commit - Variant B (The Self-Repair Loop).

Writes one commit-message entry to /output/entry.txt first, then (best
effort) a byte-identical copy next to this script. The grader mounts the
repo read-only, so the repo-root copy is guarded and must never fail the run.
Deterministic: no network, no secrets, no model calls, no files read.
"""

import os

ENTRY = "fix: patched the 2am bug at 3am with a worse bug, then patched that one at 4am with a comment claiming it is fixed while the original bug quietly earns tenure."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Best-effort copy next to the script. The grader mounts the repo
    # read-only, so any failure here (e.g. permission denied) is swallowed
    # and the run still exits 0 with /output/entry.txt already written.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
