from sqlalchemy.orm import Session

from src.pipeline import (
    classify_lead,
    generate_response
)

from src.database.repository import save_lead

from src.core.logger import logger

class LeadService:

    @staticmethod
    def process_lead(
        db: Session,
        message: str
    ):

        label, confidence = classify_lead(
            message
        )

        logger.info(
            f"Lead classified | "
            f"label={label} "
            f"confidence={confidence}"
        )

        response = generate_response(
            message,
            label
        )

        save_lead(
            db=db,
            message=message,
            label=label,
            confidence=confidence,
            response=response
        )

        logger.info(
            f"Lead saved successfully | "
            f"label={label} "
            f"confidence={confidence}"
        )

        return {
            "label": label,
            "confidence": confidence,
            "response": response
        }