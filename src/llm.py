import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def call_llm(prompt: str) -> str:

    try:

        response = client.chat.completions.create(

            model="llama3-8b-8192",

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

        return response.choices[0].message.content.strip()

    except Exception as e:

        print("LLM ERROR:", str(e))

        return ""