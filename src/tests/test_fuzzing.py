from http import HTTPStatus

from fastapi.testclient import TestClient
from hypothesis import given, strategies

from example.example2 import api, User

client0 = TestClient(api)


@given(strategies.builds(User))
def test_inserting_random_users(random_user):
    response = client0.put("/user", json=random_user.dict())
    assert response.status_code == HTTPStatus.OK


def test_inserting_random_users_and_check_for_existence():
    client = TestClient(api)

    @given(strategies.builds(User, age=strategies.integers(1, 99)))
    def insert_user(random_user: User):
        response = client.put("/user", json=random_user.dict())
        assert response.status_code == HTTPStatus.OK
        user_id = int(response.text)

        response = client.get(f"/user/{user_id}")
        assert response.status_code == HTTPStatus.OK
        assert response.json() == random_user.dict()

    insert_user()
