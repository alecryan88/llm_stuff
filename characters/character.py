from pydantic import BaseModel
from enum import Enum


class CharacterType(Enum):
    Jedi = "Jedi"
    Sith = "Sith"
    Droid = "Droid"
    Other = "Other"


class Character(BaseModel):
    name: str
    # description: str
    family: str
    character_type: list[CharacterType]
    species: str
    masters: list[str]
    apprentices: list[str]
