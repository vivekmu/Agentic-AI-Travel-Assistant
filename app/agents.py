from app.config import MAX_RETRIES, MAX_PRICE_LIMIT
from app.security import enforce_policy
from app.observability import tracer

# -------------------
# Planner
# -------------------
def planner_agent(state):
    with tracer.start_as_current_span("planner_agent"):

        # 🔴 FLATTEN __start__ STATE
        if "__start__" in state:
            start = state.pop("__start__")

            # merge values only if not already present
            for k, v in start.items():
                state.setdefault(k, v)

        # ensure defaults
        state.setdefault("retries", 0)
        state.setdefault("approved", False)

        return state

# -------------------
# Search
# -------------------
def flight_search_agent(state):
    with tracer.start_as_current_span("flight_search_agent"):
        state["flights"] = [
            {"airline": "IndiGo", "time": "18:45", "price": 6200},
            {"airline": "Air India", "time": "19:30", "price": 6800},
            {"airline": "Vistara", "time": "20:15", "price": 7400},
        ]
        return state

# -------------------
# Pricing
# -------------------
def pricing_agent(state):
    with tracer.start_as_current_span("pricing_agent"):
        affordable = [
            f for f in state.get("flights", [])
            if f["price"] <= MAX_PRICE_LIMIT
        ]

        if not affordable:
            # No affordable options → force rejection
            state["approved"] = False
            return state

        state["selected_flight"] = min(
            affordable, key=lambda x: x["price"]
        )
        return state

# -------------------
# Approval (RBAC + Policy)
# -------------------
def approval_agent(state):
    with tracer.start_as_current_span("approval_agent"):
        user = state.get("user")
        flight = state.get("selected_flight")

        # Basic validation
        if not user or not flight:
            state["approved"] = False
            state["approval_reason"] = "Missing user or flight details"
            return state

        try:
            # RBAC + price policy
            enforce_policy(flight, user, MAX_PRICE_LIMIT)

            state["approved"] = True
            state["approval_reason"] = "Approved"

        except Exception as e:
            state["approved"] = False
            state["approval_reason"] = str(e)

            # Optional: add observability signal
            tracer.get_current_span().set_attribute(
                "approval.error", str(e)
            )

        return state

# -------------------
# Booking (Retry Guard)
# -------------------
def booking_agent(state):
    with tracer.start_as_current_span("booking_agent"):
        if not state.get("approved"):
            return state

        if state["retries"] >= MAX_RETRIES:
            return state

        try:
            # Simulate transient failure
            if state["retries"] < MAX_RETRIES - 1:
                raise RuntimeError("Temporary booking failure")

            state["booking_result"] = {
                "PNR": "PNR-SECURE-001",
                "status": "CONFIRMED",
                "flight": state["selected_flight"],
            }

        except Exception:
            state["retries"] += 1

        return state

# -------------------
# Fallback
# -------------------
def fallback_agent(state):
    with tracer.start_as_current_span("fallback_agent"):
        state["booking_result"] = {
            "status": "ESCALATED",
            "reason": "Policy violation or retry limit reached",
        }
        return state

# -------------------
# Notify
# -------------------
def notification_agent(state):
    with tracer.start_as_current_span("notification_agent"):
        print("NOTIFICATION:", state.get("booking_result"))
        return state