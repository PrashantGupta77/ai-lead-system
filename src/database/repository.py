from sqlalchemy.orm import Session

from src.database.lead_model import Lead


def save_lead(
    db: Session,
    message: str,
    label: str,
    confidence: float,
    response: str
):

    lead = Lead(
        message=message,
        label=label,
        confidence=confidence,
        response=response
    )

    db.add(lead)

    db.commit()

    db.refresh(lead)

    return lead


def get_lead_stats(db: Session):

    total = db.query(Lead).count()

    hot = (
        db.query(Lead)
        .filter(Lead.label == "HOT")
        .count()
    )

    warm = (
        db.query(Lead)
        .filter(Lead.label == "WARM")
        .count()
    )

    cold = (
        db.query(Lead)
        .filter(Lead.label == "COLD")
        .count()
    )

    return {
        "total": total,
        "hot": hot,
        "warm": warm,
        "cold": cold
    }


def get_recent_leads(
    db: Session,
    limit: int = 10
):

    return (
        db.query(Lead)
        .order_by(Lead.created_at.desc())
        .limit(limit)
        .all()
    )