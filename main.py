from fastapi import FastAPI
from database import engine, Base
from routes_auth import router as auth_router
from seed_data import seed_data

app = FastAPI()

# ✅ Create tables
Base.metadata.create_all(bind=engine)

# ✅ Insert default courses & topics (runs once)
seed_data()

# ✅ Auth routes
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def index():
    return {"message": "Backend started successfully"}
