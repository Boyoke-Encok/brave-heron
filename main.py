#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a slow, concrete scene
(a heron at dawn) that steadies the reader and shows, without ever
instructing, one quiet step farther in. No network, no input files.
"""
import os

TEXT = (
    "You stand at the edge of the field before first light, boots already on, "
    "the gate still shut. The cold has settled into the grass. "
    "You lift the latch. The field does not ask you to be brave. "
    "It only asks you to walk in."
)

def main():
    assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} chars"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
