import json
from services.llm_service import generate_answer

def extract_filters(question: str) -> dict:
    prompt = f"""
Your only function is to extract structured filters from user questions about a restaurant menu.

Allowed values:
- diet: vegan | vegetarian | omnivore
- category: main_course | dessert | appetizer
- price_min: number or null
- price_max: number or null

Return ONLY valid JSON. Do NOT include any explanations. The response MUST BE PARSEABLE as JSON.
If a filter is not mentioned, use null.
If the prompt isn't totally clear or prohibitive about a filter, use null. Example: “prefer vegan but allow vegetarian”, use null for diet.
If it doesn't explicitly mention price limits, use null for price_min and price_max.

Schema example:

"diet": null,
"category": null,
"price_min": null,
"price_max": null

Each field MUST be either:
- a single string (NOT an array)
- a number
- null

Arrays are NEVER allowed.
If you return an array, the response is invalid.

User question:
{question}
"""

    response = generate_answer(prompt)

    print("-----------------------------------\n")
    print("Filter Extraction Response:", response.strip())
    print("\n-----------------------------------")

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "diet": None,
            "category": None,
            "price_min": None,
            "price_max": None
        }
