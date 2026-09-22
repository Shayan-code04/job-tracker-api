from sqlalchemy.orm import Session

from app.models.user import User


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