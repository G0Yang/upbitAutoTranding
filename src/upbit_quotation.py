import requests
import os

server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']
server_version = os.environ['UPBIT_OPEN_API_VERSION']
base_url = server_url + "/" + server_version

headers = {"Accept": "application/json"}

# 시세 종목 조회
## 마켓 코드 조회
def getMarketAll(isDetails = False):
    url = base_url + "/market/all"
    querystring = {"isDetails": isDetails}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

# 시세 캔들 조회
## 분 캔들
def getCandlesMinutes(market, unit = 1, to = None, count = 1):
    url = base_url + "/candles/minutes/" + unit
    querystring = {
        "market": market, # "KRW-BTC",
        "to": to, # "2021-03-11 10:10:10",
        "count": count, # "1"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

## 일 캔들
def getCandlesDays(market, to = None, count = 1, convertingPriceUnit = None):
    url = base_url + "/candles/days"
    querystring = {
        "market": market, # "1",
        "to": to, # "2",
        "count":count, # "3",
        "convertingPriceUnit": convertingPriceUnit, # "4"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

## 주 캔들
def getCandleWeeks(market, to = None, count = 1):
    url = base_url + "/candles/weeks"
    querystring = {
        "market": market, # "KRW-BTC",
        "to": to, # "2021-03-11 10:10:10",
        "count": count, # "1"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

## 월 캔들
def getCandlesMonths(market, to = None, count = 1):
    url = base_url + "/candles/months"
    querystring = {
        "market": market, # "KRW-BTC",
        "to": to, # "2021-03-11 10:10:10",
        "count": count, # "1"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

# 시세 체결 조회
## 최근 체결 내역
def getTradesTicks(market, to = None, count = 1, cursor = None, daysAgo = None):
    url = base_url + "/trades/ticks"
    querystring = {
        "market": market,
        "to": to,
        "count": count,
        "cursor": cursor,
        "daysAgo": daysAgo,
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

# 시세 Ticker 조회
## 현재가 정보
def getTicker(markets):
    url = base_url + "/ticker"
    querystring = {"markets": markets} # "KRW-BTC, BTC-ETH"
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

# 시세 호가 정보(Orderbook) 조회
## 호가 정보 조회
def getOrderbook(markets):
    url = base_url + "/orderbook"
    querystring = {"markets": markets} # ["1","2"]
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text
