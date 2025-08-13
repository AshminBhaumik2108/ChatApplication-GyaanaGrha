from langchain.embeddings import HuggingFaceEmbeddings
from backend import config

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
