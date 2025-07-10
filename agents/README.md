# Agent Configuration — Codex Assistant

This folder contains `agents.yaml`, which defines model instructions, personality types, and context preferences for Codex or OpenAI models.

Each agent is used to focus the assistant's behavior in a specific way (e.g., reviewer, strategist, debugger).

## 🔍 File Purpose

- Acts as the **central configuration** for all model agents
- Each agent includes: `id`, `name`, `model`, `instructions`, and `context`
- Used by both backend and frontend to route messages

## 🧠 Codex Context Use

When Codex reads this README and the associated `agents.yaml`, it can:

- Understand that each agent has specific goals and instruction sets
- Know that this folder holds the *personality schema* of the assistant
- Select context sources intelligently based on agent config

## 📄 Example agent definition

```yaml
id: strategist
name: Project Strategist
model: gpt-4
instructions: >
  Help plan the future of the codebase. Avoid specific code edits; focus on patterns, refactors, and abstractions.
context:
  - type: repo_summary
    path: ~/Projects/EleusisAI
```
