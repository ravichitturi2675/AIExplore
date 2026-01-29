# System Architecture

## Overview
A local AI-powered web converter.
- **Frontend:** HTML5/CSS3/JavaScript (Single Page App)
- **Backend:** Python (Flask) acts as the API and orchestrator.
- **Intelligence:** **Ollama API** running locally (Model: `codellama`).

## Layer 2: Navigation
1. User inputs Java Code in UI.
2. Frontend POSTs to `/api/convert`.
3. Backend constructs a prompt for Ollama.
4. Backend calls Ollama API (`POST /api/generate`).
5. Backend parses/cleans response.
6. Frontend displays result.

## Layer 3: Tools Strategy
- `app.py`: Flask entry point.
- `ai_engine.py`: Handles communication with Ollama (Prompts, formatting).
- `converter.py`: Orchestrates the flow (Input -> Prompt -> AI -> Output).

