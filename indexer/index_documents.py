import requests
from embeddings.embedder import Embedder

ENDEE_URL = "http://localhost:6333"

COLLECTION = "documents_index"
VECTOR_SIZE = 384


def create_collection():
    payload = {
        "vectors": {
            "size": VECTOR_SIZE,
            "distance": "Cosine"
        }
    }

    requests.put(
        f"{ENDEE_URL}/collections/{COLLECTION}",
        json=payload
    )


    print("Collection ready")


def load_documents():
    with open("data/documents.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def main():
    create_collection()


    embedder = Embedder()
    docs = load_documents()

    print(f"Loaded {len(docs)} documents")

    vectors = embedder.encode(docs)

    points = [
        {
            "id": i,
            "vector": vectors[i],
            "payload": {"text": text}
        }
        for i, text in enumerate(docs)
    ]


    r = requests.put(
        f"{ENDEE_URL}/collections/{COLLECTION}/points?wait=true",
        json={"points": points}
    )

    r.raise_for_status()


    print("Documents indexed successfully")


if __name__ == "__main__":
    main()
