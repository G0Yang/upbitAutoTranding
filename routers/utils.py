import utils.calc
from utils.webResponse import create_web_resp, error_web_resp
from fastapi import APIRouter

router = APIRouter()


@router.get("/utils/get_ma", tags=["utils"])
async def get_ma(peiod: int, data: list) -> bool:
    try:
        return create_web_resp(utils.calc.get_ma(peiod, data))
    except Exception as e:
        return error_web_resp(error_message="E0000 - get_ma", error_data=e.args)
