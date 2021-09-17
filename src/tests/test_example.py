from http import HTTPStatus
from fastapi.testclient import TestClient

from example.example2 import api

demo_user = {"first_name": "Peter", "last_name": "Higgs", "age": 92}


def test_read_main():
    client = TestClient(api)
    response = client.put("/user", json=demo_user)

    assert response.status_code == HTTPStatus.OK
    assert response.text == str(0)

    response = client.get("/user/0")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == demo_user

    response = client.get("/user/1")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User '1' does not exist."}
