# Educosys GenAI Agent Demo

An AI-powered assistant built with Google ADK (Agent Development Kit) that provides information about Educosys GenAI courses using RAG (Retrieval-Augmented Generation) capabilities.

## Features

- 🤖 **RAG-powered Chatbot** - Intelligent assistant that retrieves and answers questions about Educosys GenAI courses
- 🖼️ **Image Generator** - Generate images using Gemini 2.0 Flash
- 📝 **Image Caption Generator** - Upload images and get AI-generated captions
- 🎥 **YouTube Video Summarizer** - Summarize YouTube videos (placeholder for future implementation)

## Tech Stack

- **Google ADK** - Agent Development Kit for building AI agents
- **Gemini 2.5 Flash** - Google's latest LLM for agent reasoning
- **LangChain** - For document loading and text splitting
- **ChromaDB** - Vector database for storing embeddings
- **OpenAI Embeddings** - For generating text embeddings
- **Streamlit** - Web UI for image and video features

## Prerequisites

- Python 3.10+
- Google API Key (for Gemini models)
- OpenAI API Key (for embeddings)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Agent-ai-Demo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Setup

Create a `.env` file in the root directory with your API keys:

```env
GOOGLE_API_KEY=your_google_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### 1. Populate the Vector Database

First, run the script to load course data into ChromaDB:

```bash
python educosys_agent/add_vector_db.py
```

This will scrape the [Educosys GenAI Course](https://www.educosys.com/course/genai) page and store the content in the vector database.

### 2. Run the AI Agent

Start the agent using Google ADK CLI:

```bash
adk web
```

This will launch the agent interface where you can ask questions about the Educosys GenAI course.

### 3. Run the Streamlit App

For image generation and caption features:

```bash
streamlit run educourse_streamlit.py
```

## Project Structure

```
Agent-ai-Demo/
├── educosys_agent/
│   ├── __init__.py
│   ├── agent.py           # Main agent definition with RAG tool
│   └── add_vector_db.py   # Script to populate vector database
├── educourse_streamlit.py  # Streamlit app for image features
├── requirements.txt        # Python dependencies
├── chroma_genai/          # ChromaDB persistent storage (generated)
└── README.md              # This file
```

## How It Works

1. **Data Ingestion**: The `add_vector_db.py` script loads content from the Educosys course webpage, splits it into chunks, and stores embeddings in ChromaDB.

2. **Query Processing**: When a user asks a question, the agent uses the `retrieve_info` tool to search the vector database for relevant information.

3. **Response Generation**: The Gemini 2.5 Flash model uses the retrieved context to generate accurate, informative responses.

## License

MIT License
