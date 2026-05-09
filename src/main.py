from fastapi import FastAPI

from src.models import (
    LeadInput,
    LeadResponse
)

from src.pipeline import (
    classify_lead,
    generate_response
)

app = FastAPI(
    title="AI Lead Qualification System"
)


@app.get("/")
def health():

    return {
        "status": "running"
    }


@app.post(
    "/process",
    response_model=LeadResponse
)

def process_lead(input: LeadInput):

    message = input.message.strip()

    # classify

    label, confidence = classify_lead(
        message
    )

    # generate response

    response = generate_response(
        message,
        label
    )

    return {

        "label": label,
        "confidence": confidence,
        "response": response
    }