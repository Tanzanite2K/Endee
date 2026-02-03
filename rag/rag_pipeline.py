from retriever.semantic_search import SemanticSearcher

class RAGPipeline:
    def __init__(self):
        self.searcher = SemanticSearcher()


    def answer(self, query):
        docs = self.searcher.search(query)

        if not docs:
            return "No relevant documents found."


        response = "Answer based on retrieved knowledge:\n\n"
        for i, doc in enumerate(docs, 1):
            response += f"{i}. {doc}\n"

        return response
