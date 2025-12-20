"""
Vector Store Module
Manages ChromaDB for storing and retrieving document embeddings
"""
from typing import List, Optional
from pathlib import Path
from langchain_core.documents import Document
from langchain_chroma import Chroma

import sys
sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
from config import DB_DIR, COLLECTION_NAME
from src.embeddings import get_embeddings


def create_vector_store(documents: List[Document]) -> Chroma:
    """Create a new vector store from documents."""
    if not documents:
        raise ValueError("No documents provided to create vector store")
    
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
    collection = vector_store._collection
    count = collection.count()
    
    if count == 0:
        print("⚠️  Vector store is empty")
        return None
    
    print(f"✅ Loaded vector store with {count} chunks")
    return vector_store


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
