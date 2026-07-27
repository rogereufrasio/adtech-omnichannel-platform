"""
Architecture Documentation Inventory

Gera inventário dos documentos Markdown existentes no repositório.

Informações coletadas:
- Programa
- Documento
- Quantidade de linhas
- Tamanho do arquivo
- Última alteração

Uso:

python tools/architecture/inventory.py
"""

# tools/architecture/inventory.py

from pathlib import Path
from datetime import datetime


ROOT = Path("programs")

IGNORED_FILES = {
    "README.md"
}


def format_size(size):
    if size < 1024:
        return f"{size} B"

    if size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"

    return f"{size / (1024 * 1024):.1f} MB"


def analyze_document(path):
    content = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    stat = path.stat()

    return {
        "path": path,
        "lines": len(content.splitlines()),
        "size": stat.st_size,
        "modified": datetime.fromtimestamp(
            stat.st_mtime
        )
    }


def discover_programs():
    return [
        folder
        for folder in ROOT.iterdir()
        if folder.is_dir()
    ]


def discover_documents(program):
    documents = []

    for file in program.rglob("*.md"):
        if file.name in IGNORED_FILES:
            continue

        documents.append(
            analyze_document(file)
        )

    return documents


def main():

    programs = discover_programs()

    all_documents = []

    print("=" * 60)
    print("Architecture Documentation Inventory")
    print("=" * 60)

    for program in programs:

        documents = discover_documents(program)

        all_documents.extend(documents)

        print()
        print(f"Program: {program.name}")
        print(f"Documents: {len(documents)}")
        print(
            f"Lines: {sum(d['lines'] for d in documents)}"
        )

    print()
    print("-" * 60)

    total_lines = sum(
        d["lines"]
        for d in all_documents
    )

    total_size = sum(
        d["size"]
        for d in all_documents
    )

    print(f"Programs analyzed: {len(programs)}")
    print(f"Documents: {len(all_documents)}")
    print(f"Markdown lines: {total_lines:,}")
    print(
        f"Total size: {format_size(total_size)}"
    )

    print()
    print("=" * 60)
    print("Document Details")
    print("=" * 60)

    for document in sorted(
        all_documents,
        key=lambda x: str(x["path"])
    ):

        print()
        print(document["path"])
        print(
            f"Lines: {document['lines']} | "
            f"Size: {format_size(document['size'])} | "
            f"Modified: "
            f"{document['modified'].strftime('%Y-%m-%d %H:%M')}"
        )


if __name__ == "__main__":
    main()