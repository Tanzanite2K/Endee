import requests
from embeddings.embedder import Embedder

ENDEE_URL = "http://localhost:6333"
COLLECTION = "documents_index"



class SemanticSearcher:
    def __init__(self):
        self.embedder = Embedder()

    def search(self, query, top_k=3):
        vector = self.embedder.encode([query])[0]


        r = requests.post(
            f"{ENDEE_URL}/collections/{COLLECTION}/points/search",
            json={
                "vector": vector,
                "limit": top_k,
                "with_payload": True  
            }
        )

        r.raise_for_status()
        results = r.json()["result"]



        for hit in results:
            text = hit.get("payload", {}).get("text", "<no text>")
            score = hit.get("score", 0)
            print(f"{score:.4f} -> {text}")


        return [hit.get("payload", {}).get("text", "<no text>") for hit in results]
