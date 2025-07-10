# SvelteKit Frontend — Chat UI for Codex Assistant

This folder holds the frontend chat interface for the assistant. Built in SvelteKit, it connects to the backend MCP server and renders:

- A chat view
- Agent selection panel
- Optional file or diff preview (coming soon)

## 🔍 Folder Purpose

This folder:
- Provides the web UI for all agent interactions
- Allows sending MCP-formatted messages to the backend
- Will eventually support file selection for context routing

## 🧠 Codex Context Use

Codex should use this README to:
- Understand that the frontend is read-only and declarative
- Focus attention on chat rendering, not editing
- Identify where agent selection and UI components live

## 🗂️ Key Structure

```
sveltekit-ui/
├── src/routes/         # Chat and agent routes
├── lib/api.ts          # Communicates with MCP backend
├── lib/components/     # ChatBox, AgentSelector, etc.
```
