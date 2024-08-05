from fastapi.testclient import TestClient
from src.main import create_app as app

client = TestClient(app())


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
