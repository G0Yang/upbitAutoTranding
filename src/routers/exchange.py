from logging import error
from pydantic import errors
from utils.webResponse import *
from internal.upbit_exchange import *
from fastapi.logger import logger
from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/exchange/allAccounts", tags=["exchange"])
async def allAccounts(apiKey: userApiKey) -> any:
    try:
        result = getAllAccounts(apiKey.access_key, apiKey.secret_key)
        return createWebResp(result)
    except:
        return errorWebResp(errorMessage= "E0000 - allAccounts", errorData= None)

@router.get("/exchange/orderChance", tags=["exchange"])
async def orderChance(apiKey: userApiKey, market: str) -> any:
    result = getOrderChance(apiKey.access_key, apiKey.secret_key, market)
    return result

@router.get("/exchange/order", tags=["exchange"])
async def order(apiKey: userApiKey, uuid_string: str = None, identifier: str = None) -> any:
    result = getOrder(apiKey.access_key, apiKey.secret_key, uuid_string, identifier)
    return result

@router.get("/exchange/orders", tags=["exchange"])
async def orders(apiKey: userApiKey, market: str, state: str = None, states: list = None, identifiers: str = None, uuid_array: list = None, page: int = None, limit: int = None, order_by: str = None) -> any:
    result = getOrders(apiKey.access_key, apiKey.secret_key, market, state, states, identifiers, uuid_array, page, limit, order_by)
    return result

@router.delete("/exchange/order", tags=["exchange"])
async def order(apiKey: userApiKey, uuid_string: str, identifier: str = None) -> any:
    result = deleteOrder(apiKey.access_key, apiKey.secret_key, uuid_string, identifier)
    return result

@router.post("/exchange/orders", tags=["exchange"])
async def orders(apiKey: userApiKey, market: str, side: str, volume: float, price: float, ord_type: str, identifier: str = None) -> any:
    result = postOrders(apiKey.access_key, apiKey.secret_key, market, side, volume, price, ord_type, identifier)
    return result

@router.get("/exchange/withdraws", tags=["exchange"])
async def withdraws(apiKey: userApiKey, currency: str, state: str, txid_array: list = None, uuid_array: list = None, limit: int = None, page: int = None, order_by: str = None) -> any:
    result = getWithdraws(apiKey.access_key, apiKey.secret_key, currency, state, txid_array, uuid_array, limit , page, order_by)
    return result

@router.get("/exchange/withdraw", tags=["exchange"])
async def withdraw(apiKey: userApiKey,  uuid_string: str, txid: str = None, currency: str = None) -> any:
    result = getWithdraw(apiKey.access_key, apiKey.secret_key, uuid_string, txid, currency)
    return result

@router.get("/exchange/withdrawsChance", tags=["exchange"])
async def withdrawsChance(apiKey: userApiKey, currency: str = None) -> any:
    result = getWithdrawsChance(apiKey.access_key, apiKey.secret_key, currency)
    return result

@router.post("/exchange/withdrawCoin", tags=["exchange"])
async def withdrawCoin(apiKey: userApiKey, currency: str, amount: float, address: str, secondary_address: str = None, transaction_type: str = 'default') -> any:
    result = postWithdrawCoin(apiKey.access_key, apiKey.secret_key, currency, amount, address, secondary_address, transaction_type)
    return result

@router.post("/exchange/withdrawKrw", tags=["exchange"])
async def withdrawKrw(apiKey: userApiKey, amount: float) -> any:
    result = postWithdrawKrw(apiKey.access_key, apiKey.secret_key, amount)
    return result

@router.get("/exchange/deposits", tags=["exchange"])
async def deposits(apiKey: userApiKey, currency: str, state: str, txid_array: list = None, uuid_array: list = None, limit: int = None, page: int = None, order_by: str = None) -> any:
    result = getDeposits(apiKey.access_key, apiKey.secret_key, currency, state, txid_array, uuid_array, limit, page, order_by)
    return result

@router.get("/exchange/deposit", tags=["exchange"])
async def deposit(apiKey: userApiKey, uuid_string: str, txid_string: str = None, currency: str = None) -> any:
    result = getDeposit(apiKey.access_key, apiKey.secret_key, uuid_string, txid_string, currency)
    return result

@router.post("/exchange/depositsGenerateCoinAddress", tags=["exchange"])
async def depositsGenerateCoinAddress(apiKey: userApiKey, base_url: str) -> any:
    result = postDepositsGenerateCoinAddress(apiKey.access_key, apiKey.secret_key, base_url)
    return result

@router.get("/exchange/depositsCoinAddresses", tags=["exchange"])
async def depositsCoinAddresses(apiKey: userApiKey) -> any:
    result = getDepositsCoinAddresses(apiKey.access_key, apiKey.secret_key)
    return result

@router.get("/exchange/depositsCoinAddress", tags=["exchange"])
async def depositsCoinAddress(apiKey: userApiKey, currency: str = None) -> any:
    result = getDepositsCoinAddress(apiKey.access_key, apiKey.secret_key, currency)
    return result

@router.post("/exchange/depositsKrw", tags=["exchange"])
async def depositsKrw(apiKey: userApiKey, amount: float) -> any:
    result = postDepositsKrw(apiKey.access_key, apiKey.secret_key, amount)
    return result

@router.get("/exchange/statusWallet", tags=["exchange"])
async def statusWallet(apiKey: userApiKey) -> any:
    result = getStatusWallet(apiKey.access_key, apiKey.secret_key)
    return result

@router.get("/exchange/apiKeys", tags=["exchange"])
async def apiKeys(apiKey: userApiKey) -> any:
    result = getApiKeys(apiKey.access_key, apiKey.secret_key)
    return result