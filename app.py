#!/usr/bin/env python3
"""
RAG System - Gradio Web Interface (Simplified for HF Spaces)
"""
import os
import sys
import gradio as gr
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv
load_dotenv()

from config import DATA_DIR, GROQ_API_KEY
from src.document_loader import load_all_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import create_retriever
from src.generator import create_rag_chain, query

# Global variables
rag_chain = None
init_status = "⏳ 正在初始化..."


def initialize_rag():
    """Initialize the RAG system on startup."""
    global rag_chain, init_status
    
    from config import GOOGLE_API_KEY, GROQ_API_KEY
    
    if not GOOGLE_API_KEY:
        init_status = "❌ 缺少 GOOGLE_API_KEY"
        print(init_status)
        return False
    
    if not GROQ_API_KEY:
        init_status = "❌ 缺少 GROQ_API_KEY"
        print(init_status)
        return False
    
    print("✅ API Keys 已配置")
    
    try:
        print("📄 正在加载文档...")
        documents = load_all_documents(directory=DATA_DIR)
        
        if not documents:
            init_status = "❌ 没有找到文档"
            print(init_status)
            return False
        
        print(f"✅ 加载了 {len(documents)} 个文档")
        
        chunks = split_documents(documents)
        print(f"✅ 切分为 {len(chunks)} 个块")
        
        vector_store = create_vector_store(chunks)
        print("✅ 向量数据库创建成功")
        
        retriever = create_retriever(vector_store)
        rag_chain = create_rag_chain(retriever)
        
        init_status = f"✅ 已加载 {len(chunks)} 个文档块"
        print("✅ RAG 系统初始化成功!")
        return True
        
    except Exception as e:
        import traceback
        init_status = f"❌ 错误: {str(e)[:50]}"
        print(f"❌ 初始化错误: {e}")
        traceback.print_exc()
        return False


def respond(message, history):
    """Handle chat messages."""
    global rag_chain
    
    if not message.strip():
        return history
    
    if rag_chain is None:
        history.append([message, "⚠️ 系统未初始化，请检查 API Key 配置"])
        return history
    
    try:
        response = query(rag_chain, message)
        history.append([message, response])
    except Exception as e:
        history.append([message, f"❌ 错误: {str(e)}"])
    
    return history


# Initialize on startup
print("🚀 正在初始化 RAG 系统...")
initialize_rag()

# Create simple Gradio interface
with gr.Blocks(
    title="RAG 智能文档助手",
    theme=gr.themes.Soft(primary_hue="violet"),
) as demo:
    
    gr.Markdown("""
    # 🤖 RAG 智能文档助手
    基于检索增强生成技术，从文档中精准回答问题
    """)
    
    gr.Markdown(f"**状态**: {init_status}")
    
    chatbot = gr.Chatbot(height=450, label="对话")
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="💬 输入问题，按 Enter 发送...",
            show_label=False,
            scale=9,
        )
        send = gr.Button("发送", scale=1, variant="primary")
    
    with gr.Row():
        gr.Button("什么是机器学习？").click(
            lambda h: respond("什么是机器学习？", h), [chatbot], [chatbot]
        )
        gr.Button("RAG 的优势是什么？").click(
            lambda h: respond("RAG 的优势是什么？", h), [chatbot], [chatbot]
        )
        gr.Button("梯度下降如何工作？").click(
            lambda h: respond("梯度下降如何工作？", h), [chatbot], [chatbot]
        )
    
    gr.Markdown("---\n*Powered by LangChain + Groq + ChromaDB*")
    
    msg.submit(respond, [msg, chatbot], [chatbot]).then(lambda: "", None, [msg])
    send.click(respond, [msg, chatbot], [chatbot]).then(lambda: "", None, [msg])


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
