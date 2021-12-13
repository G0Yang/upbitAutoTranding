import requests
import os
import ast
from datetime import datetime, timedelta
import asyncio

server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']
server_version = os.environ['UPBIT_OPEN_API_VERSION']
base_url = server_url + "/" + server_version

headers = {"Accept": "application/json"}


async def getRequest(method, url, headers, params=None):
    response = requests.request(method, url, headers=headers, params=params)
    return ast.literal_eval(response.text)


# 시세 종목 조회
## 마켓 코드 조회
async def getMarketAll(isDetails=False):
    querystring = {"isDetails": isDetails}
    return await getRequest('GET', base_url + "/market/all", headers, querystring)


# 시세 캔들 조회
## 분 캔들
async def getCandlesMinutes(market, unit=1, to=None, count=1):
    querystring = {
        "market": market,  # "KRW-BTC",
        "to": to,  # "2021-03-11 10:10:10",
        "count": count,  # "1"
    }
    return await getRequest('GET', base_url + "/candles/minutes/" + str(unit), headers, querystring)


async def getCandlesMinutes_pro(market, unit, count):
    if (count <= 0 or unit <= 0):
        return False
    now = datetime.now()
    print("start time", now.strftime("%Y-%m-%d %H:%M:%S"))
    timeStemp = []
    countStamp = []
    MAX_COUNT = 200
    while count > 0:
        if count > MAX_COUNT:
            now = now - timedelta(minutes=unit * MAX_COUNT)
            timeStemp.append(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2021-11-15T07:50:00
            countStamp.append(MAX_COUNT)
            count = count - MAX_COUNT
        elif count == MAX_COUNT:
            countStamp.append(MAX_COUNT)
            count = count - MAX_COUNT
        else:
            now = now - timedelta(minutes=unit * count)
            timeStemp.append(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2021-11-15T07:50:00
            countStamp.append(count)
            count = 0
    promissAll = await asyncio.gather(
        *[getCandlesMinutes(market, unit, timeStemp[i], countStamp[i]) for i in range(0, len(timeStemp))])
    # data = [item for sublist in promissAll for item in sublist]
    # data.sort(key=itemgetter('timestamp'))
    # print(len(data), timeStemp, countStamp)
    # print(timeStemp, countStamp)
    for i in range(0, len(timeStemp)):
        print(timeStemp[i], countStamp[i])
    return promissAll


## 일 캔들
async def getCandlesDays(market, to=None, count=1, convertingPriceUnit=None):
    querystring = {
        "market": market,  # "1",
        "to": to,  # "2",
        "count": count,  # "3",
        "convertingPriceUnit": convertingPriceUnit,  # "4"
    }
    return await getRequest('GET', base_url + "/candles/days", headers, querystring)


## 주 캔들
async def getCandleWeeks(market, to=None, count=1):
    querystring = {
        "market": market,  # "KRW-BTC",
        "to": to,  # "2021-03-11 10:10:10",
        "count": count,  # "1"
    }
    return await getRequest('GET', base_url + "/candles/weeks", headers, querystring)


## 월 캔들
async def getCandlesMonths(market, to=None, count=1):
    querystring = {
        "market": market,  # "KRW-BTC",
        "to": to,  # "2021-03-11 10:10:10",
        "count": count,  # "1"
    }
    return await getRequest('GET', base_url + "/candles/months", headers, querystring)


# 시세 체결 조회
## 최근 체결 내역
async def getTradesTicks(market, to=None, count=1, cursor=None, daysAgo=None):
    querystring = {
        "market": market,
        "to": to,
        "count": count,
        "cursor": cursor,
        "daysAgo": daysAgo,
    }
    return await getRequest('GET', base_url + "/trades/ticks", headers, querystring)


# 시세 Ticker 조회
## 현재가 정보
async def getTicker(markets):
    querystring = {"markets": markets}  # "KRW-BTC, BTC-ETH"
    return await getRequest('GET', base_url + "/ticker", headers, querystring)


# 시세 호가 정보(Orderbook) 조회
## 호가 정보 조회
async def getOrderbook(markets):
    querystring = {"markets": markets}  # ["1","2"]
    return await getRequest('GET', base_url + "/orderbook", headers, querystring)
