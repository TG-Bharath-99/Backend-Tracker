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

class CourseResponse(BaseModel):
    id: int
    course_name: str

class TopicResponse(BaseModel):
    id: int
    topic_name: str
    youtube_url: str
    is_completed: bool
