"""
RAG System - Streamlit Web Interface
"""
import os
import sys
from pathlib import Path

import streamlit as st

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv
load_dotenv()

# Page config
st.set_page_config(
    page_title="RAG Document Assistant",
    page_icon="🤖",
    layout="wide",
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .status-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
    }
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .bot-message {
        background: #f0f0f0;
        border: 1px solid #ddd;
    }
    .feature-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def init_rag():
    """Initialize RAG system (cached)."""
    google_key = os.getenv("GOOGLE_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")
    
    if not google_key:
        return None, "❌ Missing GOOGLE_API_KEY"
    if not groq_key:
        return None, "❌ Missing GROQ_API_KEY"
    
    try:
        from config import DATA_DIR
        from src.document_loader import load_all_documents
        from src.text_splitter import split_documents
        from src.vector_store import create_vector_store
        from src.retriever import create_retriever
        from src.generator import create_rag_chain
        
        docs = load_all_documents(directory=DATA_DIR)
        if not docs:
            return None, "❌ No documents found"
        
        chunks = split_documents(docs)
        vs = create_vector_store(chunks)
        retriever = create_retriever(vs)
        chain = create_rag_chain(retriever)
        
        return chain, f"✅ Loaded {len(chunks)} document chunks"
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return None, f"❌ Error: {str(e)[:100]}"


def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 RAG Document Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">AI-powered document Q&A using Retrieval-Augmented Generation</p>', unsafe_allow_html=True)
    
    # Initialize RAG
    rag_chain, status = init_rag()
    
    # Layout
    col1, col2 = st.columns([3, 1])
    
    with col2:
        # Status box
        st.markdown(f"""
        <div class="status-box">
            <h4>🔧 System Status</h4>
            <p>{status}</p>
            <p>🤖 Model: Llama 3.3 70B</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature cards
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 24px;">📄</div>
            <div><b>Smart Retrieval</b></div>
            <div style="color: #888; font-size: 0.8rem;">Find relevant content</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 24px;">⚡</div>
            <div><b>Fast Response</b></div>
            <div style="color: #888; font-size: 0.8rem;">Powered by Groq</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col1:
        # Chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        # Display chat history
        for msg in st.session_state.messages:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                st.markdown(f'<div class="chat-message user-message">👤 {content}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message bot-message">🤖 {content}</div>', unsafe_allow_html=True)
        
        # Chat input
        st.markdown("---")
        
        # Example buttons
        col_ex1, col_ex2, col_ex3 = st.columns(3)
        with col_ex1:
            if st.button("What is machine learning?", use_container_width=True):
                st.session_state.pending_question = "What is machine learning?"
        with col_ex2:
            if st.button("What are RAG advantages?", use_container_width=True):
                st.session_state.pending_question = "What are the advantages of RAG?"
        with col_ex3:
            if st.button("How does gradient descent work?", use_container_width=True):
                st.session_state.pending_question = "How does gradient descent work?"
        
        # Text input
        question = st.chat_input("💬 Enter your question...")
        
        # Handle pending question from button
        if "pending_question" in st.session_state:
            question = st.session_state.pending_question
            del st.session_state.pending_question
        
        if question:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": question})
            
            # Generate response
            if rag_chain:
                with st.spinner("🔍 Searching documents..."):
                    try:
                        from src.generator import query
                        answer = query(rag_chain, question)
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                    except Exception as e:
                        st.session_state.messages.append({"role": "assistant", "content": f"❌ Error: {e}"})
            else:
                st.session_state.messages.append({"role": "assistant", "content": "⚠️ System not initialized"})
            
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown('<p style="text-align: center; color: #888;">Powered by LangChain + Groq + ChromaDB | Made with ❤️</p>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
