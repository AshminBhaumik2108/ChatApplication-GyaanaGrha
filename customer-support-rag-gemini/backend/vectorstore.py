# Monkey-patch sqlite3 to use pysqlite3 if available (for ChromaDB compatibility)
try:
    import pysqlite3
    import sys
    sys.modules["sqlite3"] = pysqlite3
except ImportError:
    pass

import chromadb
from langchain.vectorstores import Chroma
from backend.embeddings import get_embeddings
from backend import config

def get_vectorstore():
    return Chroma(
        persist_directory=config.CHROMA_DIR,
        embedding_function=get_embeddings()
    )
