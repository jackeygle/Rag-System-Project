# RAG System

A Retrieval-Augmented Generation (RAG) document Q&A system powered by Groq LLM and Gemini Embeddings.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Edit `.env` file:

```bash
GOOGLE_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

Get keys from:
- Gemini: https://aistudio.google.com/apikey
- Groq: https://console.groq.com/keys

### 3. Add Documents

Place your PDF, TXT, or MD files in `data/documents/`

### 4. Index Documents

```bash
python main.py --index
```

### 5. Start Querying

```bash
# Interactive mode
python main.py

# Single query
python main.py --query "Your question here"
```

## Usage

| Command | Description |
|---------|-------------|
| `python main.py --index` | Index documents in `data/documents/` |
| `python main.py --index --url URL` | Index documents + web page |
| `python main.py` | Interactive query mode |
| `python main.py --query "question"` | Single query mode |

## Project Structure

```
ragsystem/
├── main.py              # CLI entry point
├── streamlit_app.py     # Web interface (Streamlit)
├── config.py            # Configuration
├── requirements.txt     # Dependencies
├── .env                 # API keys
├── src/
│   ├── document_loader.py  # Document loading (PDF/TXT/MD/Web)
│   ├── text_splitter.py    # Text chunking
│   ├── embeddings.py       # Gemini embeddings
│   ├── vector_store.py     # ChromaDB vector store
│   ├── retriever.py        # Similarity search
│   └── generator.py        # Groq LLM generation
├── data/documents/      # Document directory
└── db/chroma/           # Vector database
```

## Supported Formats

- PDF documents
- TXT text files
- Markdown files
- Web URLs

## Tech Stack

- **LLM**: Groq (Llama 3.3 70B)
- **Embeddings**: Google Gemini
- **Vector Store**: ChromaDB
- **Framework**: LangChain
- **Web UI**: Streamlit

## License

MIT
