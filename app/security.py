import jwt
from app.config import JWT_SECRET, JWT_ALGO, APPROVER_ROLES

FORBIDDEN_WORDS = ["password", "credit card", "cvv", "otp"]

# -------------------
# Authentication
# -------------------
def authenticate(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        return payload
    except Exception:
        raise Exception("Authentication failed")

# -------------------
# Authorization (RBAC)
# -------------------
def authorize(user: dict, allowed_roles: list):
    if user.get("role") not in allowed_roles:
        raise Exception("Authorization failed")

# -------------------
# Input Sanitization
# -------------------
def sanitize_goal(goal: str):
    for word in FORBIDDEN_WORDS:
        if word in goal.lower():
            raise Exception("Sensitive data detected in input")

# -------------------
# Policy Check
# -------------------
def enforce_policy(flight: dict, user: dict, max_price: int):
    if flight["price"] > max_price:
        raise Exception("Policy violation: price limit exceeded")

    if user["role"] not in APPROVER_ROLES:
        raise Exception("Policy violation: approval role required")