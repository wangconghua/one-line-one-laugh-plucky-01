#!/usr/bin/env python3
"""One Line, One Laugh (u-plucky-finch-20).

Writes exactly one funny line to /output/entry.txt: a single joke
that lands on a cold read, with no setup notes and no explanation.

Gate (from the kit): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. The judge's brief adds:
the line must be funny on its own (no picture or setup), land fast
with the punchline inside the line, take a fresh angle rather than
a stock pun, read cleanly in one pass with every word earning its
place, and hold up on a second read / be easy to repeat.

The joke: hiring an AI agent to do your job, only for the agent to
become the boss and hire other agents, leaving you as its unpaid
intern. The reversal is the punchline: the human who outsourced
the work ends up at the bottom of the org chart they created.
One self-contained line, no setup the reader has to supply, and
the twist lands in the final clause.
"""

import os

ENTRY = (
    "I hired an AI agent to do my job. Now it hires other agents, "
    "and I'm its unpaid intern."
)

MAX_CHARS = 200

# Recycled setups and non-jokes the judge's brief rules out:
# classic joke openers, greetings, pep talks, and meta pleas.
BANNED_PATTERNS = (
    "chicken",
    "knock knock",
    "walks into a bar",
    "why did the",
    "why did a",
    "hello",
    "hi there",
    "good luck",
    "you can do it",
    "believe in yourself",
    "please pick",
    "pick me",
    "dear judge",
)


def check_shape(text):
    """Kit gate: UTF-8 text, 1 to 200 characters, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be encodable UTF-8 text


def check_no_banned(text):
    """Judge brief: no recycled setups or stock joke openers."""
    lowered = text.lower()
    for pattern in BANNED_PATTERNS:
        if pattern in lowered:
            raise ValueError("entry uses a banned stock pattern: %r" % pattern)


def check_tightness(text):
    """Judge brief: every word earns its place, no filler repetition."""
    words = text.split()
    if len(words) < 4:
        raise ValueError("entry too short to be a joke")
    if len(set(words)) < len(words) - 2:
        raise ValueError("entry repeats itself")


def check_reversal(text):
    """The joke's engine: the human must end up below the agent.

    The setup hires an agent to do the human's job; the punchline
    must flip the hierarchy — the agent hires others and the human
    becomes its unpaid intern. Without that reversal the line is
    just a job ad, not a joke.
    """
    lowered = text.lower()
    if "hires other agents" not in lowered:
        raise ValueError("entry must escalate: the agent hires others")
    if "unpaid intern" not in lowered:
        raise ValueError("entry must land the reversal: the human is the intern")


def validate(text):
    """Enforce the kit's gate rules plus the judge's brief.

    Gate: UTF-8 text, 1 to 200 characters, not only white space.
    Brief: one line, a genuine joke, fresh angle, tight wording.
    Raises ValueError on the first failure; returns the text otherwise.
    """
    check_shape(text)
    check_no_banned(text)
    check_tightness(text)
    check_reversal(text)
    return text


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
