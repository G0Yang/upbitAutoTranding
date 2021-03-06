import upbit.latest.quotation as quotation
import upbit.latest.exchange as exchange


class Account:
    def __init__(
            self,
            access_key: str = None,
            secret_key: str = None,
            total_krw_balance: int = 0,
            selected_markets: list = None,
            available_balance: int = 0,
    ):
        self._accessKey = access_key
        self._secretKey = secret_key
        self.totalKrwBalance = total_krw_balance
        self.selectedMarkets = selected_markets
        self.availableBalance = available_balance
        self.exchange = exchange
        self.quotation = quotation

    @property
    def access_key(self) -> str:
        return self._accessKey

    @access_key.setter
    def access_key(self, access_key: str):
        self._accessKey = access_key

    @property
    def secret_key(self) -> str:
        return self._secretKey

    @secret_key.setter
    def secret_key(self, secret_key: str):
        self._secretKey = secret_key

    def update_total_krw_balance(self) -> int:
        all_balance = exchange.get_all_accounts(self._accessKey, self._secretKey)
        for balance in all_balance:
            if balance.market == 'KRW':
                return balance.balance
        return 0
