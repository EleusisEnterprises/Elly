# MCP Server — FastAPI Backend

This folder contains the backend implementation for the Model Context Protocol (MCP). It exposes HTTP endpoints used by the SvelteKit frontend and external tools.

## 📌 Endpoints

- `POST /chat` — Accepts a chat message and returns a placeholder response. More routes will be added as the protocol evolves.

## 🚀 Usage

```bash
cd mcp-server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The server runs on `http://localhost:8000` by default.
