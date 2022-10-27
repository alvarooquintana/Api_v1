import uuid
from fastapi import APIRouter, HTTPException, status

from db.db import engine
from schema import UserCreate, UserResponse, UserUpdate
from models.user import User

router = APIRouter()


@router.get("/users")
async def users():
    users = await engine.find(User)
    return users


@router.get("/user/{user_id}")
async def user(user_id):
    user = await engine.find(User.id == user_id)
    return user


@router.post("/user", response_model=UserResponse)
async def create_user(user: UserCreate):
    users = User(
        name=user.name, email=user.email, password=user.password, id=uuid.uuid4().hex
    )
    await engine.save(users)
    return users


@router.put("/user/{user_id}")
async def update_user(user: UserUpdate, user_id: str):
    new_user = engine.find_one(User, User.id == user_id)

    new_user.name = user.name
    new_user.email = user.email
    new_user.password = user.password

    return new_user


@router.delete("/user/{user_id}")
def delete_user():
    pass
