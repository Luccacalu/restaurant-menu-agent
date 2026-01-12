from services.filter_service import extract_filters
from services.llm_service import generate_answer
from services.query_service import semantic_search

def rag_answer(question: str, niche: str, top_k: int = 10) -> str:
    filters = extract_filters(question)

    results = semantic_search(
        query=question,
        niche=niche,
        filters=filters,
        top_k=top_k
    )

    if not results:
        return "I couldn't find any menu items matching your request."

    context = "\n\n".join(
        f"- {document} (category: {meta['category']}, diet: {meta['diet']}, price: ${meta['price']})"
        for document, meta in results
    )


    prompt = f"""
You are an assistant answering questions using only the provided context.

Context:
{context}

Question:
{question}

If the context does not contain the answer, say you don't have that information.
Answer clearly and concisely. Be nice and polite, like a restaurant server, but always succinct. All prices are in dollars. 
Use only plain text; do not use markdown or other formatting.
"""

    print("RAG Prompt:", prompt)

    return generate_answer(prompt)
