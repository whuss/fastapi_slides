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

# Comparison (Code ⇔ **OpenAPI Spec**)

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/user/{user_id}": {
      "get": {
        "summary": "Get User",
        "operationId": "get_user_user__user_id__get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "title": "User Id",
              "type": "integer"
            },
            "name": "user_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/User"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/user": {
      "put": {
        "summary": "Create User",
        "operationId": "create_user_user_put",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/User"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "title": "Response Create User User Put",
                  "type": "integer"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "delete": {
        "summary": "Delete User",
        "operationId": "delete_user_user_delete",
        "parameters": [
          {
            "required": true,
            "schema": {
              "title": "User Id",
              "type": "integer"
            },
            "name": "user_id",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/User"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "HTTPValidationError": {
        "title": "HTTPValidationError",
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            }
          }
        }
      },
      "User": {
        "title": "User",
        "required": [
          "last_name",
          "first_name",
          "age"
        ],
        "type": "object",
        "properties": {
          "last_name": {
            "title": "Last Name",
            "type": "string"
          },
          "first_name": {
            "title": "First Name",
            "type": "string"
          },
          "age": {
            "title": "Age",
            "type": "integer"
          }
        }
      },
      "ValidationError": {
        "title": "ValidationError",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "type": "object",
        "properties": {
          "loc": {
            "title": "Location",
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "msg": {
            "title": "Message",
            "type": "string"
          },
          "type": {
            "title": "Error Type",
            "type": "string"
          }
        }
      }
    }
  }
}
```

---

# Comparison (**Code** ⇔ OpenAPI Spec)

```python
from http import HTTPStatus
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from example.simple_db import Database


class User(BaseModel):
    last_name: str
    first_name: str
    age: int


db: Database[User] = Database()

api = FastAPI()


@api.get("/user/{user_id}", response_model=User)
def get_user(user_id: int):
    user = db.find(user_id)
    if user is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"User '{user_id}' does not exist.",
        )
    return user


@api.put("/user", response_model=int)
def create_user(user: User):
    user_id = db.create(user)
    return user_id


@api.delete("/user", response_model=Optional[User])
def delete_user(user_id: int):
    deleted_user = db.delete(user_id)
    return deleted_user


if __name__ == "__main__":
    uvicorn.run("example2:api", host="0.0.0.0", port=9001, reload=True)
```

---

A note on this method, to use it with markdown you need to use code like this <section class="hbox">	<div class="container"> <div class="flex-col" data-markdown> * Column 1 Content </div> <div class="flex-col" data-markdown> * Column 2 Content </div> </div> </section>