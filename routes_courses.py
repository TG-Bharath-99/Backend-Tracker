from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Course, User

router = APIRouter(prefix="/courses", tags=["Courses"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- LIST ALL COURSES ----------------
@router.get("/")
def list_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()


# ---------------- SELECT A COURSE (ONE TIME) ----------------
@router.post("/select")
def select_course(user_id: int, course_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    user.selected_course_id = course_id
    db.commit()

    return {
        "message": "Course selected successfully",
        "course_id": course_id,
        "course_name": course.course_name
    }


# ---------------- GET USER SELECTED COURSE ----------------
@router.get("/my-course")
def get_my_course(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user or not user.selected_course_id:
        return {"message": "No course selected yet"}

    course = db.query(Course).filter(
        Course.id == user.selected_course_id
    ).first()

    return course
