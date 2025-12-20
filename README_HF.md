---
title: RAG 文档问答系统
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
license: mit
---

# RAG 文档问答系统

基于检索增强生成 (RAG) 的智能文档问答系统。

## 功能

- 📄 支持 PDF、TXT、Markdown 文档
- 🔍 智能检索相关内容
- 🤖 使用 Groq LLM 生成回答
- 🌐 Web 界面交互

## 配置

在 Settings > Secrets 中添加：
- `GROQ_API_KEY`: 你的 Groq API 密钥
- `GOOGLE_API_KEY`: 你的 Gemini API 密钥（用于 Embeddings）
