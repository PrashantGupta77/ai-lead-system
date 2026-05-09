from pydantic import BaseModel


class LeadInput(BaseModel):
    message: str


class LeadResponse(BaseModel):
    label: str
    confidence: float
    response: str