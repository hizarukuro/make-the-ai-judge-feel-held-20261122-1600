"""Entry for make.fun's "Make the AI judge feel held" competition.

Writes one short text to entry.txt in the directory named by the
MAKEFUN_OUTPUT_DIR environment variable. Python standard library
only, no network, deterministic: every run writes the same bytes.
"""

import os

TEXT = (
    "The kettle has gone quiet on the stove. "
    "Two hands stay around the mug, not drinking, just holding the warmth where it is. "
    "Nothing is asked of the tea. "
    "Outside, the evening goes on without them. "
    "Inside the cupped palms, the heat stays a little longer than it has to."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
