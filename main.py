from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from seed_data import seed_data

from routes_auth import router as auth_router
from routes_courses import router as courses_router
from routes_topics import router as topics_router

app = FastAPI()

# ✅ CORS (required for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Startup
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    seed_data()

# ✅ Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(courses_router, prefix="/courses", tags=["Courses"])
app.include_router(topics_router, prefix="/topics", tags=["Topics"])

@app.get("/")
def root():
    return {"message": "Backend running"}
