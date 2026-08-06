from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
PROGRAMS_DIR = ROOT / "programs"


QUALITY_RULES = {
    "title": lambda content: bool(re.search(r"^#\s+.+", content, re.MULTILINE)),
    "context": lambda content: any(
        section in content
        for section in (
            "Contexto",
            "Executive Summary",
            "Objetivo",
            "Propósito",
            "Visão Geral",
        )
    ),
    "references": lambda content: (
        "Referências" in content
        or "References" in content
        or "Relação com" in content
        or bool(re.search(r"\[[^\]]+\]\([^)]+\)", content))
    ),
    "decision": lambda content: (
        "Decisões Arquiteturais" in content
        or "Architecture Decision" in content
        or "Decisão" in content
        or "Decision" in content
    ),
}


def find_documents():
    return sorted(PROGRAMS_DIR.rglob("*.md"))


def evaluate_document(path):
    content = path.read_text(encoding="utf-8", errors="ignore")
    return {
        "path": str(path.relative_to(ROOT)),
        **{name: rule(content) for name, rule in QUALITY_RULES.items()},
    }


def generate_summary(results):
    print("=" * 60)
    print("Validação de Qualidade da Documentação Arquitetural")
    print("=" * 60)
    print(f"Documentos analisados: {len(results)}")

    for key, label in (
        ("title", "Com título"),
        ("context", "Com contexto"),
        ("references", "Com referências"),
        ("decision", "Com decisões arquiteturais"),
    ):
        count = sum(1 for item in results if item[key])
        print(f"{label}: {count}")


def generate_quality_issues(results):
    issues = []
    labels = {
        "title": "Título",
        "context": "Contexto",
        "references": "Referências",
    }

    for item in results:
        missing = [label for key, label in labels.items() if not item[key]]
        if missing:
            issues.append((item["path"], missing))

    print("=" * 60)
    print("Inconsistências de Qualidade")
    print("=" * 60)

    if not issues:
        print("Nenhuma inconsistência encontrada.")
        return False

    for path, missing in issues:
        print(path)
        print("  Ausente: " + ", ".join(missing))

    return True


def main():
    results = [evaluate_document(doc) for doc in find_documents()]
    generate_summary(results)
    if generate_quality_issues(results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
