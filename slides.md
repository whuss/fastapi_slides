---
marp: true
---

![FastAPI](assets/fastapi_logo.png)


Documentation: https://fastapi.tiangolo.com

Source Code: https://github.com/tiangolo/fastapi


Markdown Presentation Ecosystem

https://marp.app/

---

![bg 90%](assets/architecture.drawio.svg)

---

# Features


- Fully async
- WebSocket support.
- GraphQL support.
- Automatic data validation
- In-process background tasks.
- Startup and shutdown events.
- Test client built on requests.
- CORS, GZip, Static Files, Streaming responses.
- Session and Cookie support.
- 100% test coverage.
- 100% type annotated codebase.

---

# Powered by standard Python type hints

- Type checking
- IDE auto-completion
- Data validation
- Data serialization
- Automatic API documentation
- Automatic OpenAPI schema generation

---

# Basic example

```python
from fastapi import FastAPI

api = FastAPI()

@api.get("/user/{user_id}")
def get_user(user_id):
    user = db.find(user_id)
    return user

@api.put("/user")
def create_user(user):
    user_id = db.create(user)
    return user_id
```

---

# Automatic data validation (Pydantic)

```python
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    last_name: str
    first_name: str
    age: int

api = FastAPI()

@api.get("/user/{user_id}", response_model=Optional[User])
def get_user(user_id: int):
    user = db.find(user_id)
    return user

@api.put("/user", response_model=int)
def create_user(user: User):
    user_id = db.create(user)
    return user_id
```

---

# Error handling

- Automatic handling of data validation errors
- `HTTPException` for custom errors handling

```python
@api.get("/user/{user_id}", response_model=User)
def get_user(user_id: int):
    user = db.find(user_id)
    if user is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"User '{user_id}' does not exist.",
        )
    return user
```

---

# Testing

```python
from http import HTTPStatus
from fastapi.testclient import TestClient
from main import api

demo_user = {"first_name": "Wilfried", "last_name": "Huss", "age": 42}

def test_create_user():
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
```

---

![bg 70](assets/example.svg)
