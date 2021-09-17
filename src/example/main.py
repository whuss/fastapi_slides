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
