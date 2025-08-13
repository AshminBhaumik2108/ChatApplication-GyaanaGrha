from backend.vectorstore import get_retriever

def test_retrieval():
    retriever = get_retriever()
    docs = retriever.get_relevant_documents("refund")
    assert len(docs) > 0, "Retriever should return docs for 'refund'"

if __name__ == "__main__":
    test_retrieval()
    print("Retrieval test passed.")
