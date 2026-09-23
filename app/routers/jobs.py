from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud
from app.schemas import AnalyticsResponse
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status
)

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.job import Job
from app.models.user import User
from app.schemas import (
    JobCreate,
    JobResponse,
    JobStatus,
    JobUpdate
)
from app.auth import get_current_user


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


# ============================================================
# 1. CREATE JOB
# POST /jobs
# ============================================================

@router.post(
    "",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED
)
def create_job(
    job_data: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_job = Job(
        company=job_data.company,
        position=job_data.position,
        status=job_data.status.value,
        notes=job_data.notes,

        # IMPORTANT:
        # The user ID comes from the JWT.
        user_id=current_user.id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


# ============================================================
# 2. GET MY JOBS
# GET /jobs
# GET /jobs?status=interviewing
# ============================================================

@router.get(
    "",
    response_model=list[JobResponse]
)
def get_jobs(
    status_filter: JobStatus | None = Query(
        default=None,
        alias="status"
    ),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Job).filter(
        Job.user_id == current_user.id
    )

    if status_filter is not None:
        query = query.filter(
            Job.status == status_filter.value
        )

    return query.all()

@router.get("/analytics", response_model=AnalyticsResponse)
def get_analytics(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.get_job_analytics(db, current_user.id)
# ============================================================
# 3. GET ONE JOB
# GET /jobs/{job_id}
# ============================================================

@router.get(
    "/{job_id}",
    response_model=JobResponse
)
def get_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )

    # OWNERSHIP CHECK
    if job.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this job"
        )

    return job


# ============================================================
# 4. UPDATE JOB
# PUT /jobs/{job_id}
# ============================================================

@router.put(
    "/{job_id}",
    response_model=JobResponse
)
def update_job(
    job_id: int,
    job_data: JobUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )

    # OWNERSHIP CHECK
    if job.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to update this job"
        )

    if job_data.status is not None:
        job.status = job_data.status.value

    if job_data.notes is not None:
        job.notes = job_data.notes

    db.commit()
    db.refresh(job)

    return job


# ============================================================
# 5. DELETE JOB
# DELETE /jobs/{job_id}
# ============================================================

@router.delete(
    "/{job_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )

    # OWNERSHIP CHECK
    if job.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to delete this job"
        )

    db.delete(job)
    db.commit()

    return None