from langchain_community.embeddings import HuggingFaceEmbeddings
from backend import config

# Model definition for the embeddings.....
def get_embeddings():
    # This Mini-LM model is used for generating embeddings from text (very fast and Responsive : Also Can Understand Semantic Sentences....)
    return HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
