from sklearn.metrics.pairwise import cosine_similarity
from core.embeddings import get_embedding_model
from domain.query_plan import SemanticConstraint


def semantic_rerank(
    candidates: list[tuple[str, dict]],
    constraint: SemanticConstraint,
    top_k: int = 10,
):
    if not candidates:
        return candidates

    model = get_embedding_model()

    texts = [document for document, _ in candidates]

    query_embedding = model.encode([constraint.query])

    doc_embeddings = model.encode(texts)

    scores = cosine_similarity(query_embedding, doc_embeddings)[0]

    ranked = sorted(
        zip(candidates, scores),
        key=lambda x: x[1],
        reverse=True,
    )

    return [candidate for candidate, _ in ranked[:top_k]]
