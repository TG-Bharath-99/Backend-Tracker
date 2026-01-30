from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Motivation
import random

router = APIRouter()

@router.get("/motivation/random")
def get_random_motivation(db: Session = Depends(get_db)):
    messages = db.query(Motivation).all()
    if not messages:
        return {"message": "Keep learning!"}

    msg = random.choice(messages)
    return {"message": msg.message}
