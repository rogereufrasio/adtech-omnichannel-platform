from __future__ import annotations

from tools.architecture.models import (
    BlueprintDirectory,
    ProgramBlueprint,
)


class BlueprintLoader:
    """
    Loads the Enterprise Architecture Program Blueprint.

    Initially the blueprint is represented in code.
    Future versions will load the structure directly from
    standards/program-blueprint.
    """

    @staticmethod
    def load() -> ProgramBlueprint:
        return ProgramBlueprint(
            root_files=[
                "README.md",
                "architecture-target-state.md",
                "executive-target-state.md",
                "maturity-assessment.md",
            ],
            directories=[
                BlueprintDirectory(
                    name="adrs",
                    files=["README.md"],
                ),
                BlueprintDirectory("business-architecture"),
                BlueprintDirectory("application-architecture"),
                BlueprintDirectory("information-architecture"),
                BlueprintDirectory("integration-architecture"),
                BlueprintDirectory("technology-architecture"),
                BlueprintDirectory("governance"),
                BlueprintDirectory("diagrams"),
                BlueprintDirectory("roadmap"),
                BlueprintDirectory("docs"),
            ],
        )