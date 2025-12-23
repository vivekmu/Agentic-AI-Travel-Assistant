import os

# -----------------------------
# Helper functions
# -----------------------------
def _get_required_str(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Required environment variable '{name}' is not set")
    return value

def _get_required_int(name: str) -> int:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Required environment variable '{name}' is not set")
    try:
        return int(value)
    except ValueError:
        raise RuntimeError(f"Environment variable '{name}' must be an integer")

# -----------------------------
# Security & Policy (STRICT)
# -----------------------------
JWT_SECRET = _get_required_str("JWT_SECRET")
JWT_ALGO = "HS256"

MAX_PRICE_LIMIT = _get_required_int("MAX_PRICE_LIMIT")
MAX_RETRIES = _get_required_int("MAX_RETRIES")

# -----------------------------
# Authorization
# -----------------------------
APPROVER_ROLES = ["FINANCE_APPROVER", "ADMIN"]