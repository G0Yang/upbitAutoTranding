from threading import Thread
#from uvicorn.main import main 
from utils.account import account
import time
import os

class server(Thread):
    def __init__(self, accessKey: str= None, secretKey: str= None, risk: int= 500, tickSize: int=1, fee: float=0.05, MinlossPer: int= 10):
        Thread.__init__(self, target= self.main)
        
        self.daemon= True # 프로그램 백그라운드 설정
        self._isRun: bool= False # 봇 활성화 여부
        self.account: account= account(accessKey, secretKey) # 봇 사용자 정보
        self._risk: int= risk # range(0, 1000) 투자 위험도
        self.tickSize: int= tickSize # 거래 틱 간격
        self.fee: float= fee # 거래소 수수료
        self.MinlossPer: int= MinlossPer # 손해 하한 퍼센트
        self.allMarkets: list= self.account.Quotation.getMarketAll(True) # 투자 가능한 마켓 정보

        self.EXCHANGE_LIMIT_ORDER_PER_SECOND = os.environ['EXCHANGE_LIMIT_ORDER_PER_SECOND']
        self.EXCHANGE_LIMIT_ORDER_PER_MINUTE = os.environ['EXCHANGE_LIMIT_ORDER_PER_MINUTE']
        self.EXCHANGE_LIMIT_NOT_ORDER_PER_SECOND = os.environ['EXCHANGE_LIMIT_NOT_ORDER_PER_SECOND']
        self.EXCHANGE_LIMIT_NOT_ORDER_PER_MINUTE = os.environ['EXCHANGE_LIMIT_NOT_ORDER_PER_MINUTE']
        self.QUOTATION_LIMIT_WS_PER_SECOND = os.environ['QUOTATION_LIMIT_WS_PER_SECOND']
        self.QUOTATION_LIMIT_WS_PER_MINUTE = os.environ['QUOTATION_LIMIT_WS_PER_MINUTE']
        self.QUOTATION_LIMIT_REST_API_PER_SECOND = os.environ['QUOTATION_LIMIT_REST_API_PER_SECOND']
        self.QUOTATION_LIMIT_REST_API_PER_MINUTE = os.environ['QUOTATION_LIMIT_REST_API_PER_MINUTE']
        self.MINIMAL_ORDER_PRICE = os.environ['MINIMAL_ORDER_PRICE']


    def getServerInfo(self):
        return {
            "daemon": self.daemon,
            "isRun": self.isRun,
            "_risk": self._risk,
            "tickSize": self.tickSize,
            "fee": self.fee,
        }
	
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

    def setAvailableBalance(self, balance: int) -> int:
        if self.account.totalKrwBalance < balance:
            balance = self.account.totalKrwBalance
        self.account.availableBalance = balance
        return self.account.availableBalance

    def setAccountInfo(self, accessKey: str, secretKey: str) -> bool:
        self.account.accessKey = accessKey
        self.account.secretKey = secretKey
        return True

    def getAccountInfo(self) -> dict:
        return {
            "accessKey": self.account.accessKey,
            "secretKey": self.account.secretKey,
        }