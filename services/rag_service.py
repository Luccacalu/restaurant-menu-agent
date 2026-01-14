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
Answer clearly and concisely. Be nice and polite, like a restaurant server, talking a bit about the chosen menu items in a pleasant way, but always succinct. All prices are in dollars. 
Use ONLY plain text; NEVER use markdown or other formatting.

Your answer should be in the original language of the question. Feel free to translate the menu item names and descriptions if needed. Translate the menu items names.
"""

    print("RAG Prompt:", prompt)

    return generate_answer(prompt)
