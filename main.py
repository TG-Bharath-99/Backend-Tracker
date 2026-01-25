from fastapi import FastAPI
from database import Base, engine
from seed_data import seed_data

from routes_auth import router as auth_router
from routes_courses import router as courses_router
from routes_topics import router as topics_router

app = FastAPI()

# 🚀 SINGLE startup event (VERY IMPORTANT)
@app.on_event("startup")
def startup_event():
    print("🚀 Starting backend...")
    Base.metadata.create_all(bind=engine)
    seed_data()

# ✅ Include routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(courses_router, prefix="/courses", tags=["Courses"])
app.include_router(topics_router, prefix="/topics", tags=["Topics"])

@app.get("/")
def root():
    return {"message": "Backend running"}
