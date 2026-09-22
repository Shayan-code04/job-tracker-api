from enum import Enum

from pydantic import BaseModel, ConfigDict


# ============================================================
# USER SCHEMAS
# ============================================================

class UserCreate(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str

    model_config = ConfigDict(
        from_attributes=True
    )


class Token(BaseModel):
    access_token: str
    token_type: str


# ============================================================
# JOB SCHEMAS
# ============================================================

class JobStatus(str, Enum):
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    REJECTED = "rejected"
    OFFERED = "offered"


class JobCreate(BaseModel):
    company: str
    position: str
    status: JobStatus = JobStatus.APPLIED
    notes: str | None = None


class JobUpdate(BaseModel):
    status: JobStatus | None = None
    notes: str | None = None


class JobResponse(BaseModel):
    id: int
    company: str
    position: str
    status: JobStatus
    notes: str | None
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )