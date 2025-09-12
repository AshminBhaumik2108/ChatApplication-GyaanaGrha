import os
from langchain_community.document_loaders import UnstructuredFileLoader, PyPDFLoader, CSVLoader, TextLoader  # updated import
from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.embeddings import get_embeddings
from backend.vectorstore import get_vectorstore
from backend import config

# Function to load documents from the knowledge base directory.....
def load_docs(kb_dir):
    docs = []
    # for the type of document.....
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
        # This Line will run in the Second....
        docs.extend(loader.load())
    return docs

# Main entry point of the function of this ingestion script, So that it can Run....
def main():
    # Loads all documents from your knowledge base directory. It gathers raw files from the texts of the PDFs or others etc....
    # from the ENV file....(KB_DIR).....
    # config.py : Have all the Values of the ENV files, with the Configurations...
    docs = load_docs(config.KB_DIR)
    # A text splitter object that breaks large docs into smaller chunks : Helps to breaks into step by step....
    splitter = RecursiveCharacterTextSplitter(chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)
    chunks = splitter.split_documents(docs) # Prepares the raw text for embedding & storage....
    # Initializes your Chroma vector database (from backend/vectorstore.py).....
    vs = get_vectorstore()
    # Extracts the raw text content from each chunk object.....
    # Extracts the metadata (like source filename, page number, etc.) for each chunk.......
    texts = [c.page_content for c in chunks]
    metadatas = [c.metadata for c in chunks]
    # Adds all chunk texts + metadata into ChromaDB.....
    vs.add_texts(texts, metadatas)
    # At the End just prints the length of the Chunks for the file.....
    print(f"Ingested {len(chunks)} chunks into Chroma.")

if __name__ == "__main__":
    main()
