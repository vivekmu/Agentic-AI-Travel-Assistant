# Design Decisions

## Why LangGraph?
- Native support for stateful workflows
- Conditional routing
- Parallel agent execution
- Human-in-the-loop support

## Why Multi-Agent?
- Separation of concerns
- Easier debugging
- Independent scaling
- Enterprise maintainability

## Agent Responsibilities
- Planner: reasoning & task breakdown
- Search: external data fetch
- Pricing: decision optimization
- Booking: execution
- Fallback: resilience & escalation

## Retry Strategy
- Limited retries (configurable)
- Automatic fallback on exhaustion
- Prevents infinite loops

## Safety
- No autonomous payments without approval
- Controlled spend limits