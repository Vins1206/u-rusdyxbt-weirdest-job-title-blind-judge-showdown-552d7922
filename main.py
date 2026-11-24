"""Weirdest Job Title entry.

Writes a single job title, 60 characters or fewer and nothing else,
to /output/entry.txt. Pure standard library, deterministic.
"""

import os

TITLE = "Full-Time Apologizer to Angry Geese"


def main() -> None:
    # The gate is 1-60 characters, not only whitespace: enforce it here
    # so a bad title can never reach /output/entry.txt.
    assert 1 <= len(TITLE) <= 60, "title must be 1-60 characters"
    assert TITLE.strip(), "title must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
