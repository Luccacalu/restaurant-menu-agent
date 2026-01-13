from core.embeddings import get_embedding_model
from core.vectorstore import get_chroma_collection

def semantic_search(
    query: str,
    niche: str,
    filters: dict | None = None,
    top_k: int = 10
):
    model = get_embedding_model()
    collection = get_chroma_collection(niche)

    query_embedding = model.encode([query]).tolist()

    where = {}

    if filters:
        if filters.get("diet"):
            where["diet"] = filters["diet"]

        if filters.get("category"):
            where["category"] = filters["category"]

        if filters.get("price_max") is not None:
            where["price"] = {"$lte": filters["price_max"]}

        if filters.get("price_min") is not None:
            where["price"] = {"$gte": filters["price_min"]}

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
        include=['documents', 'metadatas'],
        where=where if where else None
    )

    print("---------------------\n")
    print("Semantic Search Results:", results)
    print("\n---------------------")

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return list(zip(documents, metadatas))
