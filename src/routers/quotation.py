from internal.upbit_quotation import *
from fastapi import APIRouter

router = APIRouter()

@router.get("/quotation/marketAll", tags=["quotation"])
async def marketAll(isDetails: bool = False):
    result = getMarketAll(isDetails)
    return result
    
@router.get("/quotation/candles/minutes/{unit}", tags=["quotation"])
async def candlesMinutes(market: str, unit: int, to: str = None, count: int = 1):
    result = getCandlesMinutes(market, unit, to, count)
    return result
    
@router.get("/quotation/candles/days", tags=["quotation"])
async def candlesDays(market: str, to:str = None, count:int = 1):
    result = getCandlesDays(market, to, count)
    return result

@router.get("/quotation/candles/weeks", tags=["quotation"])
async def candleWeeks(market: str, to: str = None, count:int = 1):
    result = getCandleWeeks(market, to, count)
    return result

@router.get("/quotation/candles/months", tags=["quotation"])
async def candlesMonths(market: str, to: str = None, count: int = 1):
    result = getCandlesMonths(market, to, count)
    return result
    
@router.get("/quotation/tradesTicks", tags=["quotation"])
async def tradesTicks(market: str, to: str = None, count: int = 1, cursor: str = None, daysAgo: int = None):
    result = getTradesTicks(market, to, count, cursor, daysAgo)
    return result
    
@router.get("/quotation/ticker", tags=["quotation"])
async def ticker(markets: str):
    result = getTicker(markets)
    return result
    
@router.get("/quotation/orderbook", tags=["quotation"])
async def orderbook(markets: str):
    result = getOrderbook(markets)
    return result