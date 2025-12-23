
---

# 📄 `architecture.md` (Technical Architecture)

```md
# Architecture Overview

## 🧩 Components

### 1. User Interface
- Web UI / Mobile App / Teams Bot
- Sends high-level goals (not steps)

### 2. Agent Orchestrator (LangGraph)
- Controls agent execution flow
- Manages state transitions
- Handles retries and fallbacks

### 3. Agents
- Planner Agent (LLM reasoning)
- Flight Search Agent
- Pricing Agent
- Weather & Risk Agents (parallel)
- Booking Agent
- Fallback Agent
- Notification Agent

### 4. Memory Layer
- Redis: short-term session memory
- Vector Store (Chroma): long-term learning

### 5. Observability
- Prometheus: metrics
- OpenTelemetry: tracing
- Logs for audit & RCA

## 🔐 Enterprise Controls
- Approval checkpoints
- Retry limits
- Audit trail
- Fail-safe fallback

## 📐 Data Flow
User → Planner → Parallel Agents → Decision → Approval → Execution → Notification