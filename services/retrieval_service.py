from core.embeddings import get_embedding_model
from core.vectorstore import get_chroma_collection
from domain.query_plan import QueryPlan

def retrieve_candidates(
    niche: str,
    plan: QueryPlan,
):
    model = get_embedding_model()
    collection = get_chroma_collection(niche)

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

    if "semantic" in plan.capabilities:
        model = get_embedding_model()
        embedding = model.encode([plan.question]).tolist()

        results = collection.query(
            query_embeddings=embedding,
            n_results=plan.candidate_limit,
            where=where if where else None,
            include=["documents", "metadatas"],
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
    else:
        results = collection.get(
            where=where if where else None,
            limit=plan.candidate_limit * 5,
            include=["documents", "metadatas"],
        )

        documents = results["documents"]
        metadatas = results["metadatas"]

    return list(zip(documents, metadatas))
