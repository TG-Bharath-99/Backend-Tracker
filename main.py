from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from database import Base, engine
from seed_data import seed_data
from routes_auth import router as auth_router
from routes_courses import router as courses_router
from routes_topics import router as topics_router
from starlette.middleware.proxy_headers import ProxyHeadersMiddleware


app = FastAPI()
app.add_middleware(
    ProxyHeadersMiddleware,
    trusted_hosts="*"
)


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    seed_data()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(courses_router, prefix="/courses", tags=["Courses"])
app.include_router(topics_router)
