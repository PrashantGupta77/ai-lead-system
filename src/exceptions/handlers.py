from fastapi import Request
from fastapi.responses import JSONResponse

from src.core.logger import logger


async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(
        f"Unhandled exception: {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal Server Error"
        }
    )