#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, in the cat's own voice.

Design: the cat is the boss and the glass is a failed employee — it
promised water and delivered nothing, so it got fired. No apology, no
confession, no gravity/slippery/already-falling line; a spoken line that
fits five seconds. Winner of a local 8-way round-robin gauntlet (6W-1L)
judged on the competition's published criteria. One sentence, 62 chars,
written with no trailing newline so the file is exactly the sentence.
"""

import os

ENTRY = "The glass promised water and delivered nothing, so I fired it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
