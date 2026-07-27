from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]

TOOLS_DIR = ROOT / "tools" / "architecture"


SCRIPTS = [
    "inventory.py",
    "validate_links.py",
    "document_report.py",
    "document-quality-check.py",
]


def run_script(script):

    path = TOOLS_DIR / script

    print("=" * 60)
    print(f"Running: {script}")
    print("=" * 60)

    result = subprocess.run(
        [
            sys.executable,
            str(path)
        ],
        cwd=ROOT
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Failed: {script}"
        )


def main():

    print(
        "Architecture Documentation Validation"
    )

    print()

    for script in SCRIPTS:
        run_script(script)

    print()
    print("=" * 60)
    print(
        "Documentation validation completed successfully"
    )
    print("=" * 60)


if __name__ == "__main__":
    main()