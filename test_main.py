from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello All! Look at Wikipedia APIs."}


def test_read_phrase():
    response = client.get("/phrase/A R Reheman")
    assert response.status_code == 200
    assert response.json() == {
    "result": [
        "allah rakha rahman",
        "a. s. dileep kumar",
        "january",
        "arr",
        "indian music composer",
        "record producer",
        "indian cinema",
        "tamil",
        "hindi",
        "occasional forays",
        "international cinema"
    ]
    }