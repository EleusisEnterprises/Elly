# Cached Summaries — Context Optimization

This folder holds summaries of files or folders that are **too large to include directly** in a model request.

Each summary:
- Includes a high-level description
- Notes token count
- Links back to the full source

Summaries are generated using an MCP context provider (`summary.py`), which uses GPT to analyze files and cache results locally.

## 🔍 File Purpose

- Improve performance and token usage
- Enable strategic agents to reason about large codebases
- Avoid repeated full-file reads during chat

## 🧠 Codex Context Use

This folder gives Codex:
- Condensed knowledge of the codebase
- Fast access to summarized files without full token cost
- Useful inputs for planning or architecture agents

## 📄 Summary File Format (JSON)

```json
{
  "file": "routes__index.ts",
  "tokens": 1200,
  "summary": "This file defines API routes for user login and session management...",
  "timestamp": "2025-07-10T10:00:00Z"
}
```
