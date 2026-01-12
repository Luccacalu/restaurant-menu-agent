# 🍽️ Restaurant Menu RAG – Proof of Concept

This project is a **Proof of Concept (PoC)** of a **Retrieval-Augmented Generation (RAG)** system applied to a restaurant menu.

It was built as a MVP to demonstrate:
- Vector databases
- Embeddings
- LLM orchestration
- End-to-end RAG architecture
- Admin vs User interfaces

---

## ✨ Overview

The system allows:

### 👨‍🍳 Admin
- Add new menu items
- Edit existing items
- Remove items

### 👤 User
- Ask natural language questions about the menu
- Receive grounded answers based only on menu data

Menu items are embedded using **SentenceTransformers** and stored in **ChromaDB**.  
User questions are embedded and matched via **semantic search**, optionally constrained by **structured filters extracted by an LLM**.

---

## 🧠 Architecture

### Admin flow
```
Admin adds / edits menu item
→ SentenceTransformer generates embedding
→ ChromaDB upsert (document + metadata)
```

### User flow
```
User question
→ LLM extracts structured filters (diet, category, price)
→ SentenceTransformer embeds query
→ ChromaDB filtered vector search
→ LLM generates grounded answer
```

This design uses **two LLM layers**:
1. Filter extraction (structured reasoning)
2. Answer generation (natural language)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI for admin and user
- **SentenceTransformers** – embeddings
- **ChromaDB** – vector database
- **Ollama** – local LLM runtime
- **LLaMA 3.1 (8B)** – language model

---

## 📁 Project Structure

```
core/
  embeddings.py        # Embedding model loader
  vectorstore.py       # ChromaDB access

models/
  menu_item.py         # Menu item model

services/
  ingest_service.py    # Menu ingestion (upsert)
  query_service.py     # Semantic search
  rag_service.py       # RAG orchestration
  llm_service.py       # LLM calls via Ollama

scripts/
  bulk_ingest_menu.py  # Bulk menu ingestion

streamlit_app.py       # Streamlit interface
```

---

## 🤖 LLM Setup (Ollama)

This project runs the LLM **locally**, without external APIs.

### 1️⃣ Install Ollama
Download and install from:
```
https://ollama.com
```

### 2️⃣ Pull the required model
```bash
ollama pull llama3.1:8b
```

### 3️⃣ Start the Ollama service
```bash
ollama serve
```

### LLM integration (code)

```python
# services/llm_service.py

import ollama

def generate_answer(prompt: str) -> str:
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]
```

---

## 🚀 Running the Application

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit app
```bash
streamlit run streamlit_app.py
```

### 3️⃣ Open in browser
```
http://localhost:8501
```

---

## 📦 Bulk Menu Ingestion

```bash
python scripts/bulk_ingest_menu.py
```

This script:
- Supports large arrays of items
- Can be safely re-run to update existing items
