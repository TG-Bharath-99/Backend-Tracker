from pydantic import BaseModel, EmailStr
from typing import Optional


class UserSignup(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    selected_course_id: Optional[int]
    
    class Config:
        from_attributes = True