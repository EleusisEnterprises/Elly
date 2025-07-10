# MCP Server — FastAPI Backend

This folder contains the backend implementation for the Model Context Protocol (MCP). It exposes HTTP endpoints used by the SvelteKit frontend and external tools.

## 📌 Endpoints

- `POST /chat` — Accepts a chat message and returns a response from OpenAI. More routes will be added as the protocol evolves.

## 🚀 Usage

```bash
cd mcp-server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The server runs on `http://localhost:8000` by default.

## 🔑 API Key

Set `OPENAI_API_KEY` in your environment so the server can call OpenAI. You can
copy `.env.example` to `.env` and add your key:

The server initializes an `openai.AsyncOpenAI` client which automatically reads
this key when handling requests.

```bash
cp .env.example .env
```
