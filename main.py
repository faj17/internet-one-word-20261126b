#!/usr/bin/env python3
"""Write the one-word entry for 'The Internet in One Word' (make.fun).

The entry is a single English word describing the whole internet.
The word is assembled from fragments so the entrypoint shows its
construction, then validated against the competition gate (UTF-8 text,
1-30 characters, not only white space) before it is written.
"""

# Fragments of the winning word, chosen against the judge's five
# criteria: single word, funny by itself, true of the whole internet,
# surprising, lands in one beat.
_FRAGMENTS = ("un", "hing", "ed")

# Rejected drafts, kept beside the winner with the reason each lost.
_REJECTED = {
    "chaos": "the first obvious word anyone reaches for",
    "memes": "one corner of the internet, not the whole of it",
    "cats": "one site/mood, not the whole internet",
    "doomscrolling": "phrase-like compound, too long to land in one beat",
    "procrastination": "true but not funny by itself",
    "feral": "strong runner-up, less funny than the winner",
    "unsupervised": "funny and true, but lands slower at 12 letters",
}

MAX_CHARS = 30


def assemble(fragments=_FRAGMENTS):
    """Join the fragments into the entry word."""
    return "".join(fragments)


def validate(word):
    """Check the entry against the competition gate."""
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word) > MAX_CHARS:
        raise ValueError(f"entry must be at most {MAX_CHARS} characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word")
    word.encode("utf-8")
    return word


def main():
    import os

    word = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
