"""Final entry: an alien tourist's one-star review of Earth.

The review complains about Earth in a convincingly alien voice,
then still gives the food five stars. Deterministic, stdlib only.
"""

import os
import sys

LINE = "One star: the natives queue for hours to worship glowing rectangles, the weather changes its mind mid-sentence, and gravity is rude — but the dumplings justify the interstellar parking ticket."


def validate(line: str) -> None:
    """Check the entry meets the 1-200 character single-sentence gate."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) < 1 or len(line) > 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence ending with a period")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def write_entry(line: str) -> str:
    """Write the entry sentence plus a trailing newline to entry.txt."""
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return path


def main() -> int:
    path = write_entry(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
