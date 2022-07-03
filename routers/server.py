from utils.webResponse import create_web_resp, error_web_resp
from internal.server import *
from utils.struct import UserApiKey
from fastapi import APIRouter
import os

UPBIT_OPEN_API_ACCESS_KEY = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
UPBIT_OPEN_API_SECRET_KEY = os.environ['UPBIT_OPEN_API_SECRET_KEY']
ORDER_FEE_PERCENT = os.environ['ORDER_FEE_PERCENT']

router = APIRouter()

serverd = Server(UPBIT_OPEN_API_ACCESS_KEY, UPBIT_OPEN_API_SECRET_KEY, 500, 5, ORDER_FEE_PERCENT, 10)


@router.get("/server/state", tags=["server"])
async def state() -> bool:
    try:
        return create_web_resp(serverd.is_alive() or serverd.isRun)
    except Exception as e:
        return error_web_resp(error_message="E0000 - state", error_data=e.args)


@router.put("/server/markets", tags=["server"])
async def markets(markets: list) -> bool:
    try:
        return create_web_resp(serverd.setMarkets(markets))
    except Exception as e:
        return error_web_resp(error_message="E0000 - markets", error_data=e.args)


@router.get("/server/start", tags=["server"])
async def start() -> bool:
    try:
        if serverd.isRun:
            return create_web_resp("server is already running")
        else:
            serverd.start()
            return create_web_resp(True)
    except Exception as e:
        return error_web_resp(error_message="E0000 - start", error_data=e.args)


@router.get("/server/stop", tags=["server"])
async def stop(timeout: int = 10) -> bool:
    try:
        if not serverd.isRun:
            return create_web_resp("server is not running")
        else:
            serverd.stop(timeout)
            return create_web_resp(True)
    except Exception as e:
        return error_web_resp(error_message="E0000 - stop", error_data=e.args)


@router.get("/server/account", tags=["server"])
async def get_account_info() -> bool:
    try:
        return serverd.getAccountInfo()
    except Exception as e:
        return error_web_resp(error_message="E0000 - getAccountInfo", error_data=e.args)


@router.get("/server/server", tags=["server"])
async def get_server_info() -> bool:
    try:
        return serverd.getServerInfo()
    except Exception as e:
        return error_web_resp(error_message="E0000 - getServerInfo", error_data=e.args)


@router.put("/server/account", tags=["server"])
async def set_account_info(keys: UserApiKey) -> bool:
    try:
        return serverd.setAccountInfo(keys.access_key, keys.secret_key)
    except Exception as e:
        return error_web_resp(error_message="E0000 - setAccountInfo", error_data=e.args)
