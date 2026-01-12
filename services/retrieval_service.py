from core.embeddings import get_embedding_model
from core.vectorstore import get_chroma_collection
from domain.query_plan import QueryPlan

def retrieve_candidates(
    query: str,
    niche: str,
    plan: QueryPlan,
):
    model = get_embedding_model()
    collection = get_chroma_collection(niche)

    query_embedding = model.encode([query]).tolist()

    where = {}

    if plan.filters:
        if plan.filters.diet:
            where["diet"] = plan.filters.diet

        if plan.filters.category:
            where["category"] = plan.filters.category

        if plan.filters.price_min is not None or plan.filters.price_max is not None:
            price_filter = {}

            if plan.filters.price_min is not None:
                price_filter["$gte"] = plan.filters.price_min

            if plan.filters.price_max is not None:
                price_filter["$lte"] = plan.filters.price_max

            where["price"] = price_filter

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=plan.candidate_limit,
        where=where if where else None,
        include=["documents", "metadatas"],
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return list(zip(documents, metadatas))
