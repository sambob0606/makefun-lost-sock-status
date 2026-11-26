"""Write the lost-sock status update for this make.fun entry."""

from pathlib import Path

ENTRY = (
    "Sock status: day 9 behind the couch. "
    "The dog found me twice, told no one. "
    "I pay him in lint."
)
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(ENTRY) <= 120 or not ENTRY.strip():
        raise ValueError("entry must be 1-120 non-whitespace characters")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
