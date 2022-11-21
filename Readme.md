# HackerNotification
## target 
- https://etherscan.io/address/0x59abf3837fa962d6853b4cc0a19513aa031fd32b
## documents
- https://qiita.com/taijusanagi/items/c34d14767feeb3e131a8
scp -i makeLambdaLayer.pem  username@ec2ip:/remote/path/to/file /local/path/to/file
  ec2-13-114-154-191.ap-northeast-1.compute.amazonaws.com

## file transfer
scp -i "makeLambdaLayer.pem" ec2-user@ec2-13-114-154-191.ap-northeast-1.compute.amazonaws.com://home/ec2-user/compornents.zip /Users/iwasakitakashidai/Desktop

# manual Execution
- ソース入れ替えしたときの再実行手順
- todo shell化
```
ssh -i "PythonBot.pem" ec2-user@ec2-18-183-236-166.ap-northeast-1.compute.amazonaws.com
sudo rm -r HackerShort/
sudo rm -r HackerShortApp/
python3 -m venv HackerShortApp/env
source ~/HackerShortApp/env/bin/activate
pip install pip --upgrade
git clone -b prod https://github.com/shoo5123/HackerShort.git
pip install python-binance
cd /home/ec2-user/HackerShort/src
cp /dev/null app_log
nohup python3 /home/ec2-user/HackerShort/src/hacker.py &
```
- トラブル時のコマンド
```
rm -r to\ be\ replaced 
python3 -m venv avgbot_app/env
source ~/avgbot_app/env/bin/activate
pip install pip --upgrade
git clone https://github.com/shoo5123/RangeBot.git
pip install python-binance
```

- ロググループ再セット
- 参考　https://business.ntt-east.co.jp/content/cloudsolution/column-try-28.html
```
sudo systemctl start awslogsd
sudo systemctl status awslogsd
```

- api reference
```
- Python Binance 
  - https://python-binance.readthedocs.io/en/latest/market_data.html
- howTo
  - https://modernimal.com/crypto-how-to-use-binance-api-5751
```
- デバック用コマンド
```
python3
from binance.client import Client
client = Client('7MlQofOjfeh6l4lxtGaqLqr04IAxwimmuqYobvozpBmqipd259dZxxHs1tBVu70a','eIIwHSRH6bpKAlAmAfhVDMjt1pmRopvSp54uC9fVF09PnYmCwS4ye2rwpsfsWOa3')
import json
depth = client.get_order_book(symbol='BNBBTC')
trades = client.get_recent_trades(symbol='BNBBTC')
info = client.get_all_tickers()
print(json.dumps(info, indent=4))
order = client.futures_create_order(symbol="BTCUSDT", side="SELL", type='MARKET', quantity=100)
order = client.futures_create_order(symbol="MATICUSDT", side="SELL", type='MARKET', quantity=6)
order = client.futures_position_information(symbol="MATICUSDT")
```

- 集計用
```
webサイトで取得
https://www.binance.com/ja/my/orders/futures/tradehistory
```


- testnet cmd
```
client = Client(api_key, api_secret, testnet=True)
```


info = client.futures_income_history()
print(json.dumps(info, indent=4))