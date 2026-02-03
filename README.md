# EndeeRAG – AI-Powered Semantic Search & RAG with Endee

## 🚀 Project Overview

**EndeeRAG** is an intelligent AI system that combines **semantic search** with **Retrieval Augmented Generation (RAG)**. It leverages **Endee**, a high-performance vector database, to retrieve contextually relevant documents and feeds them into a **large language model (LLM)** to generate accurate, informed answers.

This project bridges the gap between **domain-specific knowledge** and LLM capabilities, making it perfect for applications like:

* AI-powered **semantic search engines**
* **Knowledge retrieval systems**
* RAG-based **question-answering solutions**
* Recommendations or agentic AI workflows

---

## 🎯 Problem Statement

While LLMs like GPT are excellent at understanding and generating text, they **cannot access proprietary or domain-specific information**. This limitation makes them less effective for specialized tasks, such as corporate knowledge retrieval or research-specific question answering.

**EndeeRAG solves this problem** by embedding documents into vectors, storing them in Endee, and performing **semantic similarity searches** before generating answers. This ensures that the LLM responds using **relevant, accurate, and up-to-date information**.

---

## 🏗️ System Architecture

The workflow of EndeeRAG can be summarized as follows:

1. **Document Embedding**
   Input documents are converted into numerical vectors using **SentenceTransformers**, capturing the semantic meaning of the text.

2. **Vector Storage in Endee**
   The embeddings are stored in **Endee**, which acts as the **semantic memory** of the system, enabling fast and scalable vector similarity searches.

3. **Query Embedding**
   User queries are also converted into vectors to match against the stored document embeddings.

4. **Semantic Retrieval**
   Endee searches for the most semantically relevant documents using **vector similarity**, rather than exact keyword matches.

5. **Answer Generation**
   The retrieved context is passed to an LLM, which generates precise and meaningful answers, creating a **RAG-powered knowledge pipeline**.

---

## 🔑 Role of Endee

Endee is the backbone of EndeeRAG. Its responsibilities include:

* Efficient **storage of high-dimensional embeddings**
* **Fast vector similarity search** for semantic relevance
* Supporting **RAG workflows**, semantic search, and recommendation engines
* Acting as the **bridge between raw documents and LLM intelligence**

In short, **without Endee, RAG wouldn’t be possible at scale**.

---

## ⚡ Features

* **Semantic Search:** Find documents based on meaning, not just keywords
* **RAG Integration:** LLMs generate answers using retrieved context
* **Domain Knowledge Friendly:** Works with private, specialized datasets
* **Scalable:** Handles large collections of documents efficiently
* **Extensible:** Can be adapted for recommendation engines or AI agents

---

## 🛠️ Installation & Setup

### Prerequisites

* **Python 3.10+**
* **Docker** (for running Endee)
* **Git** (for cloning the repo)

### Steps

1. **Clone the repository**

```powershell
git clone https://github.com/yourusername/EndeeRAG.git
cd EndeeRAG
```

2. **Start Endee using Docker Compose**

```powershell
docker-compose up
```

This will run the vector database locally at `localhost:6333`.

3. **Index your documents**

```powershell
py -m indexer.index_documents
```

<img width="1074" height="309" alt="image" src="https://github.com/user-attachments/assets/c97c64e5-da66-45a1-9543-821330974327" />


This converts your documents into embeddings and stores them in Endee.

4. **Run a semantic search**

```powershell
py -m indexer.search_documents
```

Enter a query when prompted (e.g., `"chocolate cake recipe"` or `"document indexing and semantic search"`).

---

<img width="1041" height="271" alt="image" src="https://github.com/user-attachments/assets/1ddad53c-1c1d-4c5e-a60d-b648bd66aee3" />
<img width="875" height="242" alt="image" src="https://github.com/user-attachments/assets/3ffc8ade-5d97-430b-b75c-87adc4fa38ee" />


## 🔍 Example Search

**Query:** `"document indexing and semantic search"`

**Results:**

```
0.7087 -> Semantic search retrieves documents based on meaning rather than exact keyword matching.
0.6807 -> Semantic search can be applied in legal document retrieval to improve accuracy.
0.6729 -> Document metadata can be used to filter search results efficiently in vector databases.
0.5988 -> Hybrid search combines semantic vectors and keyword indices for best results.
```

---

## 💻 Commands Summary

| Command                          | Purpose                              |
| -------------------------------- | ------------------------------------ |
| `docker-compose up`              | Start the Endee vector database      |
| `py -m indexer.index_documents`  | Embed and index documents into Endee |
| `py -m indexer.search_documents` | Perform semantic search queries      |

---

## 🧰 Technologies Used

* **Python 3.10+** – Main programming language
* **Endee** – Vector database for semantic embeddings
* **SentenceTransformers** – Text embeddings
* **Docker** – Containerized Endee setup
* **RAG workflows** – Combining retrieval with LLM generation
