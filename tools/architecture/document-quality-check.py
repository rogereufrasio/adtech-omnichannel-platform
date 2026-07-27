from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
PROGRAMS_DIR = ROOT / "programs"


REQUIRED_SECTIONS = [
    "# ",
]

QUALITY_RULES = {
    "title": lambda content: bool(re.search(r"^#\s+.+", content, re.MULTILINE)),
    "context": lambda content: "Contexto" in content or "Context" in content,
    "references": lambda content: (
        "Referências" in content
        or "References" in content
        or "Relação com" in content
    ),
    "decision": lambda content: (
        "Decisões Arquiteturais" in content
        or "Architecture Decision" in content
        or "Decision" in content
    ),
}


def find_documents():
    return sorted(PROGRAMS_DIR.rglob("*.md"))


def evaluate_document(path):
    content = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    result = {
        "path": str(path.relative_to(ROOT)),
        "title": QUALITY_RULES["title"](content),
        "context": QUALITY_RULES["context"](content),
        "references": QUALITY_RULES["references"](content),
        "decision": QUALITY_RULES["decision"](content),
    }

    return result


def generate_summary(results):
    total = len(results)

    print("=" * 60)
    print("Architecture Documentation Quality Check")
    print("=" * 60)
    print()

    print(f"Documents analyzed: {total}")
    print()

    for key, label in [
        ("title", "With title"),
        ("context", "With context section"),
        ("references", "With references"),
        ("decision", "With architectural decisions"),
    ]:
        count = sum(
            1 for item in results
            if item[key]
        )

        print(f"{label}: {count}")

    print()

    missing = [
        item
        for item in results
        if not item["title"]
    ]

    print("-" * 60)
    print("Documents without title")
    print("-" * 60)

    if not missing:
        print("None")
    else:
        for item in missing:
            print(item["path"])


def generate_quality_issues(results):
    print()
    print("=" * 60)
    print("Quality Issues")
    print("=" * 60)
    print()

    issues = []

    for item in results:

        missing = []

        for key, label in [
            ("title", "Title"),
            ("context", "Context"),
            ("references", "References"),
        ]:
            if not item[key]:
                missing.append(label)

        if missing:
            issues.append(
                {
                    "path": item["path"],
                    "issues": missing
                }
            )

    if not issues:
        print("No quality issues found.")
        return

    for issue in issues:
        print(issue["path"])
        print(
            "  Missing: "
            + ", ".join(issue["issues"])
        )


def main():

    documents = find_documents()

    results = [
        evaluate_document(doc)
        for doc in documents
    ]

    generate_summary(results)
    generate_quality_issues(results)


if __name__ == "__main__":
    main()