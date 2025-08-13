import chromadb
from langchain.vectorstores import Chroma
from backend.embeddings import get_embeddings
from backend import config

def get_vectorstore():
    return Chroma(
        persist_directory=config.CHROMA_DIR,
        embedding_function=get_embeddings()
    )
