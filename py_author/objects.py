from dataclasses import dataclass


@dataclass
class Character:
    """Characters are created and tracked using this class."""
    name: str
    org: dict
    event: dict
