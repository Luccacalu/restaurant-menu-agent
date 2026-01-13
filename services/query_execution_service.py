from services.rag_service import rag_answer
from services.reranking_service import semantic_rerank
from services.retrieval_service import retrieve_candidates
from services.ingredient_filter_service import apply_ingredient_filters
from domain.query_plan import QueryPlan


def execute_query_plan(
    question: str,
    niche: str,
    plan: QueryPlan,
) -> str:
    candidates = retrieve_candidates(
        niche=niche,
        plan=plan,
    )

    if not candidates:
        return "I couldn't find any menu items matching your request."

    if "filters" in plan.capabilities and plan.filters:
        candidates = apply_ingredient_filters(candidates, plan.filters)

    if not candidates:
        return "I couldn't find any menu items matching your request."

    if "extrema" in plan.capabilities and plan.sort:
        reverse = plan.sort.order == "desc"

        candidates.sort(
            key=lambda x: x[1]["price"],
            reverse=reverse,
        )

    if "semantic" in plan.capabilities and plan.semantic_constraint:
        candidates = semantic_rerank(
            candidates=candidates,
            constraint=plan.semantic_constraint,
            top_k=10,
        )
    else:
        candidates = candidates[:10]

    return rag_answer(question, candidates)
