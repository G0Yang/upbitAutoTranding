from internal.upbit_exchange import *
from fastapi import APIRouter

router = APIRouter()

@router.get("/exchange/allAccounts", tags=["exchange"])
async def allAccounts(access_key, secret_key):
    result = getAllAccounts(access_key, secret_key)
    return result

@router.get("/exchange/apiKeys", tags=["exchange"])
async def apiKeys(access_key, secret_key):
    result = getApiKeys(access_key, secret_key)
    return result