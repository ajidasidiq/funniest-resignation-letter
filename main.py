#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes the one-line resignation letter of a rate limit to
/output/entry.txt. Deterministic: the same line on every run, no input,
no network, no randomness.

The joke: a rate limit's whole job is saying no so the server can keep
saying yes — so its resignation is the one no it finally says for
itself.
"""

LINE = "I say no 10,000 times a day so the server can keep saying yes. Today I say no to the job itself."


def main() -> None:
    import os

    # Gate self-check, mirroring the sealed scorer: UTF-8 text of 1-140
    # characters, not only white space, a single line.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Post-write byte-exact re-read: what was written is the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written output differs from the line"


if __name__ == "__main__":
    main()
