from retriever.semantic_search import SemanticSearcher

s = SemanticSearcher()

query = "your sample query here"
results = s.search(query, top_k=3)


print("Search results:")
for r in results:
    print("-", r)
