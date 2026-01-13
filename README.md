# 🍽️ Restaurant Menu RAG – Proof of Concept

This project is a **Proof of Concept (PoC)** and MVP of a **Retrieval-Augmented Generation (RAG)** system applied to a restaurant menu, which you can use to answer natural language questions about menu items, asking for recommendations, filtering by dietary preferences, ingredients, price, and more.

It demonstrates:
- Vector databases
- Embeddings
- LLM orchestration
- Structured query planning
- Intent extraction
- Semantic filtering and sorting
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
- Receive grounded answers based **only** on menu data
- Ask complex queries like:
  > “Give me the cheapest 5 vegan options with rice, no beans, that go well with wine. Also, I don't like bitter ingredients.”

Menu items are embedded using **SentenceTransformers** and stored in **ChromaDB**.  
User questions are converted into a **query plan** that controls filtering, sorting, and semantic reasoning.

---

## 🧠 Architecture

### Admin flow
```
Admin UI
→ Menu item ingestion
→ SentenceTransformer generates embedding
→ ChromaDB upsert (document + metadata)
```

### User flow
```
User question
→ Query Planner (LLM)
→ Structured query plan (filters / extrema / semantic)
→ ChromaDB retrieval
→ Optional semantic reranking
→ RAG answer generation (LLM)
```

The system uses **two LLM stages**:
1. **Query planning** – extracts structured intent (filters, sorting, semantic constraints)
2. **Answer generation** – produces a grounded natural language answer

The `capabilities` field in the query plan determines which stages execute.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Admin & User UI
- **SentenceTransformers** – embeddings
- **ChromaDB** – vector database (local, persistent)
- **Ollama** – local LLM runtime
- **LLaMA 3.1 (8B)** – language model

All inference runs **locally**. No external APIs are required.

---

## 📁 Project Structure

```
core/
  embeddings.py        # Embedding model loader
  vectorstore.py       # ChromaDB access

domain/
  query_plan.py        # Query plan schema

models/
  menu_item.py         # Domain model

services/
  ingest_service.py        # Menu ingestion
  retrieval_service.py     # Candidate retrieval
  ingredient_filter_service.py
  semantic_rerank_service.py
  query_planner.py         # LLM-based planner
  query_execution_service.py
  rag_service.py           # RAG orchestration
  llm_service.py           # Ollama wrapper

scripts/
  bulk_ingest_menu.py      # Bulk menu ingestion

streamlit_app.py           # Streamlit interface
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
- Uses the same ingestion pipeline as the admin UI

---

## ⚠️ Notes & Limitations

- This is an MVP / PoC, not production-hardened
- ChromaDB uses local disk storage
- Ollama requires sufficient RAM (8GB recommended)

---
