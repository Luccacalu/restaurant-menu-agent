from domain.query_plan import Filters

def apply_ingredient_filters(
    candidates: list[tuple[str, dict]],
    filters: Filters | None,
):
    if not filters:
        return candidates

    include = set(filters.ingredients_include or [])
    exclude = set(filters.ingredients_exclude or [])

    if not include and not exclude:
        return candidates

    filtered = []

    for document, meta in candidates:
        ingredients = set(meta.get("ingredients", []))

        if exclude and ingredients.intersection(exclude):
            continue

        #if include and not include.issubset(ingredients):
        #    continue

        filtered.append((document, meta))

    return filtered