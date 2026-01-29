import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# MODELOS Y APIS
# ==========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ==========================
# CHROMA
# ==========================
CHROMA_PERSIST_DIR = "chromadb"

# ==========================
# EMBEDDINGS
# ==========================
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
