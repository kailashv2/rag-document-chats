# RAG Document Chat 📄

> Upload any PDF and chat with it using AI. 

## What it does
- Upload any PDF
- Ask questions in natural language
- Get accurate AI answers instantly
- Clean browser UI — no terminal needed

## Tech Stack
- **Frontend:** HTML/CSS/JS
- **Backend:** FastAPI (Python)
- **Embeddings:** HuggingFace (free)
- **Vector DB:** ChromaDB
- **LLM:** Groq LLaMA 3.1 (free)
- **Orchestration:** LangChain

## Run locally

```bash
# Clone the repo
git clone https://github.com/kailashv2/rag-document-chats

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
cd backend
pip install -r requirements.txt

# Add your keys to .env
GROQ_API_KEY=your_key_here

# Start the server
uvicorn main:app --reload

# Open in browser
http://127.0.0.1:8000/app
```

## Built by
[Kailash]
