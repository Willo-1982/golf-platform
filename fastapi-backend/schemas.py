# /fastapi-backend/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str]

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class RoundBase(BaseModel):
    course_name: str
    score: int
    differential: float
    sg_tee: float
    sg_approach: float
    sg_putting: float
    video_url: Optional[str]

class Round(RoundBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

class Group(BaseModel):
    id: int
    name: str
    members: List[User]

    class Config:
        orm_mode = True

class Friend(BaseModel):
    id: int
    friend_email: EmailStr

    class Config:
        orm_mode = True
