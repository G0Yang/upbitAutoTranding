import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']
server_version = os.environ['UPBIT_OPEN_API_VERSION']
base_url = server_url + "/" + server_version


def sendRequest(mathod, url, headers, params = None):
    response = requests.request(mathod, url, headers=headers, params=params)
    return response.test

def makeJwtToken(query):
    m = hashlib.sha512()
    m.update(query)
    query_hash = m.hexdigest()
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }
    jwt_token = jwt.encode(payload, secret_key)
    return 'Bearer {}'.format(jwt_token)

def addQuery(query, array):
    query_string = urlencode(query)
    txids = array
    txids_query_string = '&'.join(["txids[]={}".format(txid) for txid in txids])
    query['txids[]'] = txids
    return "{0}&{1}".format(query_string, txids_query_string).encode()

# 자산
## 전체 계좌 조회
def getAllAccounts():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/accounts", headers)

# 주문
## 주문 가능 정보
def getOrderChance(market):
    query = {
        'market': market, # 'KRW-ETH'
    }
    authorize_token = makeJwtToken(query)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/orders/chance", headers, query)

## 개별 주문 조회
def getOrder(uuid_string = None, identifier = None):
    if(uuid_string == identifier == None):
        return False
    query = {
        'uuid': uuid_string, # '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',
        'identifier': identifier,
    }
    authorize_token = makeJwtToken(query)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/order", headers, query)

## 주문 리스트 조회
def getOrders(market, state, states = None, identifiers = None, uuid_array = None, page = None, limit = None, order_by = None):
    query = {
        'market': market,
        'state': state,
        'states': states,
        'identifiers': identifiers,
        'page': page,
        'limit': limit,
        'order_by': order_by,
    }
    query_string = addQuery(query, uuid_array)
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/orders", headers, query)

## 주문 취소 접수
def deleteOrder(uuid_string, identifier = None):
    query = {
        'uuid': uuid_string, # 'cdd92199-2897-4e14-9448-f923320408ad',
        'identifier': identifier,
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('DELETE', base_url + "/order", headers, query)

## 주문하기
def postOrders(market, side, volume, price, ord_type, identifier = None):
    query = {
        'market': market, # 'KRW-BTC',
        'side': side, # 'bid',
        'volume': volume, # '0.01',
        'price': price, # '100.0',
        'ord_type': ord_type, # 'limit',
        'identifier': identifier,
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('POST', base_url + "/orders", headers, query)

# 출금
## 출금 리스트 조회
def getWithdraws(currency, state, txid_array = None, uuid_array = None, limit = None, page = None, order_by = None):
    query = {
        'currency': currency, # 'XRP',
        'state': state, # 'done',
        'limit': limit,
        'page': page,
        'order_by': order_by,
    }
    query_string = addQuery(query, txid_array)
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/withdraws", headers, query)

## 개별 출금 조회
def getWithdraw(uuid_string, txid = None, currency = None):
    query = {
        'uuid': uuid_string, # '9f432943-54e0-40b7-825f-b6fec8b42b79'
        'txid': txid,
        'currency': currency,
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/withdraw", headers, query)

## 출금 가능 정보
def getWithdrawsChance(currency):
    query = {
        'currency': currency, # 'BTC',
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/withdraws/chance", headers, query)

## 코인 출금하기
def postWithdrawCoin(currency, amount, address, secondary_address = None, transaction_type = 'default'):
    if transaction_type not in ['default', 'internal']:
        return False
    query = {
        'currency': currency, #'BTC',
        'amount': amount, # '0.01',
        'address': address, # '3EusRwybuZUhVDeHL7gh3HSLmbhLcy7NqD',
        'secondary_address': secondary_address,
        'transaction_type': transaction_type,
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('POST', base_url + "/withdraws/coin", headers, query)

## 원화 출금하기
def postWithdrawKrw(amount):
    query = {
        'amount': amount, # '10000',
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('POST', base_url + "/withdraws/krw", headers, query)

# 입금
## 입금 리스트 조회
def getDeposits(currency, state, txid_array = None, uuid_array = None, limit = None, page = None, order_by = None):
    query = {
        'currency': currency, # 'XRP',
        'state': state, # 'done',
        'limit': limit,
        'page': page,
        'order_by': order_by,
    }
    query_string = addQuery(query, txid_array)
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/deposits", headers, query)

## 개별 입금 조회
def getDeposit(uuid_string, txid_string = None, currency = None):
    query = {
        'uuid': uuid_string, # '94332e99-3a87-4a35-ad98-28b0c969f830',
        'txid': txid_string,
        'currency': currency,
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/deposit", headers, query)

## 입금 주소 생성 요청
def postDepositsGenerateCoinAddress(base_url):
    query = {
        'currency': base_url, # 'BTC',
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('POST', base_url + "/deposits/generate_coin_address", headers, query)

## 전체 입금 주소 조회
def getDepositsCoinAddresses():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/deposits/coin_addresses", headers, query)

## 개별 입금 주소 조회
def getDepositsCoinAddress(currency):
    query = {
        'currency': currency, # 'BTC',
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/deposits/coin_address", headers, query)

## 원화 입금하기
def postDepositsKrw(amount):
    query = {
        'amount': amount, # '10000',
    }
    query_string = urlencode(query).encode()
    authorize_token = makeJwtToken(query_string)
    headers = {"Authorization": authorize_token}
    return sendRequest('POST', base_url + "/deposits/krw", headers, query)

# 서비스 정보
## 입출금 현황
def getStatusWallet():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/status/wallet", headers, query)

## API키 리스트 조회
def getApiKeys():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    return sendRequest('GET', base_url + "/api_keys", headers, query)
