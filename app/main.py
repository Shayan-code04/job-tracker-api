from fastapi import FastAPI

from app.database import Base, engine

# Import models so SQLAlchemy knows about them
from app.models import User, Job

from app.routers import auth, jobs


# Create database tables
Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Job Tracker API"
)


# Authentication routes
app.include_router(
    auth.router
)


# Job CRUD routes
app.include_router(
    jobs.router
)


@app.get("/")
def root():
    return {
        "message": "Job Tracker API is running"
    }