from __future__ import annotations

from pathlib import Path


def ensure_directory(path: Path) -> None:
    """Create a directory recursively if necessary."""
    path.mkdir(parents=True, exist_ok=True)


def ensure_file(path: Path, content: str = "") -> None:
    """Create a file if it does not already exist."""
    if path.exists():
        return

    path.write_text(content, encoding="utf-8")