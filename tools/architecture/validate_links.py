"""
Architecture Documentation Link Validator

Valida links internos entre documentos Markdown.

Verifica:
- links relativos quebrados;
- arquivos inexistentes;
- referências inválidas.

Uso:

python tools/architecture/validate_links.py
"""

import re
from pathlib import Path


ROOT_PATH = Path(__file__).resolve().parents[2]
PROGRAMS_PATH = ROOT_PATH / "programs"


MARKDOWN_LINK_PATTERN = re.compile(
    r"\[.*?\]\((.*?)\)"
)


def collect_markdown_files():
    """
    Retorna todos os arquivos Markdown do repositório.
    """

    return list(
        ROOT_PATH.rglob("*.md")
    )


def extract_links(content: str):
    """
    Extrai links Markdown.
    """

    return MARKDOWN_LINK_PATTERN.findall(
        content
    )


def is_external_link(link: str):
    """
    Ignora links externos.
    """

    return (
        link.startswith("http://")
        or link.startswith("https://")
        or link.startswith("#")
    )


def validate_link(
    source_file: Path,
    link: str
):
    """
    Valida um link relativo.

    Retorna None quando válido.
    Retorna mensagem quando inválido.
    """

    if is_external_link(link):
        return None

    target_path = (
        source_file.parent / link
    ).resolve()

    if not target_path.exists():

        return (
            f"{source_file.relative_to(ROOT_PATH)}\n"
            f"  -> {link}\n"
            f"  Arquivo não encontrado"
        )

    return None


def validate_documents():

    broken_links = []
    total_links = 0

    documents = collect_markdown_files()

    for document in documents:

        content = document.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        links = extract_links(
            content
        )

        total_links += len(links)

        for link in links:

            error = validate_link(
                document,
                link
            )

            if error:

                broken_links.append(
                    error
                )

    return (
        len(documents),
        total_links,
        broken_links
    )


def print_report(
    documents,
    total_links,
    broken_links
):

    print()
    print("=" * 60)
    print("Architecture Link Validation")
    print("=" * 60)
    print()

    print(
        f"Documents scanned: {documents}"
    )

    print(
        f"Links found: {total_links}"
    )

    print(
        f"Valid links: "
        f"{total_links - len(broken_links)}"
    )

    print(
        f"Broken links: "
        f"{len(broken_links)}"
    )

    print()

    if broken_links:

        print("-" * 60)
        print("Broken Links")
        print("-" * 60)

        for broken in broken_links:

            print()
            print(broken)

    else:

        print(
            "No broken links found."
        )

    print()


def main():

    documents, total_links, broken_links = (
        validate_documents()
    )

    print_report(
        documents,
        total_links,
        broken_links
    )


if __name__ == "__main__":
    main()