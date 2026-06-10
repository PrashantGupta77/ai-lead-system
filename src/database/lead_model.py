# src/database/lead_model.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime, UTC

from src.database.db import Base


class Lead(Base):

    __tablename__ = "leads"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    message = Column(
        String(1000),
        nullable=False
    )

    label = Column(
        String(20),
        nullable=False
    )

    confidence = Column(
        Float,
        nullable=False
    )

    response = Column(
        String(2000),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        default=lambda:datetime.now(UTC)
    )