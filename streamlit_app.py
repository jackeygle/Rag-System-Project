"""
RAG System - Streamlit Web Interface (Premium Dark Theme)
"""
import os
import sys
from pathlib import Path
from datetime import datetime

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
    initial_sidebar_state="expanded",
)

# Premium Dark Theme CSS
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Header */
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.3)); }
        to { filter: drop-shadow(0 0 30px rgba(118, 75, 162, 0.5)); }
    }
    
    .main-subtitle {
        color: rgba(255, 255, 255, 0.6);
        font-size: 1.1rem;
        font-weight: 300;
    }
    
    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    
    /* Status Card */
    .status-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .status-title {
        color: #fff;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .status-item {
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.9rem;
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .status-item:last-child {
        border-bottom: none;
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        background: #10b981;
        border-radius: 50%;
        display: inline-block;
        margin-right: 0.5rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Feature Cards */
    .feature-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 0.75rem;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(102, 126, 234, 0.5);
        transform: translateY(-2px);
    }
    
    .feature-icon {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-title {
        color: #fff;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.25rem;
    }
    
    .feature-desc {
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.75rem;
    }
    
    /* Chat Container */
    .chat-container {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        min-height: 400px;
        max-height: 500px;
        overflow-y: auto;
    }
    
    /* Chat Messages */
    .message {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
        animation: fadeIn 0.3s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .message-avatar {
        width: 40px;
        height: 40px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        flex-shrink: 0;
    }
    
    .user-avatar {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .bot-avatar {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    }
    
    .message-content {
        flex: 1;
    }
    
    .message-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.5rem;
    }
    
    .message-name {
        color: #fff;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    .message-time {
        color: rgba(255, 255, 255, 0.4);
        font-size: 0.75rem;
    }
    
    .message-bubble {
        padding: 1rem 1.25rem;
        border-radius: 16px;
        line-height: 1.6;
    }
    
    .user-bubble {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #fff;
        border-bottom-left-radius: 4px;
    }
    
    .bot-bubble {
        background: rgba(255, 255, 255, 0.08);
        color: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom-left-radius: 4px;
    }
    
    /* Example Buttons */
    .example-btn {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        color: rgba(255, 255, 255, 0.8);
        padding: 0.75rem 1rem;
        border-radius: 12px;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        text-align: left;
    }
    
    .example-btn:hover {
        background: rgba(102, 126, 234, 0.2);
        border-color: rgba(102, 126, 234, 0.5);
        color: #fff;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: rgba(255, 255, 255, 0.4);
        font-size: 0.85rem;
    }
    
    .footer-tech {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 0.5rem;
        flex-wrap: wrap;
    }
    
    .tech-badge {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.6);
    }
    
    /* Streamlit Widget Overrides */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        color: #fff !important;
        padding: 1rem !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border: none !important;
        border-radius: 12px !important;
        color: #fff !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(0, 0, 0, 0.3) !important;
        backdrop-filter: blur(10px);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: rgba(255, 255, 255, 0.8);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-color: #667eea !important;
    }
    
    /* Empty State */
    .empty-state {
        text-align: center;
        padding: 3rem;
        color: rgba(255, 255, 255, 0.4);
    }
    
    .empty-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }
    
    .empty-text {
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .empty-hint {
        font-size: 0.9rem;
        opacity: 0.7;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def init_rag():
    """Initialize RAG system (cached)."""
    google_key = os.getenv("GOOGLE_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")
    
    if not google_key:
        return None, "❌ Missing GOOGLE_API_KEY", 0
    if not groq_key:
        return None, "❌ Missing GROQ_API_KEY", 0
    
    try:
        from config import DATA_DIR
        from src.document_loader import load_all_documents
        from src.text_splitter import split_documents
        from src.vector_store import create_vector_store
        from src.retriever import create_retriever
        from src.generator import create_rag_chain
        
        docs = load_all_documents(directory=DATA_DIR)
        if not docs:
            return None, "❌ No documents found", 0
        
        chunks = split_documents(docs)
        vs = create_vector_store(chunks)
        retriever = create_retriever(vs)
        chain = create_rag_chain(retriever)
        
        return chain, "✅ System Online", len(chunks)
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return None, f"❌ Error: {str(e)[:50]}", 0


def render_message(role: str, content: str, timestamp: str = None):
    """Render a chat message with modern styling."""
    if timestamp is None:
        timestamp = datetime.now().strftime("%H:%M")
    
    if role == "user":
        st.markdown(f"""
        <div class="message">
            <div class="message-avatar user-avatar">👤</div>
            <div class="message-content">
                <div class="message-header">
                    <span class="message-name">You</span>
                    <span class="message-time">{timestamp}</span>
                </div>
                <div class="message-bubble user-bubble">{content}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="message">
            <div class="message-avatar bot-avatar">🤖</div>
            <div class="message-content">
                <div class="message-header">
                    <span class="message-name">AI Assistant</span>
                    <span class="message-time">{timestamp}</span>
                </div>
                <div class="message-bubble bot-bubble">{content}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def main():
    # Initialize RAG
    rag_chain, status, chunk_count = init_rag()
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
        <div class="status-card">
            <div class="status-title">🔧 System Status</div>
            <div class="status-item"><span class="status-dot"></span>""" + status + """</div>
            <div class="status-item">📊 """ + str(chunk_count) + """ document chunks</div>
            <div class="status-item">🤖 Llama 3.3 70B</div>
            <div class="status-item">🔍 Gemini Embeddings</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">📄</div>
                <div class="feature-title">Smart Retrieval</div>
                <div class="feature-desc">Semantic document search</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">Fast Response</div>
                <div class="feature-desc">Powered by Groq</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🧠</div>
                <div class="feature-title">Context Aware</div>
                <div class="feature-desc">Multi-document synthesis</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    # Main Header
    st.markdown("""
    <div class="main-header">
        <div class="main-title">🤖 RAG Document Assistant</div>
        <div class="main-subtitle">AI-powered document Q&A with Retrieval-Augmented Generation</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat Container
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    if not st.session_state.messages:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">💬</div>
            <div class="empty-text">Start a conversation</div>
            <div class="empty-hint">Ask questions about your documents below</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in st.session_state.messages:
            render_message(msg["role"], msg["content"], msg.get("time"))
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Example Questions
    st.markdown("#### 💡 Try asking:", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("What is machine learning?", use_container_width=True, key="ex1"):
            st.session_state.pending_question = "What is machine learning?"
    with col2:
        if st.button("What are RAG advantages?", use_container_width=True, key="ex2"):
            st.session_state.pending_question = "What are the advantages of RAG?"
    with col3:
        if st.button("How does NLP work?", use_container_width=True, key="ex3"):
            st.session_state.pending_question = "How does natural language processing work?"
    
    # Chat Input
    st.markdown("<br>", unsafe_allow_html=True)
    question = st.chat_input("💬 Ask anything about your documents...")
    
    # Handle pending question from button
    if "pending_question" in st.session_state:
        question = st.session_state.pending_question
        del st.session_state.pending_question
    
    if question:
        current_time = datetime.now().strftime("%H:%M")
        st.session_state.messages.append({
            "role": "user", 
            "content": question,
            "time": current_time
        })
        
        if rag_chain:
            with st.spinner("🔍 Searching documents..."):
                try:
                    from src.generator import query
                    answer = query(rag_chain, question)
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": answer,
                        "time": datetime.now().strftime("%H:%M")
                    })
                except Exception as e:
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": f"❌ Error: {e}",
                        "time": datetime.now().strftime("%H:%M")
                    })
        else:
            st.session_state.messages.append({
                "role": "assistant", 
                "content": "⚠️ System not initialized. Please check API configuration.",
                "time": datetime.now().strftime("%H:%M")
            })
        
        st.rerun()
    
    # Footer
    st.markdown("""
    <div class="footer">
        <div>Built with ❤️ for intelligent document understanding</div>
        <div class="footer-tech">
            <span class="tech-badge">LangChain</span>
            <span class="tech-badge">Groq</span>
            <span class="tech-badge">ChromaDB</span>
            <span class="tech-badge">Gemini</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
