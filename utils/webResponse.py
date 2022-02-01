from fastapi.logger import logger
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("uvicorn")


def createWebResp(data: any, code: int = 200):
    webResponse = {
        "code": code,
        "data": data,
    }
    # logger.info(webResponse)
    return JSONResponse(content=webResponse)


def errorWebResp(errorMessage: str, errorData: any, code: int = 400):
    webResponse = {
        "code": code,
        "message": errorMessage,
        "errorData": errorData,
    }
    logger.error(webResponse)
    return JSONResponse(content=webResponse)
