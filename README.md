# chatter-mate
An LLM-powered conversational language partner built with LangGraph and FastAPI. 
ChatterMate helps users improve their language skills through natural, casual chat, while providing intelligent corrections, 
contextual explanations, and adaptive coaching.

The project is designed with a **modular architecture**, separating:

- Backend application logic
- API layer
- Agent logic
- Clients (CLI, future voice...)

This ensures flexibility, scalability, and clean client-server communication.

## Architecture Overview

ChatterMate follows a decoupled client–server architecture:

```
Client (CLI / Web / Bot / Voice)
        ↓
HTTP API (FastAPI)
        ↓
Agent Layer (LangGraph)
        ↓
Persistence (future: memory & progress tracking)
```
