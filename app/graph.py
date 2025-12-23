from langgraph.graph import StateGraph, END

from app.agents import (
    planner_agent,
    flight_search_agent,
    pricing_agent,
    approval_agent,
    booking_agent,
    fallback_agent,
    notification_agent,
)

# 🔴 MUST be dict (NOT Pydantic)
graph = StateGraph(dict)

graph.add_node("planner", planner_agent)
graph.add_node("search", flight_search_agent)
graph.add_node("pricing_agent", pricing_agent)
graph.add_node("approval_agent", approval_agent)
graph.add_node("booking_agent", booking_agent)
graph.add_node("fallback_agent", fallback_agent)
graph.add_node("notification_agent", notification_agent)

graph.set_entry_point("planner")

graph.add_edge("planner", "search")
graph.add_edge("search", "pricing_agent")
graph.add_edge("pricing_agent", "approval_agent")

graph.add_conditional_edges(
    "approval_agent",
    lambda state: "approved" if state.get("approved") else "rejected",
    {
        "approved": "booking_agent",
        "rejected": "fallback_agent",
    },
)

graph.add_edge("booking_agent", "notification_agent")
graph.add_edge("notification_agent", END)
graph.add_edge("fallback_agent", END)

# 🔴 NO checkpointer
app = graph.compile()