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
    
    if ingredients is None:
        ingredients_list = []
    elif isinstance(ingredients, str):
        ingredients_list = [
            i.strip().lower()
            for i in ingredients.split(",")
            if i.strip()
        ]
    elif isinstance(ingredients, list):
        ingredients_list = [str(i).lower().strip() for i in ingredients]
    else:
        raise ValueError(f"Invalid ingredients type: {type(ingredients)}")
    
    model = get_embedding_model()
    collection = get_chroma_collection(niche)

    document = f"{name}. {description}"

    embedding = model.encode([document]).tolist()

    print(f"Ingesting ingredients for {name}: {ingredients_list}")

    metadata = {
        "name": name,
        "category": category,
        "diet": diet,
        "price": price,
        "ingredients": ", ".join(ingredients_list),
    }

    collection.upsert(
        ids=[id],
        documents=[document],
        embeddings=embedding,
        metadatas=[metadata]
    )
