from core.embeddings import get_embedding_model
from core.vectorstore import get_chroma_collection

def ingest_menu_item(
    id: str,
    name: str,
    description: str,
    category: str,
    diet: str,
    price: float,
    ingredients: list[str],
    niche: str = "restaurant"
):
    model = get_embedding_model()
    collection = get_chroma_collection(niche)

    document = f"{name}. {description}"

    embedding = model.encode([document]).tolist()

    metadata = {
        "name": name,
        "category": category,
        "diet": diet,
        "price": price,
        "ingredients": [i.lower() for i in ingredients],
    }

    collection.upsert(
        ids=[id],
        documents=[document],
        embeddings=embedding,
        metadatas=[metadata]
    )
