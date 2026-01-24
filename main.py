from fastapi import FastAPI
from database import Base, engine
from seed_data import seed_data

from routes_auth import router as auth_router
from routes_courses import router as courses_router
from routes_topics import router as topics_router
from routes_progress import router as progress_router

app = FastAPI()

# ✅ SINGLE startup event (ONLY ONE)
@app.on_event("startup")
def startup_event():
    print("🚀 Starting backend...")
    Base.metadata.create_all(bind=engine)
    seed_data()

# ✅ INCLUDE ALL ROUTERS
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(courses_router, prefix="/courses", tags=["Courses"])
app.include_router(topics_router, prefix="/topics", tags=["Topics"])
app.include_router(progress_router, prefix="/progress", tags=["Progress"])

@app.get("/")
def root():
    return {"message": "Backend running"}
