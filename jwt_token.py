from dotenv import load_dotenv
import os
import jwt

load_dotenv()  # 🔴 REQUIRED

secret = os.getenv("JWT_SECRET")

#print("JWT_SECRET loaded:", secret)  # debug line for testing

token = jwt.encode(
    {"user": "vivek", "role": "FINANCE_APPROVER"},
    secret,
    algorithm="HS256"
)

print(token)