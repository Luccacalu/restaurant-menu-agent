from dataclasses import dataclass
from typing import List, Optional, Literal


Capability = Literal[
    "filters",
    "extrema",
    "semantic"
]

Diet = Literal[
    "vegan",
    "vegetarian",
    "pescatarian",
    "omnivore",
]

Category = Literal[
    "main_course",
    "appetizer",
    "dessert",
    "beverage",
]

@dataclass
class SortSpec:
    field: Literal["price"]
    order: Literal["asc", "desc"]


@dataclass
class Filters:
    diet: Optional[Diet] = None
    category: Optional[Category] = None
    ingredients_include: Optional[List[str]] = None
    ingredients_exclude: Optional[List[str]] = None
    price_min: Optional[float] = None
    price_max: Optional[float] = None


@dataclass
class SemanticConstraint:
    query: str


@dataclass
class QueryPlan:
    capabilities: List[Capability]
    filters: Optional[Filters] = None
    sort: Optional[SortSpec] = None
    semantic_constraint: Optional[SemanticConstraint] = None
    candidate_limit: int = 20
    question: str = ""