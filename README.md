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
Primary conversation endpoint. Accepts a structured request and returns a structured response, 
including the assistant's reply and any language corrections detected in the user's message.

## Nodes
- **detect_language**: detects whether the user's message contains the target language.
- **detect_errors**: analyzes errors and generates the conversational response. 

The node design aims to minimize LLM calls per turn by combining related tasks within a single call. 
This reduces the maximum number of LLM calls to 2 per turn (1 if no target language is detected).

## Running with Docker

```bash
docker build -t chatter-mate .
docker run -p 8000:8000 chatter-mate
```

## Current Status
- ✅ FastAPI backend running
- ✅ Modular src/ layout
- ✅ Health endpoint
- ✅ Structured /chat endpoint
- ✅ CLI client
- ✅ LangGraph graph with mock nodes (end-to-end flow working)
- 🚧 LLM integration for language detection and error analysis
- 🚧 Persistent memory & progress tracking

Also, extensible architecture allows for future features like multiple client interfaces and voice input.

TODO: -check whether streaming response support is needed (i.e. tokens instead of full response) for better user experience.