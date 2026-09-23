from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.user import User
from app.models import Job

# ============================================================
# GET USER BY EMAIL
# ============================================================

def get_user_by_email(
    db: Session,
    email: str
):
    return db.query(User).filter(
        User.email == email
    ).first()


# ============================================================
# CREATE USER
# ============================================================

def create_user(
    db: Session,
    email: str,
    password_hash: str
):
    new_user = User(
        email=email,
        password_hash=password_hash
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
def get_job_analytics(db, user_id):
    total_applications = (
        db.query(func.count(Job.id))
        .filter(Job.user_id == user_id)
        .scalar()
    )

    status_counts = (
        db.query(
            Job.status,
            func.count(Job.id)
        )
        .filter(Job.user_id == user_id)
        .group_by(Job.status)
        .all()
    )

    by_status = {
        status: count
        for status, count in status_counts
    }

    interviewing = by_status.get("interviewing", 0)
    offered = by_status.get("offered", 0)

    if total_applications > 0:
        interview_rate = (
            (interviewing + offered)
            / total_applications
        ) * 100
    else:
        interview_rate = 0.0

    return {
        "total_applications": total_applications,
        "by_status": by_status,
        "interview_rate": interview_rate
    }