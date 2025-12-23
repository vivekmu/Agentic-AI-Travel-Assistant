# Agentic AI Travel Assistant

Enterprise-grade Agentic AI using LangGraph with:
- Multi-agent collaboration
- LLM reasoning
- Redis + Vector memory
- Retry & fallback
- Observability (Prometheus + OpenTelemetry)

## 🚀 Features
- Goal-driven autonomous agents
- Human-in-the-loop approvals
- Resilient execution with retries
- Short-term and long-term memory
- Production-style observability

## 🏗️ Architecture (High Level)
User → API / Bot → LangGraph Orchestrator → Agents → APIs → Memory → Observability

## Run
- pip install -r requirements.txt
- python jwt_token.py
- python -m app.main
