import os
from dotenv import load_dotenv

# Load .env file locally (Streamlit Cloud ignores this, so safe to keep)
load_dotenv()

# Helper function to safely get environment variables with type casting
def get_env(var_name, default=None, cast_type=str):
    value = os.getenv(var_name, default)
    try:
        return cast_type(value) if value is not None else default
    except (ValueError, TypeError):
        print(f"Warning: Could not cast {var_name}='{value}' to {cast_type}. Using default={default}")
        return default

# API & model configurations
GOOGLE_API_KEY = get_env("GOOGLE_API_KEY", "")
GEMINI_MODEL = get_env("GEMINI_MODEL", "models/gemini-1.5-flash")
EMBEDDING_MODEL = get_env("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

# Data directories (make absolute to avoid path issues)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "chroma"))
KB_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "knowledge_base"))

# Ensure directories exist...
print("CHROMA_DIR:", CHROMA_DIR)
print("Exists:", os.path.exists(CHROMA_DIR))

# Retrieval & LLM settings
RETRIEVE_K = get_env("RETRIEVE_K", 4, int)
TEMPERATURE = get_env("TEMPERATURE", 0.5, float)
CHUNK_SIZE = get_env("CHUNK_SIZE", 800, int)
CHUNK_OVERLAP = get_env("CHUNK_OVERLAP", 120, int)
MAX_TOKENS = get_env("MAX_TOKENS", 1024, int)

# Debug output (optional, useful for deployment)
# print("Loaded Environment Variables:")
# print(f"GOOGLE_API_KEY: {'SET' if GOOGLE_API_KEY else 'NOT SET'}")
# print(f"GEMINI_MODEL: {GEMINI_MODEL}")
# print(f"EMBEDDING_MODEL: {EMBEDDING_MODEL}")
# print(f"CHROMA_DIR: {CHROMA_DIR}")
# print(f"KB_DIR: {KB_DIR}")
# print(f"RETRIEVE_K: {RETRIEVE_K}, TEMPERATURE: {TEMPERATURE}")
# print(f"CHUNK_SIZE: {CHUNK_SIZE}, CHUNK_OVERLAP: {CHUNK_OVERLAP}, MAX_TOKENS: {MAX_TOKENS}")
