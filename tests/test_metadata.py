from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_metadata():

    response = client.get(
        "/api/v1/metadata"
    )

    assert response.status_code == 200

    assert "accuracy" in response.json()