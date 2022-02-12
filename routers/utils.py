import utils.calc
from utils.webResponse import createWebResp, errorWebResp
from fastapi import APIRouter

router = APIRouter()


@router.get("/utils/get_ma", tags=["utils"])
async def get_ma(peiod: int, data: list) -> bool:
    try:
        return createWebResp(utils.calc.get_ma(peiod, data))
    except Exception as e:
        return errorWebResp(error_message="E0000 - get_ma", error_data=e.args)
