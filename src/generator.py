"""
Generator Module
Uses Groq LLM to generate responses based on retrieved context
"""
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever

import sys
sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
from config import GROQ_API_KEY, LLM_MODEL


# RAG Prompt Template
RAG_PROMPT = """You are a helpful AI assistant. Please answer the user's question based on the provided context.

Rules:
1. Only answer based on the provided context
2. If the context doesn't contain relevant information, honestly say "I couldn't find relevant information in the provided documents"
3. Be accurate, concise, and well-organized
4. Cite sources when applicable

Context:
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
        temperature=0.3,  # Lower temperature for more factual responses
    )


def format_docs(docs) -> str:
    """Format retrieved documents into a single context string."""
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


def query(chain, question: str) -> str:
    """Execute a query and return the response."""
    return chain.invoke(question)
