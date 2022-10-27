from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: str
    name: str


class UserUpdate(Basemodel):
    name: str
    email: str
    password: str
