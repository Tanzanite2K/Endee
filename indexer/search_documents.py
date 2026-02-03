from retriever.semantic_search import SemanticSearcher

if __name__ == "__main__":
    s = SemanticSearcher()
    query = input("Enter search query: ")
    results = s.search(query, top_k=5)


    print("\nTop results:")
    for i, r in enumerate(results, start=1):
        print(f"{i}. {r}")
