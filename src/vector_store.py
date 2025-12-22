"""
Vector Store Module
Manages ChromaDB for storing and retrieving document embeddings
"""
import shutil
from typing import List, Optional
from pathlib import Path
from langchain_core.documents import Document
from langchain_chroma import Chroma

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import DB_DIR, COLLECTION_NAME
from src.embeddings import get_embeddings


def clear_vector_store() -> bool:
    """Clear the existing vector store to prevent duplicates on re-indexing.
    
    Returns:
        bool: True if cleared successfully, False otherwise
    """
    try:
        if DB_DIR.exists():
            shutil.rmtree(DB_DIR)
            DB_DIR.mkdir(parents=True, exist_ok=True)
            print("🗑️  Cleared existing vector store")
            return True
        return True
    except Exception as e:
        print(f"⚠️  Warning: Could not clear vector store: {e}")
        return False


def create_vector_store(documents: List[Document], clear_existing: bool = True) -> Chroma:
    """Create a new vector store from documents.
    
    Args:
        documents: List of documents to index
        clear_existing: If True, clear existing data before indexing (prevents duplicates)
    """
    if not documents:
        raise ValueError("No documents provided to create vector store")
    
    # Clear existing to prevent duplicates
    if clear_existing:
        clear_vector_store()
    
    print(f"🔄 Creating vector store with {len(documents)} chunks...")
    
    embeddings = get_embeddings()
    
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=str(DB_DIR),
    )
    
    print(f"✅ Vector store created and saved to {DB_DIR}")
    return vector_store


def load_vector_store() -> Optional[Chroma]:
    """Load an existing vector store."""
    if not DB_DIR.exists() or not any(DB_DIR.iterdir()):
        print("⚠️  No existing vector store found")
        return None
    
    print("📂 Loading existing vector store...")
    
    embeddings = get_embeddings()
    
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(DB_DIR),
    )
    
    # Check if collection has documents
    try:
        collection = vector_store._collection
        count = collection.count()
        
        if count == 0:
            print("⚠️  Vector store is empty")
            return None
        
        print(f"✅ Loaded vector store with {count} chunks")
        return vector_store
    except Exception as e:
        print(f"⚠️  Error accessing vector store: {e}")
        return None


def get_or_create_vector_store(documents: Optional[List[Document]] = None) -> Chroma:
    """Get existing vector store or create new one if documents provided."""
    existing_store = load_vector_store()
    
    if existing_store is not None:
        return existing_store
    
    if documents is None:
        raise ValueError(
            "No existing vector store found and no documents provided.\n"
            "Please add documents to the data/documents/ directory and run with --index flag."
        )
    
    return create_vector_store(documents)

