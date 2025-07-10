# Codex Assistant — Repo-Aware AI Chat Tool

This project implements a local AI assistant that understands your codebase using the Model Context Protocol (MCP). It connects a Python backend and SvelteKit UI to OpenAI models like GPT-4.

It does **not generate code** directly. Instead, it helps **analyze, explain, and plan** using full access to your repo and agents defined in YAML.

## 🧠 Purpose

This tool is designed for **context-first interaction with OpenAI models**, specifically:

- Reading your repo structure, files, and diffs
- Summarizing or reviewing pull requests
- Answering questions about the codebase
- Acting as a design advisor for future development

## 🗂️ Structure Overview

```
Elly/
├── mcp-server/       # FastAPI backend with MCP endpoints
├── sveltekit-ui/     # Frontend chat interface (SvelteKit)
├── agents/           # YAML agent definitions (see `agents/agents.yaml`)
├── summaries/        # Cached summaries of large files
└── README.md         # This file — high-level context
```

## 🔧 Setup Instructions

### Backend (MCP server)
```bash
cd mcp-server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
See `mcp-server/README.md` for endpoint details and additional usage notes.

### Frontend (SvelteKit UI)
```bash
cd sveltekit-ui
npm install
npm run dev
```
Open `http://localhost:5173` to interact with the chat interface.

---

## 🧠 Codex Context Use

This README is intended to help Codex:

- Understand the overall purpose of the assistant
- Identify the backend and frontend folder roles
- See where agent personalities are defined
- Locate summary caches used for planning

This file should be included in every model context request involving strategic or high-level planning.

## ✍️ Customizing Agents

Edit `agents/agents.yaml` to add or adjust agent personalities. Each entry defines
an `id`, `name`, `model`, `instructions`, and a `context` list. Update these fields
to tailor how the assistant operates.
