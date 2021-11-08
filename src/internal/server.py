from threading import Thread

from uvicorn.main import main 
from internal.upbit_exchange import *
from internal.upbit_quotation import *
from utils.account import account

import time

class server(Thread):
    def __init__(self, accessKey: str= None, secretKey: str= None):
        Thread.__init__(self, target= self.main)
        self.daemon= True
        self._isRun: bool= False
        self.account: account= account(accessKey, secretKey)
        self._risk: int= 500 # range(0, 1000)
        self.allMarkets: list= getMarketAll(True)
	
    @property
    def isRun(self) -> bool:
        return self._isRun

    @property
    def risk(self) -> int:
        return self._risk

    @risk.setter
    def risk(self, risk: int):
        self._risk = risk

    def stop(self, timeout: int= 10):
        self._isRun = False
        self.join(timeout)
        self._stop()

    def main(self):
        self._isRun = True
        number = 0
        while(self._isRun):
            print(number)
            number = number + 1
            time.sleep(1)
    
    def setMarkets(self, markets: list) -> list:
        marketFailed = False
        for market in markets:
            if market not in self.allMarkets:
                marketFailed = True
        if marketFailed:
            self.account.selectedMarkets = markets
        else: 
            self.account.selectedMarkets = []
        return self.account.selectedMarkets

    def setAvailableBalance(self, balance) -> int:
        if self.account.totalKrwBalance < balance:
            balance = self.account.totalKrwBalance
        self.account.availableBalance = balance
        return self.account.availableBalance
