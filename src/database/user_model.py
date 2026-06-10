from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime, UTC

from src.database.db import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(20),
        default="USER"
    )

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )