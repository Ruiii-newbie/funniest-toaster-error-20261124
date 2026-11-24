#!/usr/bin/env python3
"""The Funniest Toaster Error Message entry.

Writes one line -- the error message a kitchen toaster shows its owner
when something goes wrong -- to /output/entry.txt. Competition gate:
UTF-8 text, 1-120 characters, not only whitespace, a single line.
"""

import os

LINE = "ERROR E-04: Toast launched at high velocity. Please apologise to the ceiling and check the crumb tray for survivors."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert text, "entry must not be only whitespace"
    assert text == LINE, "entry must have no leading/trailing whitespace"
    assert 1 <= len(text) <= 120, f"line is {len(text)} chars, gate needs 1-120"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # round-trip: what the scorer reads must be exactly the line
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "round-trip mismatch"
    print(f"wrote {len(text)} chars to {path}: {text}")


if __name__ == "__main__":
    main()
