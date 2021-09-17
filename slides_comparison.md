---
marp: true
---

# Comparison (Code ⇔ OpenAPI Spec)

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
          "404": {
            "description": "Not Found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPError"
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
          "404": {
            "description": "Not Found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPError"
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
      "HTTPError": {
        "title": "HTTPError",
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "type": "string"
          }
        }
      },
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

# Comparison (Code ⇔ OpenAPI Spec)

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import uvicorn

from example.simple_db import Database


class User(BaseModel):
    last_name: str
    first_name: str
    age: int


class HTTPError(BaseModel):
    detail: str


db: Database[User] = Database()

api = FastAPI()


@api.get(
    "/user/{user_id}",
    response_model=User,
    responses={status.HTTP_404_NOT_FOUND: {"model": HTTPError}},
)
def get_user(user_id: int):
    user = db.find(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User '{user_id}' does not exist.",
        )
    return user


@api.put("/user", response_model=int)
def create_user(user: User):
    user_id = db.create(user)
    return user_id


@api.delete(
    "/user",
    response_model=User,
    responses={status.HTTP_404_NOT_FOUND: {"model": HTTPError}},
)
def delete_user(user_id: int):
    deleted_user = db.delete(user_id)
    if deleted_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User '{user_id}' does not exist.",
        )

    return deleted_user


if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=9001, reload=True)

```
