from threading import Thread
from utils.account import Account
import time
import os


class Server(Thread):
    def __init__(self, access_key: str = None, secret_key: str = None, risk: int = 500, tick_size: int = 1,
                 fee: float = 0.05, min_loss_per: int = 10):
        Thread.__init__(self, target=self.main)

        self.daemon = True  # 프로그램 백그라운드 설정
        self._isRun: bool = False  # 봇 활성화 여부
        self.account: Account = Account(access_key, secret_key)  # 봇 사용자 정보
        self._risk: int = risk  # range(0, 1000) 투자 위험도
        self.tick_size: int = tick_size  # 거래 틱 간격
        self.fee: float = fee  # 거래소 수수료
        self.min_loss_per: int = min_loss_per  # 손해 하한 퍼센트
        self.allMarkets: list = self.account.quotation.getMarketAll(True)  # 투자 가능한 마켓 정보

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
            "tick_size": self.tick_size,
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

    def stop(self, timeout: int = 10):
        self._isRun = False
        self.join(timeout)
        self._stop()

    def main(self):
        self._isRun = True
        number = 0
        while self._isRun:
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

    def setAccountInfo(self, access_key: str, secret_key: str) -> bool:
        self.account.access_key = access_key
        self.account.secret_key = secret_key
        return True

    def getAccountInfo(self) -> dict:
        return {
            "access_key": self.account.access_key,
            "secret_key": self.account.secret_key,
        }
