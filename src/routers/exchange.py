from src.utils.webResponse import createWebResp, errorWebResp
from src.utils.struct import userApiKey
from src.internal.upbit_exchange import *
from fastapi import APIRouter

router = APIRouter()


@router.get("/exchange/allAccounts", tags=["exchange"])
async def allAccounts(apiKey: userApiKey) -> any:
    try:
        result = await getAllAccounts(apiKey.access_key, apiKey.secret_key)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - allAccounts", errorData=e.args)


@router.get("/exchange/orderChance", tags=["exchange"])
async def orderChance(apiKey: userApiKey, market: str) -> any:
    try:
        result = await getOrderChance(apiKey.access_key, apiKey.secret_key, market)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - orderChance", errorData=e.args)


@router.get("/exchange/order", tags=["exchange"])
async def order(apiKey: userApiKey, uuid_string: str = None, identifier: str = None) -> any:
    try:
        result = await getOrder(apiKey.access_key, apiKey.secret_key, uuid_string, identifier)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - order", errorData=e.args)


@router.get("/exchange/orders", tags=["exchange"])
async def orders(apiKey: userApiKey, market: str, state: str = None, states: list = None, identifiers: str = None,
                 uuid_array: list = None, page: int = None, limit: int = None, order_by: str = None) -> any:
    try:
        result = await getOrders(apiKey.access_key, apiKey.secret_key, market, state, states, identifiers, uuid_array,
                                 page, limit, order_by)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - orders", errorData=e.args)


@router.delete("/exchange/order", tags=["exchange"])
async def order(apiKey: userApiKey, uuid_string: str, identifier: str = None) -> any:
    try:
        result = await deleteOrder(apiKey.access_key, apiKey.secret_key, uuid_string, identifier)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - order", errorData=e.args)


@router.post("/exchange/orders", tags=["exchange"])
async def orders(apiKey: userApiKey, market: str, side: str, volume: float, price: float, ord_type: str,
                 identifier: str = None) -> any:
    try:
        result = await postOrders(apiKey.access_key, apiKey.secret_key, market, side, volume, price, ord_type,
                                  identifier)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - orders", errorData=e.args)


@router.get("/exchange/withdraws", tags=["exchange"])
async def withdraws(apiKey: userApiKey, currency: str, state: str, txid_array: list = None, uuid_array: list = None,
                    limit: int = None, page: int = None, order_by: str = None) -> any:
    try:
        result = await getWithdraws(apiKey.access_key, apiKey.secret_key, currency, state, txid_array, uuid_array,
                                    limit, page, order_by)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - withdraws", errorData=e.args)


@router.get("/exchange/withdraw", tags=["exchange"])
async def withdraw(apiKey: userApiKey, uuid_string: str, txid: str = None, currency: str = None) -> any:
    try:
        result = await getWithdraw(apiKey.access_key, apiKey.secret_key, uuid_string, txid, currency)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - withdraw", errorData=e.args)


@router.get("/exchange/withdrawsChance", tags=["exchange"])
async def withdrawsChance(apiKey: userApiKey, currency: str = None) -> any:
    try:
        result = await getWithdrawsChance(apiKey.access_key, apiKey.secret_key, currency)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - withdrawsChance", errorData=e.args)


@router.post("/exchange/withdrawCoin", tags=["exchange"])
async def withdrawCoin(apiKey: userApiKey, currency: str, amount: float, address: str, secondary_address: str = None,
                       transaction_type: str = 'default') -> any:
    try:
        result = await postWithdrawCoin(apiKey.access_key, apiKey.secret_key, currency, amount, address,
                                        secondary_address, transaction_type)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - withdrawCoin", errorData=e.args)


@router.post("/exchange/withdrawKrw", tags=["exchange"])
async def withdrawKrw(apiKey: userApiKey, amount: float) -> any:
    try:
        result = await postWithdrawKrw(apiKey.access_key, apiKey.secret_key, amount)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - withdrawKrw", errorData=e.args)


@router.get("/exchange/deposits", tags=["exchange"])
async def deposits(apiKey: userApiKey, currency: str, state: str, txid_array: list = None, uuid_array: list = None,
                   limit: int = None, page: int = None, order_by: str = None) -> any:
    try:
        result = await getDeposits(apiKey.access_key, apiKey.secret_key, currency, state, txid_array, uuid_array, limit,
                                   page, order_by)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - deposits", errorData=e.args)


@router.get("/exchange/deposit", tags=["exchange"])
async def deposit(apiKey: userApiKey, uuid_string: str, txid_string: str = None, currency: str = None) -> any:
    try:
        result = await getDeposit(apiKey.access_key, apiKey.secret_key, uuid_string, txid_string, currency)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - deposit", errorData=e.args)


@router.post("/exchange/depositsGenerateCoinAddress", tags=["exchange"])
async def depositsGenerateCoinAddress(apiKey: userApiKey, base_url: str) -> any:
    try:
        result = await postDepositsGenerateCoinAddress(apiKey.access_key, apiKey.secret_key, base_url)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - depositsGenerateCoinAddress", errorData=e.args)


@router.get("/exchange/depositsCoinAddresses", tags=["exchange"])
async def depositsCoinAddresses(apiKey: userApiKey) -> any:
    try:
        result = await getDepositsCoinAddresses(apiKey.access_key, apiKey.secret_key)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - depositsCoinAddresses", errorData=e.args)


@router.get("/exchange/depositsCoinAddress", tags=["exchange"])
async def depositsCoinAddress(apiKey: userApiKey, currency: str = None) -> any:
    try:
        result = await getDepositsCoinAddress(apiKey.access_key, apiKey.secret_key, currency)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - depositsCoinAddress", errorData=e.args)


@router.post("/exchange/depositsKrw", tags=["exchange"])
async def depositsKrw(apiKey: userApiKey, amount: float) -> any:
    try:
        result = await postDepositsKrw(apiKey.access_key, apiKey.secret_key, amount)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - depositsKrw", errorData=e.args)


@router.get("/exchange/statusWallet", tags=["exchange"])
async def statusWallet(apiKey: userApiKey) -> any:
    try:
        result = await getStatusWallet(apiKey.access_key, apiKey.secret_key)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - statusWallet", errorData=e.args)


@router.get("/exchange/apiKeys", tags=["exchange"])
async def apiKeys(apiKey: userApiKey) -> any:
    try:
        result = await getApiKeys(apiKey.access_key, apiKey.secret_key)
        return createWebResp(result)
    except Exception as e:
        return errorWebResp(errorMessage="E0000 - apiKeys", errorData=e.args)
