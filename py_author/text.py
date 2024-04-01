from dataclasses import dataclass
from datetime import date


@dataclass
class Scene:
    """Scene."""
    date: date
    summary: str
    text: str = ""
    characters: list = []
    places: list = []


def update_text(text):
    text = text.split(" ")
    characters = []
    for word in text:
        if "C?" in word:
            characters.append(word.replace("C?", ""))
""