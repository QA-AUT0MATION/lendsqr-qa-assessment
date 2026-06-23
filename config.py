import os

BASE_URL = os.getenv("BASE_URL", "https://adjutor.lendsqr.com")
API_KEY = os.getenv("ADJUTOR_API_KEY")

if not API_KEY:
    raise RuntimeError("Missing ADJUTOR_API_KEY environment variable. Do not hardcode API keys.")


def auth_headers(token: str | None = None) -> dict:
    token = token or API_KEY
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
