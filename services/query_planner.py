import json
from typing import Any
from services.llm_service import generate_answer
from domain.query_plan import (
    QueryPlan,
    Filters,
    SortSpec,
    SemanticConstraint,
)

QUERY_PLANNER_PROMPT = """
You are a query planner for a restaurant menu search system.

Your task is to convert a natural language question into a structured query plan.

You MUST return ONLY parsable valid JSON.
NO explanations.
NO markdown.
NO comments.

PURE VALID JSON.

--------------------
CAPABILITIES:
- "filters": hard constraints (diet, category, ingredients, price) that MUST be strictly applied
- "semantic": subjective preferences (taste, pairing, style) that'll be handled by a semantic search
- "extrema": sorting like cheapest or most expensive

--------------------
RULES:

- If the question isn't in english, translate all fields to english.
- Include ONLY the capabilities that are explicitly or clearly implied.
- If a field is not mentioned, use null.
- If something is ambiguous, not specified, or user is not entirely sure, use null.
- ingredient lists must be arrays of lowercase strings.
- For semantic constraints, combine all semantic preferences into a single query string.
- If the question isn't in english, translate the semantic constraints to english.
- For price filters, if no absolutely certain min or max is mentioned, use null.
- If the user says "cheapest", use sort by price ascending.
- If no sort is mentioned, sort MUST be null.
- candidate_limit should be between 20 and 40 (default 30).
- It have at least one capability. It can have multiple capabilities. If unsure use semantic.

--------------------
SCHEMA:

{
  "capabilities": ["filters", "semantic", "extrema"],
  "filters": {
    "diet": "vegan | vegetarian | pescatarian | omnivore | null",
    "category": "main_course | appetizer | dessert | beverage | null",
    "ingredients_include": ["string"] | null,
    "ingredients_exclude": ["string"] | null,
    "price_min": number | null,
    "price_max": number | null
  },
  "semantic_constraint": {
    "query": "string"
  } | null
  },
  "sort": {
    "field": "price",
    "order": "asc | desc"
  } | null,
  "candidate_limit": number
}

ALL of the fields above MUST be present in your output JSON. Always use null if you're not sure about a field.

--------------------
EXAMPLES:

User: "cheapest vegan main course with rice, no beans, goes well with wine, and I hate bitter stuff."
Output:
{
  "capabilities": ["filters", "semantic", "extrema"],
  "filters": {
    "diet": "vegan",
    "category": "main_course",
    "ingredients_include": ["rice"],
    "ingredients_exclude": ["beans"],
    "price_min": null,
    "price_max": null
  },
  "semantic_constraint": {
    "query": "goes well with wine, not bitter"
  },
  "sort": {
    "field": "price",
    "order": "asc"
  },
  "candidate_limit": 30
}

--------------------
User question:
"""

def build_query_plan(question: str) -> QueryPlan:
    prompt = QUERY_PLANNER_PROMPT + question

    response = generate_answer(prompt).strip()

    print("---------------------\n")
    print("Query Planner raw response: ")
    print(response)
    print("\n---------------------")

    try:
        data: dict[str, Any] = json.loads(response)
    except json.JSONDecodeError as e:
        raise ValueError("Query planner returned invalid JSON") from e

    return QueryPlan(
        capabilities=data["capabilities"],
        filters=Filters(**data["filters"]) if data.get("filters") else None,
        semantic_constraint=(
            SemanticConstraint(**data["semantic_constraint"])
            if data.get("semantic_constraint")
            else None
        ),
        sort=SortSpec(**data["sort"]) if data.get("sort") else None,
        candidate_limit=data.get("candidate_limit", 30),
        question=question,
    )
