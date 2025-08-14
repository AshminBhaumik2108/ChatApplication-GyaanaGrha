from langchain_community.embeddings import HuggingFaceEmbeddings  # updated import
from backend import config

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
