#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a slow, concrete scene
(a heron at dawn) that steadies the reader and shows, without ever
instructing, one quiet step farther in. No network, no input files.
"""
import os

TEXT = (
    "At the edge of the silt, a heron stands on one grey leg while the river "
    "does its slow work under the reeds. The bird waits until the water clears, "
    "then lifts its foot and sets it down again, a little farther in. "
    "The river keeps going. So does the heron."
)

def main():
    assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} chars"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
