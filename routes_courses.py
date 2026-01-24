from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Course

router = APIRouter(prefix="/courses", tags=["Courses"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- ADD COURSE ----------------
@router.post("/")
def add_course(course_name: str, db: Session = Depends(get_db)):
    existing = db.query(Course).filter(Course.course_name == course_name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Course already exists")

    course = Course(course_name=course_name)
    db.add(course)
    db.commit()
    db.refresh(course)

    return {"id": course.id, "course_name": course.course_name}


# ---------------- LIST COURSES ----------------
@router.get("/")
def list_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses
