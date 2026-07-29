from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class BlueprintDirectory:
    """Represents a directory inside a Program Blueprint."""

    name: str
    files: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ProgramBlueprint:
    """Represents the complete Program Blueprint."""

    root_files: list[str]
    directories: list[BlueprintDirectory]