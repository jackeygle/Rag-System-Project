"""
Text Splitter Module
Splits documents into smaller chunks for embedding
"""
from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

import sys
sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
from config import CHUNK_SIZE, CHUNK_OVERLAP


def create_text_splitter() -> RecursiveCharacterTextSplitter:
    """Create a text splitter with configured parameters."""
    return RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", "。", ".", " ", ""],
    )


def split_documents(documents: List[Document]) -> List[Document]:
    """Split documents into smaller chunks."""
    if not documents:
        print("⚠️  No documents to split")
        return []
    
    splitter = create_text_splitter()
    chunks = splitter.split_documents(documents)
    
    print(f"📄 Split {len(documents)} document(s) into {len(chunks)} chunk(s)")
    return chunks
