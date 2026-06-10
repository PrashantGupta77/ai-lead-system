from datetime import datetime

from pydantic import BaseModel, Field

from typing import Literal


class LeadInput(BaseModel):
    message: str = Field(
        min_length=3,
        max_length=2000
    )


class LeadResponse(BaseModel):
    label: str
    confidence: float
    response: str


class UserRegister(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=30,
        pattern=r"^[a-zA-Z0-9_]+$",
        description="Username must be between 3 and 30 characters"
    )

    password: str = Field(
        min_length=8,
        max_length=72,
        description="Password must be between 8 and 72 characters"
    )


class RoleUpdate(BaseModel):
    role: Literal["ADMIN", "USER"]


class AuditLogResponse(BaseModel):
    username: str
    action: str
    timestamp: datetime