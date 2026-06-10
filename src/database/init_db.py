from src.database.db import (
    Base,
    engine
)

from src.database.lead_model import Lead
from src.database.user_model import User

from src.database.audit_log_model import AuditLog

def init_db():

    Base.metadata.create_all(
        bind=engine
    )