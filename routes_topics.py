from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Topic, Course, User, Progress
from dependencies import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def get_topics(course_id: int, db: Session = Depends(get_db)):
    topics = db.query(Topic).filter(Topic.course_id == course_id).all()
    return topics


@router.post("/add")
def add_topic(
    course_id: int,
    topic_name: str,
    youtube_url: str,
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    topic = Topic(
        course_id=course_id,
        topic_name=topic_name,
        youtube_url=youtube_url
    )

    db.add(topic)
    db.commit()
    db.refresh(topic)

    return topic


@router.get("/user")
def list_topics_for_user(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.selected_course_id is None:
        raise HTTPException(status_code=400, detail="Select course first")

    topics = db.query(Topic).filter(
        Topic.course_id == current_user.selected_course_id
    ).all()

    result = []
    for topic in topics:
        progress = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.topic_id == topic.id
        ).first()

        result.append({
            "topic_id": topic.id,
            "topic_name": topic.topic_name,
            "youtube_url": topic.youtube_url,
            "completed": progress.is_completed if progress else False
        })

    return result


@router.post("/mark/{topic_id}")
def mark_topic(
    topic_id: int,
    completed: bool,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.topic_id == topic_id
    ).first()

    if not progress:
        progress = Progress(
            user_id=current_user.id,
            topic_id=topic_id,
            is_completed=completed
        )
        db.add(progress)
    else:
        progress.is_completed = completed

    db.commit()

    return {
        "message": "Progress updated",
        "topic_id": topic_id,
        "completed": completed
    }