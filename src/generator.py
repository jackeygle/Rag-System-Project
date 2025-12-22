"""
Generator Module
Uses Groq LLM to generate responses based on retrieved context
Falls back to general knowledge when no relevant documents found
"""
import time
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import GROQ_API_KEY, LLM_MODEL


# RAG Prompt Template - with fallback to general knowledge
RAG_PROMPT = """You are a helpful AI assistant. Answer the user's question based on the provided context when relevant.

Rules:
1. If the context contains relevant information, use it to answer and cite sources
2. If the context is NOT relevant to the question, use your general knowledge to provide a helpful answer
3. Be accurate, concise, and well-organized
4. When using context, mention "According to the documents..."
5. When using general knowledge, just answer directly without mentioning documents

Context from documents:
{context}

User Question: {question}

Answer:"""


def get_llm() -> ChatGroq:
    """Get the configured LLM (Groq)."""
    if not GROQ_API_KEY:
        raise ValueError(
            "❌ GROQ_API_KEY not found!\n"
            "Please set your API key in the .env file:\n"
            "GROQ_API_KEY=your_api_key_here\n"
            "Get your key from: https://console.groq.com/keys"
        )
    
    return ChatGroq(
        model=LLM_MODEL,
        api_key=GROQ_API_KEY,
        temperature=0.3,
    )


def format_docs(docs) -> str:
    """Format retrieved documents into a single context string."""
    if not docs:
        return "No relevant documents found."
    
    formatted = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("file_name", doc.metadata.get("source", "Unknown"))
        formatted.append(f"[Document {i}] Source: {source}\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted)


def create_rag_chain(retriever: VectorStoreRetriever):
    """Create the complete RAG chain."""
    prompt = ChatPromptTemplate.from_template(RAG_PROMPT)
    llm = get_llm()
    
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain


def query(chain, question: str, max_retries: int = 3) -> str:
    """Execute a query with retry logic for transient failures.
    
    Args:
        chain: The RAG chain to execute
        question: The user's question
        max_retries: Maximum number of retry attempts
        
    Returns:
        The generated response
    """
    last_error = None
    
    for attempt in range(max_retries):
        try:
            return chain.invoke(question)
        except Exception as e:
            last_error = e
            error_str = str(e).lower()
            
            # Check for non-retryable errors
            if "api_key" in error_str or "authentication" in error_str:
                raise ValueError(
                    "❌ API authentication failed. Please check your GROQ_API_KEY."
                ) from e
            
            if "rate_limit" in error_str or "429" in str(e):
                # Rate limited - wait longer before retry
                wait_time = (attempt + 1) * 2
                print(f"⚠️  Rate limited, waiting {wait_time}s before retry...")
                time.sleep(wait_time)
            elif attempt < max_retries - 1:
                # Other transient errors - brief wait
                time.sleep(0.5)
    
    # All retries failed
    raise RuntimeError(
        f"❌ Query failed after {max_retries} attempts. Last error: {last_error}"
    )

