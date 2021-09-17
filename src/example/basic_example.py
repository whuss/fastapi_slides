# Basic example without any data validation.
# For the full example see main.py

from fastapi import FastAPI
import uvicorn

from example.simple_db import Database

db = Database()

api = FastAPI()


@api.get("/user/{user_id}")
def get_user(user_id):
    user = db.find(user_id)
    return user


@api.put("/user")
def create_user(user):
    user_id = db.create(user)
    return user_id


@api.delete("/user")
def delete_user(user_id):
    deleted_user = db.delete(user_id)
    return deleted_user


if __name__ == "__main__":
    uvicorn.run("basic_example:api", host="0.0.0.0", port=9001, reload=True)
