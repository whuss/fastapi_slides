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


if __name__ == "__main__":
    uvicorn.run("example1:api", host="0.0.0.0", port=9001, reload=True)
