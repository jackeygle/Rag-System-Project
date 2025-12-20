"""
RAG System Configuration
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data" / "documents"
DB_DIR = BASE_DIR / "db" / "chroma"

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_DIR.mkdir(parents=True, exist_ok=True)

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Model Configuration
EMBEDDING_MODEL = "models/text-embedding-004"  # Gemini embedding model

# LLM Configuration (using Groq for faster response)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "llama-3.3-70b-versatile"  # Groq LLM model

# Text Splitting Configuration
CHUNK_SIZE = 1000  # Characters per chunk
CHUNK_OVERLAP = 200  # Overlap between chunks

# Retrieval Configuration
TOP_K = 4  # Number of documents to retrieve

# Vector Store Configuration
COLLECTION_NAME = "rag_documents"
