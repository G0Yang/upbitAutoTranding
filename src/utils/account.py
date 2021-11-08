from internal.upbit_exchange import *
from internal.upbit_quotation import *

class account:
    def __init__(
        self,
        accessKey: str= None,
        secretKey: str= None,
        totalKrwBalance: int= 0,
        selectedMarkets: list= [],
        availableBalance: int= 0,
        ):
        self._accessKey = accessKey
        self._secretKey = secretKey
        self.totalKrwBalance = totalKrwBalance
        self.selectedMarkets = selectedMarkets
        self.availableBalance = availableBalance

    @property
    def accessKey(self) -> str:
        return self._accessKey

    @accessKey.setter
    def accessKey(self, accessKey: str):
        self._accessKey = accessKey

    @property
    def secretKey(self) -> str:
        return self._secretKey
    
    @secretKey.setter
    def secretKey(self, secretKey: str):
        self._secretKey = secretKey

    def updateTotalKrwBalance(self) -> int:
        allBalance = getAllAccounts(self._accessKey, self._secretKey)
        for balance in allBalance:
            if balance.market is 'KRW':
                return balance.balance