from utils.webResponse import createWebResp, errorWebResp
from internal.upbit_quotation import *
from fastapi import APIRouter

router = APIRouter()

@router.get("/quotation/marketAll", tags=["quotation"])
async def marketAll(isDetails: bool = False):
    try:
        result = await getMarketAll(isDetails)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - marketAll", errorData= e.args)
    
@router.get("/quotation/candles/minutes/{unit}", tags=["quotation"])
async def candlesMinutes(market: str, unit: int, to: str = None, count: int = 1):
    try:
        result = await getCandlesMinutes(market, unit, to, count)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - candlesMinutes", errorData= e.args)
    
@router.get("/quotation/candles/pro/minutes/{unit}", tags=["quotation"])
async def candlesMinutes(market: str, unit: int, count: int = 1):
    try:
        result = await getCandlesMinutes_pro(market, unit, count)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - candlesMinutes", errorData= e.args)
    
@router.get("/quotation/candles/days", tags=["quotation"])
async def candlesDays(market: str, to:str = None, count:int = 1):
    try:
        result = await getCandlesDays(market, to, count)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - candlesDays", errorData= e.args)

@router.get("/quotation/candles/weeks", tags=["quotation"])
async def candleWeeks(market: str, to: str = None, count:int = 1):
    try:
        result = await getCandleWeeks(market, to, count)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - candleWeeks", errorData= e.args)

@router.get("/quotation/candles/months", tags=["quotation"])
async def candlesMonths(market: str, to: str = None, count: int = 1):
    try:
        result = await getCandlesMonths(market, to, count)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - candlesMonths", errorData= e.args)
    
@router.get("/quotation/tradesTicks", tags=["quotation"])
async def tradesTicks(market: str, to: str = None, count: int = 1, cursor: str = None, daysAgo: int = None):
    try:
        result = await getTradesTicks(market, to, count, cursor, daysAgo)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - tradesTicks", errorData= e.args)
    
@router.get("/quotation/ticker", tags=["quotation"])
async def ticker(markets: str):
    try:
        result = await getTicker(markets)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - ticker", errorData= e.args)
    
@router.get("/quotation/orderbook", tags=["quotation"])
async def orderbook(markets: str):
    try:
        result = await getOrderbook(markets)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage= "E0000 - orderbook", errorData= e.args)
