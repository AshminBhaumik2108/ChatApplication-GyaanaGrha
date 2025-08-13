import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "models/gemini-1.5-flash")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
CHROMA_DIR = os.getenv("CHROMA_DIR", "data/chroma")
KB_DIR = os.getenv("KB_DIR", "data/knowledge_base")
RETRIEVE_K = int(os.getenv("RETRIEVE_K", 4))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.5))
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 800))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 120))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1024))
