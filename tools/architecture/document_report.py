from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parents[2]
PROGRAMS_DIR = ROOT / "programs"
REPORTS_DIR = ROOT / "reports"

OUTPUT_FILE = REPORTS_DIR / "architecture-documentation-report.md"


def find_documents():
    return sorted(PROGRAMS_DIR.rglob("*.md"))


def analyze_documents(documents):
    result = []

    for document in documents:
        content = document.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        result.append(
            {
                "path": str(document.relative_to(ROOT)),
                "size": document.stat().st_size,
                "modified": datetime.fromtimestamp(
                    document.stat().st_mtime
                ).strftime("%Y-%m-%d"),
                "title": content.startswith("# "),
                "context": (
                    "Contexto" in content
                    or "Context" in content
                ),
                "references": (
                    "Referências" in content
                    or "References" in content
                    or "Relação com" in content
                ),
            }
        )

    return result


def generate_report(data):

    REPORTS_DIR.mkdir(
        exist_ok=True
    )

    total = len(data)

    with_title = sum(
        1 for item in data
        if item["title"]
    )

    with_context = sum(
        1 for item in data
        if item["context"]
    )

    with_references = sum(
        1 for item in data
        if item["references"]
    )

    report = []

    report.append(
        "# Architecture Documentation Report\n"
    )

    report.append(
        "## Summary\n"
    )

    report.append(
        f"- Total documents: {total}\n"
    )

    report.append(
        f"- Documents with title: {with_title}\n"
    )

    report.append(
        f"- Documents with context section: {with_context}\n"
    )

    report.append(
        f"- Documents with references: {with_references}\n"
    )

    report.append(
        "\n---\n\n"
    )

    report.append(
        "## Document Inventory\n\n"
    )

    report.append(
        "| Document | Size | Last Modified |\n"
    )

    report.append(
        "|---|---|---|\n"
    )

    for item in data:

        report.append(
            f"| {item['path']} | "
            f"{item['size']} bytes | "
            f"{item['modified']} |\n"
        )

    OUTPUT_FILE.write_text(
        "".join(report),
        encoding="utf-8"
    )

    print(
        f"Report generated: {OUTPUT_FILE}"
    )


def main():

    documents = find_documents()

    analyzed = analyze_documents(
        documents
    )

    generate_report(
        analyzed
    )


if __name__ == "__main__":
    main()