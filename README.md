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
**POST /chat**
Primary conversation endpoint. 

This endpoint accepts a structured request and returns a structured response.
It currently returns a mock (stub) response and will later be connected to the LangGraph agent.

Note about the correction schema: although corrections are currently returned as an empty list (stub implementation),
this structure will be used by the agent to provide intelligent feedback and **track learning** progress.

## Current Status
- ✅ FastAPI backend running
- ✅ Modular src/ layout
- ✅ Health endpoint
- ✅ Structured /chat endpoint
- ✅ Stub conversational response
- 🚧 LangGraph integration (coming next)
- 🚧 Persistent memory & progress tracking

Also, extensible architecture allows for future features like multiple client interfaces and voice input.

TODO: -check whether streaming response support is needed (i.e. tokens instead of full response) for better user experience.