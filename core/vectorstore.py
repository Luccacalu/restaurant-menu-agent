import chromadb

def get_chroma_collection(niche: str, collection_name: str = "documents"):
    client = chromadb.PersistentClient(path=f"data/{niche}")

    return client.get_or_create_collection(name=collection_name)
