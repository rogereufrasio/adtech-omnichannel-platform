# tools/architecture/architecture_catalog.py

from pathlib import Path
from datetime import datetime


PROGRAMS_ROOT = Path("programs")
OUTPUT_FILE = Path("docs/architecture-catalog.md")

IGNORED_FILES = {
    "README.md"
}


def discover_programs():
    return sorted(
        [
            folder
            for folder in PROGRAMS_ROOT.iterdir()
            if folder.is_dir()
        ],
        key=lambda x: x.name
    )


def discover_documents(program):
    documents = []

    for file in program.rglob("*.md"):

        if file.name in IGNORED_FILES:
            continue

        documents.append(file)

    return sorted(
        documents,
        key=lambda x: str(x)
    )


def detect_category(path):

    parts = path.parts

    categories = [
        "adrs",
        "architecture",
        "business-architecture",
        "information-architecture",
        "application-architecture",
        "technology-architecture",
        "governance",
        "roadmap",
        "diagrams",
        "docs",
        "events"
    ]

    for category in categories:

        if category in parts:
            return category.replace(
                "-",
                " "
            ).title()

    return "General"


def create_relative_link(path):

    return path.as_posix()


def generate_catalog():

    lines = []

    lines.append(
        "# Architecture Catalog"
    )

    lines.append("")

    lines.append(
        f"Generated: {datetime.now().strftime('%Y-%m-%d')}"
    )

    lines.append("")

    lines.append(
        "## Programs"
    )

    lines.append("")

    programs = discover_programs()

    landscape = []

    for program in programs:

        documents = discover_documents(
            program
        )

        if not documents:
            continue

        lines.append(
            f"## {program.name}"
        )

        lines.append("")

        lines.append(
            f"Documents: {len(documents)}"
        )

        lines.append("")

        categories = {}

        for document in documents:

            category = detect_category(
                document
            )

            categories.setdefault(
                category,
                []
            )

            categories[category].append(
                document
            )

        lines.append(
            "Categories:"
        )

        lines.append("")

        for category in sorted(categories):

            lines.append(
                f"- {category}"
            )

        lines.append("")

        landscape.append(
            {
                "program": program.name,
                "documents": len(documents)
            }
        )

        lines.append(
            "### Documents"
        )

        lines.append("")

        for document in documents:

            title = document.stem.replace(
                "-",
                " "
            ).replace(
                "_",
                " "
            ).title()

            link = create_relative_link(
                document
            )

            lines.append(
                f"- [{title}]({link})"
            )

        lines.append("")


    lines.append(
        "## Architecture Landscape"
    )

    lines.append("")

    lines.append(
        "| Program | Documents |"
    )

    lines.append(
        "|---|---|"
    )

    for item in landscape:

        lines.append(
            f"| {item['program']} | {item['documents']} |"
        )

    lines.append("")

    return "\n".join(lines)


def main():

    catalog = generate_catalog()

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_FILE.write_text(
        catalog,
        encoding="utf-8"
    )

    print(
        "Architecture catalog generated:"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":
    main()