import requests
import time
import json
from logging import getLogger, config

# layer import
from binance.client import Client
from binance.exceptions import BinanceAPIException

apikey = "KETZFRQWRCBE7NYNEYTI1IEW1D87R3KHJI"
target_address = "0x59abf3837fa962d6853b4cc0a19513aa031fd32b"
url = "https://api.etherscan.io/api"
urls = "https://api.etherscan.io/api?" \
       "module=account" \
       "&action=txlist" \
       "&address=0x59abf3837fa962d6853b4cc0a19513aa031fd32b" \
       "&startblock=0" \
       "&endblock=99999999" \
       "&page=1" \
       "&offset=10" \
       "&sort=desc" \
       "&apikey=KETZFRQWRCBE7NYNEYTI1IEW1D87R3KHJI"
API_KEY = "zCXiJnbeCce3tToi15KOrveechtKvMVegyDH8eNNCB7F3cCT3vLefNnlDjvZEtm1"
SECRET_KEY = "kcuPiq5gzTDeuHhW9SLgPzFqjp6iVIDGEm2TNtSeU7TY7M7S6BgsNDJ8vcVN6UBp"

# client
binance = Client(API_KEY, SECRET_KEY, {"timeout": 20})
ticker = 'ETH'  # 取引対象
currency = 'BUSD'  # USDT建て
symbol = ticker + currency
side = Client.SIDE_SELL
type = "MARKET"
quantity = 10

# log instance
with open('./log_config.json', 'r') as f:
    log_conf = json.load(f)
config.dictConfig(log_conf)
logger = getLogger(__name__)


def main():
    logger.info("batch start")

    while True:
        # ethscan api実行
        res = requests.get(urls).json().get("result")

        # 1eth以上のトランスファーをチェック
        for t in res:
            if (int(t.get('value')) / 1000000000000000000) > 1:
                logger.info("鯨がうごきました")
                logger.info("https://etherscan.io/address/0x59abf3837fa962d6853b4cc0a19513aa031fd32b")
                create_short_entry(symbol, side, type, quantity)
        logger.info("まだ鯨は動いてないよ")
        # 1min おきに実行
        time.sleep(60)


def create_short_entry(sym, si, ty, qua):
    logger.info("entry short")
    try:
        binance.futures_create_order(symbol=sym, side=si, type=ty, quantity=qua)
    except BinanceAPIException as e:
        logger.error("short注文に失敗しました")
        logger.error(e.status_code)
        logger.error(e.message)


# local 動作確認用
if __name__ == '__main__':
    main()