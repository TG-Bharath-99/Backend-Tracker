from pydantic import BaseModel, EmailStr
from pydantic import StringConstraints
from typing import Optional, Annotated


PasswordStr = Annotated[
    str,
    StringConstraints(min_length=6, max_length=50)
]


class UserSignup(BaseModel):
    full_name: str
    email: EmailStr
    password: PasswordStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    selected_course_id: Optional[int]
