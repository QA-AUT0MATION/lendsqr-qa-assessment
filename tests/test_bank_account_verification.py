import pytest
import requests
from config import BASE_URL, auth_headers

PAYLOAD = {
    "account_number": "0425571111",
    "bank_code": "058",
}


@pytest.mark.api
def test_bank_account_bvn_valid_token():
    response = requests.post(
        f"{BASE_URL}/v2/verification/bankaccount/bvn",
        json=PAYLOAD,
        headers=auth_headers(),
        timeout=30,
    )
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3
    assert isinstance(response.json(), dict)


@pytest.mark.api
def test_bank_account_bvn_invalid_token():
    response = requests.post(
        f"{BASE_URL}/v2/verification/bankaccount/bvn",
        json=PAYLOAD,
        headers=auth_headers("invalid_token"),
        timeout=30,
    )
    assert response.status_code in [401, 403]
    body = response.json()
    assert body.get("status") == "error"
