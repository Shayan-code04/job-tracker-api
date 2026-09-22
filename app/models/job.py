from enum import Enum

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship

from app.database import Base


class JobStatus(str, Enum):
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    REJECTED = "rejected"
    OFFERED = "offered"


class Job(Base):
    __tablename__ = "jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    company = Column(
        String,
        nullable=False
    )

    position = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False,
        default=JobStatus.APPLIED.value
    )

    notes = Column(
        Text,
        nullable=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="jobs"
    )