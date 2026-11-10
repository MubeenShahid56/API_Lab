import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")  # Read from .env; never hardcode a real secret.
headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {
    "Authorization": "Bearer YOUR_TOKEN_HERE"
}
print("Authorization header configured:", "Authorization" in headers)
print("Authorization value: Bearer [REDACTED]")

# JSONPlaceholder is a public demonstration API and does not require this token.
# This shows how to construct a protected-API request without exposing a real key.
