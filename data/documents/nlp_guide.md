# Natural Language Processing (NLP) Guide

## What is NLP?

Natural Language Processing is a field of AI that enables computers to understand, interpret, and generate human language. It bridges the gap between human communication and computer understanding.

## Text Preprocessing

### Tokenization

Breaking text into smaller units:
- **Word Tokenization**: Split by words
- **Sentence Tokenization**: Split by sentences
- **Subword Tokenization**: BPE, WordPiece, SentencePiece

### Text Normalization

- **Lowercasing**: Convert to lowercase
- **Stemming**: Reduce words to root form (running → run)
- **Lemmatization**: Dictionary-based normalization
- **Stop Word Removal**: Remove common words (the, is, at)
- **Punctuation Removal**

### Text Representation

1. **Bag of Words (BoW)**: Count word occurrences
2. **TF-IDF**: Term Frequency-Inverse Document Frequency
3. **Word Embeddings**: Dense vector representations

## Word Embeddings

### Word2Vec (2013)

Learn word vectors from context:
- **CBOW**: Predict word from context
- **Skip-gram**: Predict context from word

Properties:
- king - man + woman ≈ queen
- Similar words have similar vectors

### GloVe (2014)

Global Vectors for Word Representation:
- Uses word co-occurrence statistics
- Combines global and local context

### FastText

- Extends Word2Vec with subword information
- Handles out-of-vocabulary words
- Better for morphologically rich languages

## Language Models

### N-gram Models

Predict next word based on previous n-1 words:
- Bigram: P(word|previous_word)
- Trigram: P(word|previous_two_words)

### Neural Language Models

- RNN-based: LSTM, GRU
- Transformer-based: Modern state-of-the-art

## Transformer Models for NLP

### BERT (Bidirectional Encoder Representations)

- Pre-trained on masked language modeling
- Bidirectional context
- Great for understanding tasks

Variants:
- RoBERTa: Optimized training
- ALBERT: Parameter-efficient
- DistilBERT: Smaller, faster

### GPT (Generative Pre-trained Transformer)

- Autoregressive language model
- Great for text generation
- GPT-3, GPT-4, ChatGPT

### T5 (Text-to-Text Transfer Transformer)

- All tasks as text-to-text
- Unified framework

### LLaMA, Mistral, Gemini

- Modern open and closed source LLMs
- Competitive with GPT

## NLP Tasks

### Text Classification

- Sentiment Analysis: Positive/Negative/Neutral
- Topic Classification: Categorize documents
- Spam Detection

### Named Entity Recognition (NER)

Identify entities in text:
- Person, Organization, Location
- Date, Money, Percentage

### Part-of-Speech Tagging

Label words with grammatical tags:
- Noun, Verb, Adjective, Adverb, etc.

### Question Answering

- Extractive QA: Find answer span in text
- Generative QA: Generate answer
- Open-domain QA: Answer any question

### Machine Translation

- Neural Machine Translation (NMT)
- Sequence-to-sequence with attention
- mBART, mT5 for multilingual

### Text Summarization

- **Extractive**: Select important sentences
- **Abstractive**: Generate new summary text

### Text Generation

- Story generation
- Code generation (Copilot, CodeGen)
- Creative writing

## Evaluation Metrics

### Classification Metrics
- Accuracy, Precision, Recall, F1

### Generation Metrics
- **BLEU**: N-gram overlap (translation)
- **ROUGE**: Recall-oriented (summarization)
- **Perplexity**: Language model quality
- **BERTScore**: Semantic similarity

## Prompt Engineering

Designing effective prompts for LLMs:

- **Zero-shot**: No examples
- **Few-shot**: Provide examples
- **Chain-of-Thought**: Step-by-step reasoning
- **Role-playing**: Assign persona

## Fine-tuning Strategies

1. **Full Fine-tuning**: Update all parameters
2. **LoRA**: Low-rank adaptation
3. **QLoRA**: Quantized LoRA
4. **Prefix Tuning**: Learn continuous prompts
5. **Adapter Layers**: Add small trainable modules

## Retrieval-Augmented Generation (RAG)

Combine retrieval with generation:
1. Retrieve relevant documents
2. Use as context for generation
3. Reduces hallucination

## Applications

- Chatbots and Virtual Assistants
- Search Engines
- Content Moderation
- Legal Document Analysis
- Medical Text Mining
- Code Understanding
