"""Two-Sentence Horror entry for make.fun.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic: no randomness, no network, no input, no files read.
The second sentence reframes the first: the drawings stop, and
something that could only have come from outside is already inside.
"""

from pathlib import Path

STORY = (
    "Every night my daughter tapes a new drawing to the fridge: "
    "the same tall man, standing at the end of our driveway, "
    "a little closer each time. "
    "This morning there was no drawing, only a single muddy footprint "
    "on the kitchen floor, and her crayons were still sealed in the box."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
