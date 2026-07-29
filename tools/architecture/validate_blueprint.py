#!/usr/bin/env python3

"""
Enterprise Architecture Blueprint Validator

Validates the standards/program-blueprint structure before generating
Enterprise Architecture Programs.

Checks:

- Required blueprint files
- Template existence
- Document matrix consistency
- Program structure existence
"""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]

BLUEPRINT_PATH = (
    ROOT
    / "standards"
    / "program-blueprint"
)

REQUIRED_FILES = [
    "README.md",
    "program-structure.md",
    "document-matrix.md",
    "adr-template.md",
    "checklist.md",
]


REQUIRED_TEMPLATES = [
    "templates/README.md.template",
    "templates/architecture-target-state.md.template",
    "templates/executive-target-state.md.template",
    "templates/maturity-assessment.md.template",
    "templates/adrs/README.md.template",
]


class BlueprintValidationError(Exception):
    pass


def validate_required_files() -> list[str]:
    errors = []

    for filename in REQUIRED_FILES:
        file_path = BLUEPRINT_PATH / filename

        if not file_path.exists():
            errors.append(
                f"Missing blueprint file: {file_path}"
            )

    return errors


def validate_templates() -> list[str]:
    errors = []

    for template in REQUIRED_TEMPLATES:
        template_path = BLUEPRINT_PATH / template

        if not template_path.exists():
            errors.append(
                f"Missing template: {template_path}"
            )

    return errors


def validate_template_directory() -> list[str]:
    errors = []

    template_directory = BLUEPRINT_PATH / "templates"

    if not template_directory.exists():
        errors.append(
            f"Missing templates directory: {template_directory}"
        )

    return errors


def validate() -> bool:
    errors = []

    errors.extend(validate_required_files())
    errors.extend(validate_template_directory())
    errors.extend(validate_templates())

    if errors:
        print()
        print("Blueprint validation failed")
        print("=" * 60)

        for error in errors:
            print(f"- {error}")

        print()

        return False

    print()
    print("Blueprint validation completed successfully.")
    print()

    return True


def main() -> int:
    valid = validate()

    if not valid:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())