# RAG System

基于 Gemini API 的检索增强生成系统。

## 快速开始

### 1. 安装依赖

```bash
cd /Users/xinle/ragsystem
pip install -r requirements.txt
```

### 2. 配置 API Key

编辑 `.env` 文件，填入你的 Gemini API Key：

```bash
GOOGLE_API_KEY=你的API密钥
```

获取密钥：https://aistudio.google.com/apikey

### 3. 添加文档

将你的文档（PDF、TXT、MD）放入 `data/documents/` 目录。

### 4. 索引文档

```bash
python main.py --index
```

### 5. 开始查询

```bash
python main.py
```

## 使用方法

| 命令 | 说明 |
|------|------|
| `python main.py --index` | 索引 `data/documents/` 中的文档 |
| `python main.py --index --url URL` | 索引文档 + 网页 |
| `python main.py` | 交互式查询模式 |
| `python main.py --query "问题"` | 单次查询模式 |

## 项目结构

```
ragsystem/
├── main.py              # 主程序
├── config.py            # 配置文件
├── requirements.txt     # 依赖
├── .env                 # API 密钥
├── src/
│   ├── document_loader.py  # 文档加载
│   ├── text_splitter.py    # 文本切分
│   ├── embeddings.py       # 向量嵌入
│   ├── vector_store.py     # 向量存储
│   ├── retriever.py        # 检索器
│   └── generator.py        # 生成器
├── data/documents/      # 文档目录
└── db/chroma/           # 向量数据库
```

## 支持格式

- PDF 文档
- TXT 文本文件
- Markdown 文件
- 网页 URL
