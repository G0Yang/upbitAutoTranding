from utils.webResponse import create_web_resp, error_web_resp
from upbit.latest.quotation import *
from fastapi import APIRouter

router = APIRouter()


@router.get("/quotation/marketAll", tags=["quotation"])
async def marketAll(isDetails: bool = False):
    try:
        result = await get_market_all(isDetails)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - marketAll", error_data=e.args)


@router.get("/quotation/candles/minutes/{unit}", tags=["quotation"])
async def candlesMinutes(market: str, unit: int, to: str = None, count: int = 1):
    try:
        result = await get_candles_minutes(market, unit, to, count)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - candlesMinutes", error_data=e.args)


@router.get("/quotation/candles/pro/minutes/{unit}", tags=["quotation"])
async def candlesMinutes(market: str, unit: int, count: int = 1):
    try:
        result = await get_candles_minutes_pro(market, unit, count)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - candlesMinutes", error_data=e.args)


@router.get("/quotation/candles/days", tags=["quotation"])
async def candlesDays(market: str, to: str = None, count: int = 1):
    try:
        result = await get_candles_days(market, to, count)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - candlesDays", error_data=e.args)


@router.get("/quotation/candles/weeks", tags=["quotation"])
async def candleWeeks(market: str, to: str = None, count: int = 1):
    try:
        result = await get_candle_weeks(market, to, count)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - candleWeeks", error_data=e.args)


@router.get("/quotation/candles/months", tags=["quotation"])
async def candlesMonths(market: str, to: str = None, count: int = 1):
    try:
        result = await get_candles_months(market, to, count)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - candlesMonths", error_data=e.args)


@router.get("/quotation/tradesTicks", tags=["quotation"])
async def tradesTicks(market: str, to: str = None, count: int = 1, cursor: str = None, daysAgo: int = None):
    try:
        result = await get_trades_ticks(market, to, count, cursor, daysAgo)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - tradesTicks", error_data=e.args)


@router.get("/quotation/ticker", tags=["quotation"])
async def ticker(markets: str):
    try:
        result = await get_ticker(markets)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - ticker", error_data=e.args)


@router.get("/quotation/orderbook", tags=["quotation"])
async def orderbook(markets: str):
    try:
        result = await get_orderbook(markets)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - orderbook", error_data=e.args)
