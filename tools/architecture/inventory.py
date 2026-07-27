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

from pathlib import Path
from datetime import datetime


ROOT_PATH = Path(__file__).resolve().parents[2]
PROGRAMS_PATH = ROOT_PATH / "programs"


def format_size(size_bytes: int) -> str:
    """
    Converte bytes para formato legível.
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"

    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"

    return f"{size_bytes / (1024 * 1024):.1f} MB"


def get_program_name(file_path: Path) -> str:
    """
    Identifica o programa baseado na estrutura:

    programs/
        programa/
            arquivo.md
    """

    try:
        relative = file_path.relative_to(PROGRAMS_PATH)
        return relative.parts[0]

    except ValueError:
        return "unknown"


def collect_documents():
    """
    Busca todos os arquivos Markdown dentro de programs.
    """

    documents = []

    for markdown_file in PROGRAMS_PATH.rglob("*.md"):

        content = markdown_file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        metadata = markdown_file.stat()

        documents.append(
            {
                "program": get_program_name(markdown_file),
                "document": str(
                    markdown_file.relative_to(ROOT_PATH)
                ),
                "lines": len(content.splitlines()),
                "size": format_size(metadata.st_size),
                "modified": datetime.fromtimestamp(
                    metadata.st_mtime
                ).strftime("%Y-%m-%d %H:%M"),
            }
        )

    return documents


def print_summary(documents):

    total_lines = sum(
        document["lines"]
        for document in documents
    )

    total_size = sum(
        Path(ROOT_PATH / document["document"]).stat().st_size
        for document in documents
    )

    programs = sorted(
        set(
            document["program"]
            for document in documents
        )
    )

    print()
    print("=" * 60)
    print("Architecture Documentation Inventory")
    print("=" * 60)
    print()

    print(f"Programs analyzed: {len(programs)}")
    print(f"Documents: {len(documents)}")
    print(f"Markdown lines: {total_lines:,}")
    print(f"Total size: {format_size(total_size)}")

    print()
    print("-" * 60)

    for program in programs:

        program_documents = [
            document
            for document in documents
            if document["program"] == program
        ]

        lines = sum(
            document["lines"]
            for document in program_documents
        )

        print()
        print(f"Program: {program}")
        print(f"Documents: {len(program_documents)}")
        print(f"Lines: {lines:,}")

    print()


def print_details(documents):

    print("=" * 60)
    print("Document Details")
    print("=" * 60)

    for document in sorted(
        documents,
        key=lambda item: item["document"]
    ):

        print()
        print(document["document"])
        print(
            f"Lines: {document['lines']} | "
            f"Size: {document['size']} | "
            f"Modified: {document['modified']}"
        )


def main():

    if not PROGRAMS_PATH.exists():

        print(
            "Directory programs not found:"
            f" {PROGRAMS_PATH}"
        )

        return

    documents = collect_documents()

    if not documents:

        print(
            "No Markdown documents found."
        )

        return

    print_summary(documents)

    print_details(documents)


if __name__ == "__main__":
    main()