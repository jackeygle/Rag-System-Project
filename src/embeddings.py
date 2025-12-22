"""
Embeddings Module
Creates vector embeddings using Gemini
"""
from pathlib import Path
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import GOOGLE_API_KEY, EMBEDDING_MODEL


def get_embeddings() -> GoogleGenerativeAIEmbeddings:
    """Get the configured embedding model."""
    if not GOOGLE_API_KEY:
        raise ValueError(
            "❌ GOOGLE_API_KEY not found!\n"
            "Please set your API key in the .env file:\n"
            "GOOGLE_API_KEY=your_api_key_here\n"
            "Get your key from: https://aistudio.google.com/apikey"
        )
    
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY,
    )
