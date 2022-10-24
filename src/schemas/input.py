from src.schemas.base import ItemBase
from typing import Optional, List, Literal


class TextIn(ItemBase):
    text: str
    adequacy_threshold: float
    fluency_threshold: float
    diversity_ranker: str
