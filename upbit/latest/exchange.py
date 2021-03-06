import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests

server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']
server_version = os.environ['UPBIT_OPEN_API_VERSION']
base_url = server_url + "/" + server_version


async def send_request(method: str, url: str, headers: dict, params=None) -> any:
    response = requests.request(method, url, headers=headers, params=params)
    formed_text = response.text.replace('\"', '\'') \
        .replace('true', 'True') \
        .replace('false', 'False') \
        .replace('null', 'None')
    return eval(formed_text)


def make_jwt_token(access_key: str, secret_key: str, query: bytes = None) -> str:
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


def add_query(query: dict, array) -> str:
    query_string = urlencode(query)
    tx_ids = array
    tx_ids_query_string = '&'.join(["tx_ids[]={}".format(tx_id) for tx_id in tx_ids])
    query['tx_ids[]'] = tx_ids
    return str("{0}&{1}".format(query_string, tx_ids_query_string).encode())


# 자산
## 전체 계좌 조회
async def get_all_accounts(access_key: str, secret_key: str):
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/accounts", headers)


# 주문
## 주문 가능 정보
async def get_order_chance(access_key: str, secret_key: str, market: str):
    query = {
        'market': market,  # 'KRW-ETH'
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/orders/chance", headers, query)


## 개별 주문 조회
async def get_order(access_key: str, secret_key: str, uuid_string: str = None, identifier: str = None):
    if uuid_string == identifier is None:
        return False
    query = {
        'uuid': uuid_string,  # '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',
        'identifier': identifier,
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/order", headers, query)


## 주문 리스트 조회
async def get_orders(access_key: str, secret_key: str, market: str, state: str = 'done', states='done',
                     identifiers: str = None,
                     uuid_array=None, page: int = 1, limit: int = 100, order_by: str = "desc"):
    query = {
        'market': market,
        'state': state,
        'states': states,
        'identifiers': identifiers,
        'page': page,
        'limit': limit,
        'order_by': order_by,
    }
    query_string = add_query(query, uuid_array)
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/orders", headers, query)


## 주문 취소 접수
async def delete_order(access_key: str, secret_key: str, uuid_string: str, identifier=None):
    query = {
        'uuid': uuid_string,  # 'cdd92199-2897-4e14-9448-f923320408ad',
        'identifier': identifier,
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('DELETE', base_url + "/order", headers, query)


## 주문하기
async def post_orders(access_key: str, secret_key: str, market: str, side: str, volume: float, price: float,
                      ord_type: str, identifier: str = None):
    query = {
        'market': market,  # 'KRW-BTC',
        'side': side,  # 'bid',
        'volume': volume,  # '0.01',
        'price': price,  # '100.0',
        'ord_type': ord_type,  # 'limit',
        'identifier': identifier,
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('POST', base_url + "/orders", headers, query)


# 출금
## 출금 리스트 조회
async def get_withdraws(access_key: str, secret_key: str, currency, state: str, txid_array=None, uuid_array=None,
                        limit: int = None, page: int = None, order_by: str = None):
    query = {
        'currency': currency,  # 'XRP',
        'state': state,  # 'done',
        'limit': limit,
        'page': page,
        'order_by': order_by,
    }
    query_string = add_query(query, txid_array)
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/withdraws", headers, query)


## 개별 출금 조회
async def get_withdraw(access_key: str, secret_key: str, uuid_string: str, txid: str = None, currency=None):
    query = {
        'uuid': uuid_string,  # '9f432943-54e0-40b7-825f-b6fec8b42b79'
        'txid': txid,
        'currency': currency,
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/withdraw", headers, query)


## 출금 가능 정보
async def get_withdraws_chance(access_key: str, secret_key: str, currency: str = None):
    query = {
        'currency': currency,  # 'BTC',
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/withdraws/chance", headers, query)


## 코인 출금하기
async def post_withdraw_coin(access_key: str, secret_key: str, currency: str, amount: float, address: str,
                             secondary_address: str = None, transaction_type: str = 'async default'):
    if transaction_type not in ['async default', 'internal']:
        return False
    query = {
        'currency': currency,  # 'BTC',
        'amount': amount,  # '0.01',
        'address': address,  # '3EusRwybuZUhVDeHL7gh3HSLmbhLcy7NqD',
        'secondary_address': secondary_address,
        'transaction_type': transaction_type,
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('POST', base_url + "/withdraws/coin", headers, query)


## 원화 출금하기
async def post_withdraw_krw(access_key: str, secret_key: str, amount: float):
    query = {
        'amount': amount,  # '10000',
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('POST', base_url + "/withdraws/krw", headers, query)


# 입금
## 입금 리스트 조회
async def get_deposits(access_key: str, secret_key: str, currency: str, state: str, txid_array=None, uuid_array=None,
                       limit: int = None, page: int = None, order_by: str = None):
    query = {
        'currency': currency,  # 'XRP',
        'state': state,  # 'done',
        'limit': limit,
        'page': page,
        'order_by': order_by,
    }
    query_string = add_query(query, txid_array)
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/deposits", headers, query)


## 개별 입금 조회
async def get_deposit(access_key: str, secret_key: str, uuid_string: str, txid_string: str = None, currency: str = None):
    query = {
        'uuid': uuid_string,  # '94332e99-3a87-4a35-ad98-28b0c969f830',
        'txid': txid_string,
        'currency': currency,
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/deposit", headers, query)


## 입금 주소 생성 요청
async def post_deposits_generate_coin_address(access_key: str, secret_key: str, base_url: str):
    query = {
        'currency': base_url,  # 'BTC',
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('POST', base_url + "/deposits/generate_coin_address", headers, query)


## 전체 입금 주소 조회
async def get_deposits_coin_addresses(access_key: str, secret_key: str):
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/deposits/coin_addresses", headers)


## 개별 입금 주소 조회
async def get_deposits_coin_address(access_key: str, secret_key: str, currency: str):
    query = {
        'currency': currency,  # 'BTC',
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/deposits/coin_address", headers, query)


## 원화 입금하기
async def post_deposits_krw(access_key: str, secret_key: str, amount: float):
    query = {
        'amount': amount,  # '10000',
    }
    query_string = urlencode(query).encode()
    authorize_token = make_jwt_token(access_key, secret_key, query_string)
    headers = {"Authorization": authorize_token}
    return await send_request('POST', base_url + "/deposits/krw", headers, query)


# 서비스 정보
## 입출금 현황
async def get_status_wallet(access_key: str, secret_key: str):
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/status/wallet", headers)


## API키 리스트 조회
async def get_api_keys(access_key: str, secret_key: str):
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    return await send_request('GET', base_url + "/api_keys", headers)
