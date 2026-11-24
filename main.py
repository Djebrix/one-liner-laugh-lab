"""One-liner laugh lab entry: the robot vacuum's excuse.

Writes the entry line to <ENTRY_OUTPUT_DIR>/entry.txt.
Python 3 standard library only; deterministic.
"""

import os

TEXT = "It matched the rug. I refuse to apologize to camouflage."


def main():
    line = TEXT.strip()
    assert 1 <= len(line) <= 200, f"line length {len(line)} out of range 1-200"
    assert line.strip(), "line must not be blank"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {out_path} ({len(line)} characters)")


if __name__ == "__main__":
    main()
