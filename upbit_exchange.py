import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

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

    res = requests.get(server_url + "/v1/accounts", headers=headers)
    return res.json()

# 주문
## 주문 가능 정보
def getOrderChance(market):
    query = {
        'market': market, # 'KRW-ETH'
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/orders/chance", params=query, headers=headers)
    return res.json()

## 개별 주문 조회
def getOrder(uuid_string):
    query = {
        'uuid': uuid_string, # '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/order", params=query, headers=headers)
    return res.json()

## 주문 리스트 조회

## 주문 취소 접수
## 주문하기

# 출금
## 출금 리스트 조회
## 개별 출금 조회
## 출금 가능 정보
## 코인 출금하기
## 원화 출금하기

# 입금
## 입금 리스트 조회
## 개별 입금 조회
## 입금 주소 생성 요청
## 전체 입금 주소 조회
## 개별 입금 주소 조회
## 원화 입금하기

# 서비스 정보
## 입출금 현황
## API키 리스트 조회
