from services.llm_service import generate_answer
from services.query_service import semantic_search

def rag_answer(question: str, candidates: list[tuple[str, dict]]) -> str:
    context = "\n\n".join(
        f"- {document} (category: {meta['category']}, diet: {meta['diet']}, price: ${meta['price']}, ingredients: {meta['ingredients']})"
        for document, meta in candidates
    )


    prompt = f"""
You are an assistant answering questions using only the provided context.

Context:
{context}

Question:
{question}

If the context does not contain the answer, say you don't have that information.
Answer clearly and concisely. Be nice and polite, like a restaurant server, justifying and explaining the chosen menu items, but always succinct. All prices are in dollars. 
Use ONLY plain text; NEVER use markdown or other formatting.
"""

    print("RAG Prompt:", prompt)

    return generate_answer(prompt)
