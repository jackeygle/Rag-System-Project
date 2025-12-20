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
RAG_PROMPT = """你是一个有帮助的AI助手。请根据以下提供的上下文来回答用户的问题。

规则：
1. 只根据提供的上下文来回答问题
2. 如果上下文中没有相关信息，请诚实地说"根据提供的文档，我没有找到相关信息"
3. 回答要准确、简洁、有条理
4. 如果适用，请引用信息来源

上下文：
{context}

用户问题：{question}

回答："""


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
        formatted.append(f"[文档 {i}] 来源: {source}\n{doc.page_content}")
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
