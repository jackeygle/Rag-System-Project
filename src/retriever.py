"""
Retriever Module
Retrieves relevant documents from vector store
"""
from pathlib import Path
from langchain_chroma import Chroma
from langchain_core.vectorstores import VectorStoreRetriever

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import TOP_K


def create_retriever(vector_store: Chroma, k: int = None) -> VectorStoreRetriever:
    """Create a retriever from the vector store."""
    if k is None:
        k = TOP_K
    
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    
    return retriever
