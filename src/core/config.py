from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_DB = os.getenv("MYSQL_DB")

    SECRET_KEY = os.getenv("SECRET_KEY")

    if not SECRET_KEY:
        raise ValueError("SECRET_KEY is not set in environment variables")


settings = Settings()