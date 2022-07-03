from utils.webResponse import create_web_resp, error_web_resp
from utils.struct import UserApiKey
from upbit.latest.exchange import *
from fastapi import APIRouter

router = APIRouter()


@router.post("/exchange/allAccounts", tags=["exchange"])
async def allAccounts(api_kry: UserApiKey) -> any:
    try:
        result = await get_all_accounts(api_kry.access_key, api_kry.secret_key)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - allAccounts", error_data=e.args)


@router.post("/exchange/orderChance", tags=["exchange"])
async def orderChance(api_kry: UserApiKey, market: str) -> any:
    try:
        result = await get_order_chance(api_kry.access_key, api_kry.secret_key, market)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - orderChance", error_data=e.args)


@router.post("/exchange/order", tags=["exchange"])
async def order(api_kry: UserApiKey, uuid_string: str = None, identifier: str = None) -> any:
    try:
        result = await get_order(api_kry.access_key, api_kry.secret_key, uuid_string, identifier)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - order", error_data=e.args)


@router.post("/exchange/getOrders", tags=["exchange"])
async def get_orders(api_kry: UserApiKey, market: str = None, state: str = None, states: list = None,
                     identifiers: str = None,
                     uuid_array: list = None, page: int = None, limit: int = None, order_by: str = None) -> any:
    try:
        result = await get_orders(api_kry.access_key, api_kry.secret_key, market, state, states, identifiers, uuid_array,
                                  page, limit, order_by)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - get_orders", error_data=e.args)


@router.delete("/exchange/order", tags=["exchange"])
async def order(api_kry: UserApiKey, uuid_string: str, identifier: str = None) -> any:
    try:
        result = await delete_order(api_kry.access_key, api_kry.secret_key, uuid_string, identifier)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - order", error_data=e.args)


@router.post("/exchange/orders", tags=["exchange"])
async def orders(api_kry: UserApiKey, market: str, side: str, volume: float, price: float, ord_type: str,
                 identifier: str = None) -> any:
    try:
        result = await post_orders(api_kry.access_key, api_kry.secret_key, market, side, volume, price, ord_type,
                                   identifier)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - orders", error_data=e.args)


@router.post("/exchange/withdraws", tags=["exchange"])
async def withdraws(api_kry: UserApiKey, currency: str, state: str, txid_array: list = None, uuid_array: list = None,
                    limit: int = None, page: int = None, order_by: str = None) -> any:
    try:
        result = await get_withdraws(api_kry.access_key, api_kry.secret_key, currency, state, txid_array, uuid_array,
                                     limit, page, order_by)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - withdraws", error_data=e.args)


@router.post("/exchange/withdraw", tags=["exchange"])
async def withdraw(api_kry: UserApiKey, uuid_string: str, txid: str = None, currency: str = None) -> any:
    try:
        result = await get_withdraw(api_kry.access_key, api_kry.secret_key, uuid_string, txid, currency)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - withdraw", error_data=e.args)


@router.post("/exchange/withdrawsChance", tags=["exchange"])
async def withdrawsChance(api_kry: UserApiKey, currency: str = None) -> any:
    try:
        result = await get_withdraws_chance(api_kry.access_key, api_kry.secret_key, currency)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - withdrawsChance", error_data=e.args)


@router.post("/exchange/withdrawCoin", tags=["exchange"])
async def withdrawCoin(api_kry: UserApiKey, currency: str, amount: float, address: str, secondary_address: str = None,
                       transaction_type: str = 'default') -> any:
    try:
        result = await post_withdraw_coin(api_kry.access_key, api_kry.secret_key, currency, amount, address,
                                          secondary_address, transaction_type)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - withdrawCoin", error_data=e.args)


@router.post("/exchange/withdrawKrw", tags=["exchange"])
async def withdrawKrw(api_kry: UserApiKey, amount: float) -> any:
    try:
        result = await post_withdraw_krw(api_kry.access_key, api_kry.secret_key, amount)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - withdrawKrw", error_data=e.args)


@router.post("/exchange/deposits", tags=["exchange"])
async def deposits(api_kry: UserApiKey, currency: str, state: str, txid_array: list = None, uuid_array: list = None,
                   limit: int = None, page: int = None, order_by: str = None) -> any:
    try:
        result = await get_deposits(api_kry.access_key, api_kry.secret_key, currency, state, txid_array, uuid_array,
                                    limit,
                                    page, order_by)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - deposits", error_data=e.args)


@router.post("/exchange/deposit", tags=["exchange"])
async def deposit(api_kry: UserApiKey, uuid_string: str, txid_string: str = None, currency: str = None) -> any:
    try:
        result = await get_deposit(api_kry.access_key, api_kry.secret_key, uuid_string, txid_string, currency)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - deposit", error_data=e.args)


@router.post("/exchange/depositsGenerateCoinAddress", tags=["exchange"])
async def depositsGenerateCoinAddress(api_kry: UserApiKey, base_url: str) -> any:
    try:
        result = await post_deposits_generate_coin_address(api_kry.access_key, api_kry.secret_key, base_url)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - depositsGenerateCoinAddress", error_data=e.args)


@router.post("/exchange/depositsCoinAddresses", tags=["exchange"])
async def depositsCoinAddresses(api_kry: UserApiKey) -> any:
    try:
        result = await get_deposits_coin_addresses(api_kry.access_key, api_kry.secret_key)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - depositsCoinAddresses", error_data=e.args)


@router.post("/exchange/depositsCoinAddress", tags=["exchange"])
async def depositsCoinAddress(api_kry: UserApiKey, currency: str = None) -> any:
    try:
        result = await get_deposits_coin_address(api_kry.access_key, api_kry.secret_key, currency)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - depositsCoinAddress", error_data=e.args)


@router.post("/exchange/depositsKrw", tags=["exchange"])
async def depositsKrw(api_kry: UserApiKey, amount: float) -> any:
    try:
        result = await post_deposits_krw(api_kry.access_key, api_kry.secret_key, amount)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - depositsKrw", error_data=e.args)


@router.post("/exchange/statusWallet", tags=["exchange"])
async def statusWallet(api_kry: UserApiKey) -> any:
    try:
        result = await get_status_wallet(api_kry.access_key, api_kry.secret_key)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - statusWallet", error_data=e.args)


@router.post("/exchange/api_krys", tags=["exchange"])
async def api_krys(api_kry: UserApiKey) -> any:
    try:
        result = await get_api_keys(api_kry.access_key, api_kry.secret_key)
        return create_web_resp(result)
    except Exception as e:
        return error_web_resp(error_message="E0000 - api_krys", error_data=e.args)
