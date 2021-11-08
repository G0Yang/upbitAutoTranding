from utils.webResponse import *
from internal.server import *
from fastapi import APIRouter

router = APIRouter()

serverd = server()

@router.get("/server/state", tags=["server"])
async def state() -> bool:
    try:
        return createWebResp(serverd.is_alive() or serverd.isRun)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - state", errorData= e.args)

@router.put("/server/markets", tags=["server"])
async def markets(markets: list) -> bool:
    try:
        return createWebResp(serverd.setMarkets(markets))
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - markets", errorData= e.args)

@router.get("/server/start", tags=["server"])
async def start() -> bool:
    try:
        if serverd.isRun:
            return createWebResp("server is already running")
        else:
            serverd.start()
            return createWebResp(True)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - start", errorData= e.args)

@router.get("/server/stop", tags=["server"])
async def stop(timeout: int= 10) -> bool:
    try:
        if not serverd.isRun:
            return createWebResp("server is not running")
        else:
            serverd.stop(timeout)
            return createWebResp(True)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - stop", errorData= e.args)

