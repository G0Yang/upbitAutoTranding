from utils.webResponse import createWebResp, errorWebResp
from internal.server import *
from utils.struct import userApiKey
from fastapi import APIRouter
import os

UPBIT_OPEN_API_ACCESS_KEY = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
UPBIT_OPEN_API_SECRET_KEY = os.environ['UPBIT_OPEN_API_SECRET_KEY']
ORDER_FEE_PERCENT = os.environ['ORDER_FEE_PERCENT']

router = APIRouter()

serverd = server(UPBIT_OPEN_API_ACCESS_KEY, UPBIT_OPEN_API_SECRET_KEY, 500, 5, ORDER_FEE_PERCENT, 10)


@router.get("/server/state", tags=["server"])
async def state() -> bool:
    try:
        return createWebResp(serverd.is_alive() or serverd.isRun)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - state", errorData=e.args)


@router.put("/server/markets", tags=["server"])
async def markets(markets: list) -> bool:
    try:
        return createWebResp(serverd.setMarkets(markets))
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - markets", errorData=e.args)


@router.get("/server/start", tags=["server"])
async def start() -> bool:
    try:
        if serverd.isRun:
            return createWebResp("server is already running")
        else:
            serverd.start()
            return createWebResp(True)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - start", errorData=e.args)


@router.get("/server/stop", tags=["server"])
async def stop(timeout: int = 10) -> bool:
    try:
        if not serverd.isRun:
            return createWebResp("server is not running")
        else:
            serverd.stop(timeout)
            return createWebResp(True)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - stop", errorData=e.args)


@router.get("/server/account", tags=["server"])
async def getAccountInfo() -> bool:
    try:
        return serverd.getAccountInfo()
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - getAccountInfo", errorData=e.args)


@router.get("/server/server", tags=["server"])
async def getServerInfo() -> bool:
    try:
        return serverd.getServerInfo()
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - getServerInfo", errorData=e.args)


@router.put("/server/account", tags=["server"])
async def setAccountInfo(keys: userApiKey) -> bool:
    try:
        return serverd.setAccountInfo(keys.access_key, keys.secret_key)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - setAccountInfo", errorData=e.args)
