from fastapi import FastAPI
from database import Base, engine
from seed_data import seed_data
from routes_auth import router as auth_router
from seed_data import seed_data

app = FastAPI()

# ✅ Startup event (CORRECT WAY)
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    seed_data()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.on_event("startup")
def startup_event():
    seed_data()