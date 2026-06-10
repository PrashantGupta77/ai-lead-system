import os

from dotenv import load_dotenv
from groq import Groq

from src.core.logger import logger

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


MODEL_NAME = "llama-3.1-8b-instant"


def call_llm(prompt: str) -> str:

    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[

                {
                    "role": "system",
                    "content": "You are a precise AI assistant."
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.2,
            max_tokens=100
        )

        return (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

    except Exception as e:

        logger.error(
            f"LLM call failed: {str(e)}"
        )

        return ""