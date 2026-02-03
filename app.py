from rag.rag_pipeline import RAGPipeline

def main():
    rag = RAGPipeline()


    while True:
        query = input("Ask a question (or 'exit'): ")
        if query.lower() == "exit":
            break



        print()
        print(rag.answer(query))
        print()

if __name__ == "__main__":
    main()
