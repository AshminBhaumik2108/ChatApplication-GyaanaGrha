import os
from langchain_community.document_loaders import UnstructuredFileLoader, PyPDFLoader, CSVLoader, TextLoader  # updated import
from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.embeddings import get_embeddings
from backend.vectorstore import get_vectorstore
from backend import config

def load_docs(kb_dir):
    docs = []
    for fname in os.listdir(kb_dir):
        fpath = os.path.join(kb_dir, fname)
        if fname.endswith(".pdf"):
            loader = PyPDFLoader(fpath)
        elif fname.endswith(".csv"):
            loader = CSVLoader(fpath)
        elif fname.endswith(".txt"):
            loader = TextLoader(fpath)
        elif fname.endswith(".md"):
            loader = UnstructuredFileLoader(fpath)
        else:
            continue
        docs.extend(loader.load())
    return docs

def main():
    docs = load_docs(config.KB_DIR)
    splitter = RecursiveCharacterTextSplitter(chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)
    chunks = splitter.split_documents(docs)
    vs = get_vectorstore()
    texts = [c.page_content for c in chunks]
    metadatas = [c.metadata for c in chunks]
    vs.add_texts(texts, metadatas)
    print(f"Ingested {len(chunks)} chunks into Chroma.")

if __name__ == "__main__":
    main()
