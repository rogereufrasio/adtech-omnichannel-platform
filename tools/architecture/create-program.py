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


def create_file(
    path: Path,
    content: str = "",
    mode: str = "default",
) -> str:
    """
    Create or update a file according to generation mode.

    Modes:
    - default: create only if missing
    - update: create only missing files
    - force: overwrite existing files
    """

    if path.exists():
        if mode == "force":
            path.write_text(
                content,
                encoding="utf-8",
            )
            return "updated"

        return "skipped"

    path.write_text(
        content,
        encoding="utf-8",
    )

    return "created"


def create_directory(path: Path) -> None:
    """Create a directory recursively."""
    path.mkdir(parents=True, exist_ok=True)


def render_template(
    template_path: Path,
    **variables,
) -> str:
    """
    Render blueprint template replacing variables.
    """

    content = template_path.read_text(encoding="utf-8")

    for key, value in variables.items():
        content = content.replace(
            f"{{{{{key}}}}}",
            str(value),
        )

    return content


def build_program_path(number: int, name: str) -> Path:
    directory = f"{number:02d}-{name}"
    return Path("programs") / directory


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
        print(f"  {program_path / filename}")

    for directory, files in DIRECTORIES.items():
        print()

        if files:
            for filename in files:
                print(f"  {program_path / directory / filename}")
        else:
            print(f"  {program_path / directory}/")

    print()


def scaffold(
    program_path: Path,
    number: int,
    name: str,
    mode: str = "default",
) -> dict:
    create_directory(program_path)

    created_files = []

    # 1. Process Root Files
    for filename in ROOT_FILES:
        template = (
            Path("standards")
            / "program-blueprint"
            / "templates"
            / f"{filename}.template"
        )

        file_path = program_path / filename

        content = render_template(
            template,
            PROGRAM_NUMBER=f"{number:02d}",
            PROGRAM_TITLE=name.replace("-", " ").title(),
        )

        create_file(
            file_path,
            content,
            mode=mode,
        )

        created_files.append(str(file_path))

    # 2. Process Directories and Sub-templates
    for directory, files in DIRECTORIES.items():
        folder = program_path / directory
        create_directory(folder)

        for filename in files:
            target = folder / filename

            template_path = (
                Path("standards")
                / "program-blueprint"
                / "templates"
                / directory
                / f"{filename}.template"
            )

            content = render_template(
                template_path,
                PROGRAM_NUMBER=f"{number:02d}",
                PROGRAM_TITLE=name.replace("-", " ").title(),
            )

            create_file(
                target,
                content,
                mode=mode,
            )

            created_files.append(str(target))

    return {
        "program": str(program_path),
        "files": created_files,
    }


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
        help="Nome do programa (minúsculas separadas por hífens)",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview generated program structure without creating files",
    )

    parser.add_argument(
        "--update",
        action="store_true",
        help="Create only missing files and preserve existing files",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files",
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

    mode = "default"
    if args.force:
        mode = "force"
    elif args.update:
        mode = "update"

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
        mode=mode,
    )

    print()

    if exists_before:
        print("Enterprise Architecture Program scaffold updated successfully.")
    else:
        print("Enterprise Architecture Program created successfully.")

    print(f"Location: {program_path}")
    print()


if __name__ == "__main__":
    raise SystemExit(main())
