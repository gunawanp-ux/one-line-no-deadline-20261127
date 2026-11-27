"""One Line, No Deadline Met — a single-line joke excusing a missed deadline.

Writes one original one-line excuse to /output/entry.txt (created if
it does not exist). The entry is a single sentence, 95 characters,
within the competition gate of 1-200 characters.
"""

import os

ENTRY = "I finished the work on time \u2014 in a dream \u2014 and unfortunately dreams don't have a submit button."


def main() -> None:
    # Competition gate: the entry must be 1-200 characters, one line,
    # and not only white space.
    assert 1 <= len(ENTRY) <= 200, (
        f"entry is {len(ENTRY)} chars, must be 1-200"
    )
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
