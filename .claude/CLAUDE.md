# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Populate the ChromaDB vector database (run once before starting the agent)
python educosys_agent/add_vector_db.py

# Run the AI agent (Google ADK web interface)
adk web

# Run the Streamlit app (image generation/captioning)
streamlit run educourse_streamlit.py
```

## Environment

Requires a `.env` file in the project root:
```
GOOGLE_API_KEY=...
OPENAI_API_KEY=...
```

## Architecture

This project has two distinct entry points that operate independently:

1. **ADK Agent** (`educosys_agent/`) — A Google ADK agent (`root_agent` in `agent.py`) powered by `gemini-2.5-flash`. It exposes a single `retrieve_info` tool (a `FunctionTool` wrapping a RAG function) that queries a local ChromaDB vector store (`./chroma_genai/`) using OpenAI embeddings (`text-embedding-3-large`). The ADK framework discovers the agent via the `educosys_agent/` package. Run with `adk web`.

2. **Streamlit App** (`educourse_streamlit.py`) — A standalone UI for image generation (Gemini 2.0 Flash image generation model), image captioning (Gemini 2.0 Flash), and a YouTube summarizer placeholder. Uses `google.genai` client directly, not the ADK.

**RAG pipeline**: `add_vector_db.py` scrapes the Educosys GenAI course webpage using `WebBaseLoader`, splits with `RecursiveCharacterTextSplitter`, embeds with OpenAI, and persists to `./chroma_genai/`. The vector store must be populated before the agent can answer course-related questions. Note: the embedding/storage code in `add_vector_db.py` is currently commented out — only the loader runs.

**Key dependency**: The `chroma_genai/` directory (ChromaDB persistent storage) is generated locally and not committed to the repo.
