# tools/architecture/quality_gate.py

from pathlib import Path
import re


ROOT = Path("programs")

IGNORED_FILES = {
    "README.md"
}


REQUIRED_METADATA = [
    "Informações do Documento",
    "Documento",
    "Versão",
    "Status"
]


REQUIRED_WARNINGS = {
    "references": [
        "Referências",
        "References",
        "Relação com"
    ],
    "decisions": [
        "Decisões Arquiteturais",
        "Architectural Decisions"
    ],
    "next_steps": [
        "Próximos Passos",
        "Next Steps"
    ]
}


ERRORS = []
WARNINGS = []


def load_documents():

    documents = []

    for file in ROOT.rglob("*.md"):

        if file.name in IGNORED_FILES:
            continue

        documents.append(file)

    return sorted(documents)


def check_empty_document(path, content):

    if not content.strip():

        ERRORS.append(
            f"Empty document: {path}"
        )


def check_title(path, content):

    if not re.search(
        r"^#\s+.+",
        content,
        re.MULTILINE
    ):

        ERRORS.append(
            f"Missing title: {path}"
        )


def check_metadata(path, content):

    missing = []

    for item in REQUIRED_METADATA:

        if item.lower() not in content.lower():

            missing.append(item)

    if missing:

        WARNINGS.append(
            f"{path} missing metadata: "
            f"{', '.join(missing)}"
        )


def check_sections(path, content):

    for section, patterns in REQUIRED_WARNINGS.items():

        found = any(
            pattern.lower()
            in content.lower()
            for pattern in patterns
        )

        if not found:

            WARNINGS.append(
                f"{path} missing section: {section}"
            )


def check_filename(path):

    filename = path.stem

    if " " in filename:

        ERRORS.append(
            f"Invalid filename with spaces: {path}"
        )


def validate_documents():

    documents = load_documents()

    for document in documents:

        content = document.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        check_empty_document(
            document,
            content
        )

        check_title(
            document,
            content
        )

        check_metadata(
            document,
            content
        )

        check_sections(
            document,
            content
        )

        check_filename(
            document
        )

    return documents


def calculate_score(total):

    if total == 0:
        return 0

    penalty = (
        len(ERRORS) * 3
        +
        len(WARNINGS)
    )

    score = 100 - (
        penalty / total * 10
    )

    return max(
        0,
        round(score, 1)
    )


def print_report(documents):

    score = calculate_score(
        len(documents)
    )

    print("=" * 60)
    print("Architecture Quality Gate")
    print("=" * 60)

    print()

    print(
        f"Documents analyzed: {len(documents)}"
    )

    print(
        f"Quality Score: {score}%"
    )

    print()

    print("Checks:")
    print()
    print("✓ Markdown structure")
    print("✓ Required metadata")
    print("✓ Required sections")
    print("✓ Naming conventions")
    print("✓ Empty documents")

    print()

    if ERRORS:

        print("Errors:")

        for error in ERRORS:

            print(
                f"- {error}"
            )

    else:

        print("Errors:")
        print("0")

    print()

    if WARNINGS:

        print("Warnings:")

        for warning in WARNINGS[:20]:

            print(
                f"- {warning}"
            )

        if len(WARNINGS) > 20:

            print(
                f"- +{len(WARNINGS)-20} additional warnings"
            )

    else:

        print("Warnings:")
        print("0")

    print()

    if ERRORS:

        print(
            "Result: FAIL"
        )

    else:

        print(
            "Result: PASS"
        )


def main():

    documents = validate_documents()

    print_report(
        documents
    )

    if ERRORS:

        exit(1)


if __name__ == "__main__":
    main()