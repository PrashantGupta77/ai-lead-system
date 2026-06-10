from tests.conftest import client


def test_health_endpoint():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_process_endpoint():

    payload = {
        "message": "Need AI automation for customer support"
    }

    response = client.post("/process", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "label" in data
    assert "confidence" in data
    assert "response" in data