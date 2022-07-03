# from fastapi.logger import logger
from fastapi.responses import JSONResponse
import logging

local_logger = logging.getLogger("uvicorn")


def create_web_resp(data: any, code: int = 200):
    web_response = {
        "code": code,
        "data": data,
    }
    local_logger.debug(web_response)
    return JSONResponse(content=web_response)


def error_web_resp(error_message: str, error_data: any, code: int = 400):
    web_response = {
        "code": code,
        "message": error_message,
        "errorData": error_data,
    }
    local_logger.error(web_response)
    return JSONResponse(content=web_response)
