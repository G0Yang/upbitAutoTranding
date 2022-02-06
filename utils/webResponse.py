from fastapi.logger import logger
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("uvicorn")


def createWebResp(data: any, code: int = 200):
    web_response = {
        "code": code,
        "data": data,
    }
    # logger.info(webResponse)
    return JSONResponse(content=web_response)


def errorWebResp(error_message: str, error_data: any, code: int = 400):
    web_response = {
        "code": code,
        "message": error_message,
        "errorData": error_data,
    }
    logger.error(web_response)
    return JSONResponse(content=web_response)
