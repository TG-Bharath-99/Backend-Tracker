from fastapi import FastAPI
from database import engine, Base
from routes_auth import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router,prefix="/auth",tags=["Auth"])

@app.get("/")
def index():
    return {"message": "Backend started"}

