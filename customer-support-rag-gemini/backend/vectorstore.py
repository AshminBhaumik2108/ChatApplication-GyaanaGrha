# Monkey-patch sqlite3 to use pysqlite3 for ChromaDB compatibility (SQLite >= 3.35.0)
import sys
try:
    import pysqlite3
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass

import chromadb
from langchain_community.vectorstores import Chroma
from backend.embeddings import get_embeddings
from backend import config

def get_vectorstore():
    return Chroma(
        persist_directory=config.CHROMA_DIR,
        embedding_function=get_embeddings()
    )
