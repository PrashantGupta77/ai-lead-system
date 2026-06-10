from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime, UTC

from src.database.db import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(255),
        nullable=False
    )

    action = Column(
        String(255),
        nullable=False
    )

    timestamp = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )