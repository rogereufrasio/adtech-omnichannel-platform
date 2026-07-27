"""
Architecture Documentation Report Generator

Gera um relatório de qualidade da documentação arquitetural.

Analisa documentos Markdown considerando:

- quantidade total de documentos;
- documentos com título principal;
- documentos com seção Contexto;
- documentos com referências;
- documentos sem revisão.

Uso:

python tools/architecture/document_report.py
"""

from pathlib import Path
import re
from datetime import datetime


ROOT_PATH = Path(__file__).resolve().parents[2]


MARKDOWN_PATHS = [
    ROOT_PATH / "programs"
]


def collect_documents():
    """
    Coleta todos os arquivos Markdown
    """

    documents = []

    for path in MARKDOWN_PATHS:

        if path.exists():

            documents.extend(
                path.rglob("*.md")
            )

    return documents


def has_title(content: str):
    """
    Verifica existência de título Markdown.
    """

    return bool(
        re.search(
            r"^#\s+.+",
            content,
            re.MULTILINE
        )
    )


def has_context_section(content: str):
    """
    Verifica se possui seção de contexto.
    """

    patterns = [
        r"#\s+Contexto",
        r"##\s+Contexto",
        r"#\s+Context",
        r"##\s+Context"
    ]

    return any(
        re.search(
            pattern,
            content,
            re.IGNORECASE
        )
        for pattern in patterns
    )


def has_reference_section(content: str):
    """
    Verifica referências ou relacionamentos.
    """

    patterns = [
        r"#\s+Referências",
        r"##\s+Referências",
        r"#\s+Relacionamento",
        r"#\s+Relação com",
        r"#\s+Documentos relacionados"
    ]

    return any(
        re.search(
            pattern,
            content,
            re.IGNORECASE
        )
        for pattern in patterns
    )


def has_revision_marker(content: str):
    """
    Identifica documentos sem indicação de revisão.

    Considera como revisado documentos
    que possuem:

    - Versão
    - Status
    - Histórico
    - Revisão
    """

    patterns = [
        r"Versão",
        r"Status",
        r"Histórico",
        r"Revisão"
    ]

    return any(
        re.search(
            pattern,
            content,
            re.IGNORECASE
        )
        for pattern in patterns
    )


def analyze_documents():

    documents = collect_documents()

    result = {
        "total": len(documents),
        "with_title": 0,
        "with_context": 0,
        "with_references": 0,
        "without_revision": 0,
    }

    details = []


    for document in documents:

        content = document.read_text(
            encoding="utf-8",
            errors="ignore"
        )


        if has_title(content):
            result["with_title"] += 1


        if has_context_section(content):
            result["with_context"] += 1


        if has_reference_section(content):
            result["with_references"] += 1


        if not has_revision_marker(content):
            result["without_revision"] += 1


        details.append(
            {
                "file": str(
                    document.relative_to(ROOT_PATH)
                ),
                "size": document.stat().st_size,
                "updated": datetime.fromtimestamp(
                    document.stat().st_mtime
                ).strftime(
                    "%Y-%m-%d"
                )
            }
        )


    return result, details



def generate_report(
    result,
    details
):

    output = []


    output.append(
        "# Architecture Documentation Report\n"
    )

    output.append(
        "## Resumo\n"
    )

    output.append(
        f"- Total documentos: {result['total']}\n"
    )

    output.append(
        f"- Com título: {result['with_title']}\n"
    )

    output.append(
        f"- Com seção Contexto: {result['with_context']}\n"
    )

    output.append(
        f"- Com referências: {result['with_references']}\n"
    )

    output.append(
        f"- Sem revisão: {result['without_revision']}\n"
    )


    output.append(
        "\n---\n\n"
    )


    output.append(
        "## Inventário de Documentos\n\n"
    )


    output.append(
        "| Documento | Tamanho | Última alteração |\n"
    )

    output.append(
        "|---|---|---|\n"
    )


    for item in details:

        output.append(
            f"| {item['file']} | "
            f"{item['size']} bytes | "
            f"{item['updated']} |\n"
        )


    return "".join(output)



def main():

    result, details = analyze_documents()

    report = generate_report(
        result,
        details
    )


    output_file = (
        ROOT_PATH /
        "architecture-documentation-report.md"
    )


    output_file.write_text(
        report,
        encoding="utf-8"
    )


    print(
        f"Report generated: {output_file}"
    )



if __name__ == "__main__":

    main()