import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.database import Base, engine

# Import models so SQLAlchemy knows about them
from app.models import User, Job

from app.routers import auth, jobs


# Create logger
logger = logging.getLogger(__name__)


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Job Tracker API"
)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(
        "Unhandled exception while processing %s %s",
        request.method,
        request.url.path
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error"
        }
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