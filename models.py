from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class GPT:
    token: str
    organization: str

# @dataclass
class Anchor(BaseModel):
    left_context: str
    anchor: str
    right_context: str

# @dataclass
class AnchorsResponse(BaseModel):
    anchors: list[Anchor]
    final_answer: str