import sys
import os
import json
from datetime import datetime, timezone


def summarize(text: str, max_words: int = 40) -> tuple[int, str]:
    """Return token count and simple summary from text.

    Tokens are approximated using whitespace word count.
    The summary is the first `max_words` words of the file.
    """
    words = text.strip().split()
    token_count = len(words)
    summary = " ".join(words[:max_words])
    return token_count, summary


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python summary.py <file>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    tokens, summary = summarize(content)

    result = {
        "file": os.path.basename(path),
        "tokens": tokens,
        "summary": summary,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
