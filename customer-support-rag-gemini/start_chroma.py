import chromadb
from chromadb.config import Settings  # Configuration Settings for ChromaDB....

# Configuration Settings : To tell ChromaDB where to Store the Vector Data....
client = chromadb.Client(Settings(
    persist_directory="data/chroma", # To tell the client where to store the data....
    chroma_db_impl="duckdb+parquet",
))

print("ChromaDB started with persistence at data/chroma by AshminBhaumik....")
# Now we can use `client` to add/query embeddings here
