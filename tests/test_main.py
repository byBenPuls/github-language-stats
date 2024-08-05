from fastapi.testclient import TestClient
from src.main import create_app as app

client = TestClient(app())


class TestResponses:
    def test_read_main(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}
