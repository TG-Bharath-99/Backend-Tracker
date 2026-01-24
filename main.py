from fastapi import FastAPI
from database import engine, Base
from routes_auth import router as auth_router
from routes_courses import router as courses_router
from routes_topics import router as topics_router



app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router,prefix="/auth",tags=["Auth"])
app.include_router(courses_router)
app.include_router(topics_router)



@app.get("/")
def index():
    return {"message": "Backend started"}

