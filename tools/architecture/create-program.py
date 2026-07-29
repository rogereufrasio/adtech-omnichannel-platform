#!/usr/bin/env python3

"""
Enterprise Architecture Program Scaffold Generator

Usage:

python tools/architecture/create-program.py \
    --number 03 \
    --name enterprise-integration-platform
"""

from __future__ import annotations

import argparse
from pathlib import Path
from validate_blueprint import validate


ROOT_FILES = [
    "README.md",
    "architecture-target-state.md",
    "executive-target-state.md",
    "maturity-assessment.md",
]

DIRECTORIES = {
    "adrs": [
        "README.md",
    ],
    "business-architecture": [],
    "application-architecture": [],
    "information-architecture": [],
    "integration-architecture": [],
    "technology-architecture": [],
    "governance": [],
    "diagrams": [],
    "roadmap": [],
    "docs": [],
}


def create_file(path: Path, content: str = "") -> None:
    """Create a file if it does not already exist."""
    if path.exists():
        return

    path.write_text(content, encoding="utf-8")


def create_directory(path: Path) -> None:
    """Create a directory recursively."""
    path.mkdir(parents=True, exist_ok=True)


def build_program_path(number: int, name: str) -> Path:
    directory = f"{number:02d}-{name}"
    return Path("programs") / directory


def generate_readme(program_name: str, number: int) -> str:
    title = program_name.replace("-", " ").title()

    return f"""# Program {number:02d} — {title}

## Overview

Describe the purpose of this Enterprise Architecture Program.

## Objectives

- Define the architectural vision.
- Document the target state.
- Guide implementation.
- Support architecture governance.

## Documentation

- architecture-target-state.md
- executive-target-state.md
- maturity-assessment.md

## Architecture Domains

- Business Architecture
- Application Architecture
- Information Architecture
- Technology Architecture
- Governance
- Roadmap
"""


def generate_adr_readme() -> str:
    return """# Architecture Decision Records

This directory stores all Architecture Decision Records (ADRs)
for this Enterprise Architecture Program.

Follow the template defined in:

standards/program-blueprint/adr-template.md
"""

def preview_program(program_path: Path, number: int, name: str) -> None:
    print()
    print("Enterprise Architecture Program Preview")
    print("=" * 60)
    print()

    print(f"Program: {number:02d}-{name}")
    print()

    print("Files that would be created:")
    print()

    for filename in ROOT_FILES:
        print(
            f"  {program_path / filename}"
        )

    for directory, files in DIRECTORIES.items():
        print()

        if files:
            for filename in files:
                print(
                    f"  {program_path / directory / filename}"
                )
        else:
            print(
                f"  {program_path / directory}/"
            )

    print()

def scaffold(program_path: Path, number: int, name: str) -> None:
    create_directory(program_path)

    for filename in ROOT_FILES:
        file_path = program_path / filename

        if filename == "README.md":
            create_file(file_path, generate_readme(name, number))
        else:
            create_file(file_path)

    for directory, files in DIRECTORIES.items():
        folder = program_path / directory
        create_directory(folder)

        for filename in files:
            target = folder / filename

            if directory == "adrs" and filename == "README.md":
                create_file(target, generate_adr_readme())
            else:
                create_file(target)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Enterprise Architecture Program Scaffold Generator"
    )

    parser.add_argument(
        "--number",
        required=True,
        type=int,
        help="Program number",
    )

    parser.add_argument(
        "--name",
        required=True,
        help="Program name (kebab-case)",
    )

    parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Preview generated program structure without creating files",
    )

    return parser.parse_args()


def main():

    if not validate():
        print(
            "Program generation cancelled because "
            "blueprint validation failed."
        )

        return 1

    args = parse_args()

    program_path = build_program_path(
        args.number,
        args.name,
    )

    if args.dry_run:
        preview_program(
            program_path,
            args.number,
            args.name,
        )

        return 0

    exists_before = program_path.exists()

    scaffold(
        program_path=program_path,
        number=args.number,
        name=args.name,
    )

    print()

    if exists_before:
        print("Enterprise Architecture Program scaffold updated successfully.")
    else:
        print("Enterprise Architecture Program created successfully.")

    print(f"Location: {program_path}")
    print()

    scaffold(
        program_path=program_path,
        number=args.number,
        name=args.name,
    )

if __name__ == "__main__":
    raise SystemExit(main())