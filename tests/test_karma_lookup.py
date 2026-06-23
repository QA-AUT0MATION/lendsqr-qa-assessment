import pytest
import requests
from config import BASE_URL, auth_headers


@pytest.mark.api
def test_karma_lookup_valid_token():
    response = requests.get(
        f"{BASE_URL}/v2/verification/karma/test@example.com",
        headers=auth_headers(),
        timeout=30,
    )
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3
    assert isinstance(response.json(), dict)


@pytest.mark.api
def test_karma_lookup_invalid_token():
    response = requests.get(
        f"{BASE_URL}/v2/verification/karma/test@example.com",
        headers=auth_headers("invalid_token"),
        timeout=30,
    )
    assert response.status_code in [401, 403]
    body = response.json()
    assert body.get("status") == "error"
    assert "access" in body.get("message", "").lower() or "api key" in body.get("message", "").lower()
