from dotenv import load_dotenv
load_dotenv()

from app.graph import app
from app.security import authenticate, sanitize_goal
#from app.state import TravelState

# -------------------
# Simulated incoming request
# -------------------
JWT_TOKEN = "Provide a valid JWT token here by running 'python jwt_token.py' once."

user = authenticate(JWT_TOKEN)

goal = "Book flight Coimbatore to Chennai Friday evening under 7000"
sanitize_goal(goal)

# -------------------
# Initialize typed state
# -------------------
initial_state = {
    "__start__": {   # 🔴 REQUIRED FOR PREGEL
        "goal": goal,
        "user": user,
        "retries": 0,
        "approved": False,
    }
}
# -------------------
# Invoke graph
# -------------------
result = app.invoke(initial_state)

print("\nFINAL RESULT:\n", result)