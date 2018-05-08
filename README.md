# zaif-client

[![PyPI version](https://badge.fury.io/py/zaif-client.svg)](https://badge.fury.io/py/zaif-client) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

zaif-client is a python client (sync/async) library for zaif api

## Installation

    $ pip install zaif-client

## Usage

### Public
```python
#
# sync
#
from zaif_client.public import Public

client = Public(public_key='your key', private_key='your secret key')
response = client.ticker()
print(response.status_code, response.json())

#
# async
#
import grequests
from zaif_client.publicasync import PublicAsync

client = PublicAsync(public_key='your key', private_key='your secret key')
reqs = [client.ticker(), client.depth(), ...]
response = grequests.map(reqs)
for r in response:
	print(r.status_code, r.json())

#
# /currencies/{currency}
#
client.currencies(currency='all')
# [{"name": "btc","is_token": false},{"name": "XCP","is_token": true},...]

#
# /currency_pairs/{currency_pair}
#
client.currency_pairs(currency_pair='all')
# [{"name": "BTC/JPY","title": "BTC/JPY","currency_pair": "btc_jpy","description": "\u30d3\u30c3\u30c8\u30b3\u30a4\u30f3\u30fb\u65e5\u672c\u5186\u306e\u53d6\u5f15\u3092\u884c\u3046\u3053\u3068\u304c\u3067\u304d\u307e\u3059","is_token": false,"event_number": 0,"item_unit_min": 0.0001,"item_unit_step": 0.0001,"aux_unit_min": 5.0,"aux_unit_step": 5.0,"seq": 0,"aux_japanese": "\u65e5\u672c\u5186","item_japanese": "\u30d3\u30c3\u30c8\u30b3\u30a4\u30f3","aux_unit_point": 0,},{"name": "KINOKOUSAKA/JPY","title": "KINOKOUSAKA/JPY \u53d6\u5f15\u6240 - ZAIF Exchange","currency_pair": "kinokousaka_jpy","description": "KINOKOUSAKA/JPY \u53d6\u5f15\u6240\u3002KINOKOUSAKA\u3068\u65e5\u672c\u5186\u306e\u53d6\u5f15\u304c\u884c\u3048\u307e\u3059\u3002","is_token": true,"event_number": 1,"item_unit_min": 0.01,"item_unit_step": 0.01,"aux_unit_min": 0.01,"aux_unit_step": 0.01,"seq": 134,"aux_japanese": "\u65e5\u672c\u5186","item_japanese": "KINOKOUSAKA","aux_unit_point": 2,}...]

#
# /last_price/{currency_pair}
#
client.last_price(currency_pair='btc_jpy')
# {"last_price": 134820.0}

#
# /ticker/{currency_pair}
#
client.ticker(currency_pair='btc_jpy')
# {"last": 135875.0,"high": 136000.0,"low": 131570.0,"vwap": 133301.7489,"volume": 6889.215,"bid": 135875.0,"ask": 135920.0}

#
# /trades/{currency_pair}
#
client.trades(currency_pair='btc_jpy')
# [{"date": 1491756592,"price": 135340.0,"amount": 0.02,"tid": 43054307,"currency_pair": "btc_jpy","trade_type": "ask"},{"date": 1491756591,"price": 135345.0,"amount": 0.01,"tid": 43054306,"currency_pair": "btc_jpy","trade_type": "bid"},...]

#
# /depth/{currency_pair}
#
client.depth(currency_pair='btc_jpy')
# {"asks": [[134875.0,0.0063],[134885.0,0.1639],...],"bids": [[134870.0,0.01],[134865.0,0.3066],...]}
```

### Trade
```python
#
# sync
#
from zaif_client.trade import Trade

client = Trade(public_key='your key', private_key='your secret key')
response = client.get_info()
print(response.status_code, response.json())

#
# async
#
import grequests
from zaif_client.tradeasync import TradeAsync

client = TradeAsync(public_key='your key', private_key='your secret key')
reqs = [client.get_info(), client.get_info2(), ...]
response = grequests.map(reqs)
for r in response:
	print(r.status_code, r.json())

#
# get_info
#
client.get_info()
# {"success":1,"return":{"funds":{"jpy":15320,"btc":1.389,"xem":100.2,"mona":2600,"pepecash":0.1},"deposit":{"jpy":20440,"btc":1.479,"xem":100.2,"mona":3200,"pepecash":0.1},"rights":{"info":1,"trade":1,"withdraw":0,"personal_info":0,"id_info":0,},"trade_count":18,"open_orders":3,"server_time":1401950833}}

#
# get_info2
#
client.get_info2()
# {"success": 1,"return": {"funds": {"jpy": 15320,"btc": 1.389,"xem": 100.2,"mona": 2600,"pepecash": 0.1},"deposit": {"jpy": 20440,"btc": 1.479,"xem": 100.2,"mona": 3200,"pepecash": 0.1},"rights": {"info": 1,"trade": 1,"withdraw": 0,"personal_info": 0},"open_orders": 3,"server_time": 1401950833}

#
# get_personal_info
#
client.get_personal_info()
# {"success": 1,"return": {"ranking_nickname": "ニックネーム","icon_path": "https://abs.twimg.com/sticky/default_profile_images/default_profile_0_normal.png"}}

#
# get_id_info
#
client.get_id_info()
# {'success': 1, 'return': {'user': {'certified': True, 'kana': 'カナ', 'id': 123123, 'name': '氏名', 'email': 'メール'}}}

#
# trade_history
#
client.trade_history()
# {"success": 1,"return": {"182": {"currency_pair": "btc_jpy","action": "bid","amount": 0.03,"price": 56000,"fee": 0,"your_action": "ask","bonus": 1.6,"timestamp": 1402018713,"comment" : "demo"}}}

#
# active_orders
#
client.active_orders()
# {"success": 1,"return": {"184": {"currency_pair": "btc_jpy","action": "ask","amount": 0.03,"price": 56000,"timestamp": 1402021125,"comment" : "demo"}}}is_token_bothがtrueの時は下記{"success": 1,"return": {"active_orders": {"184": {"currency_pair": "btc_jpy","action": "ask","amount": 0.03,"price": 56000,"timestamp": 1402021125,"comment" : "demo"},"token_active_orders": {"235": {"currency_pair": "kaori_jpy","action": "ask","amount": 0.3,"price": 10,"timestamp": 1402064525,"comment" : "demo"}}}}}

#
# trade
#
client.trade(currency_pair='btc_jpy', action='bid', price=1, amount=1)
# {"success": 1,"return": {"received": 0.1,"remains": 0,"order_id": 0,"funds": {"jpy": 325,"btc": 1.392,"mona": 2600}}}

#
# cancel_order
#
client.cancel_order(currency_pair='btc_jpy', order_id=184)
# {"success": 1,"return": {"order_id": 184,"funds": {"jpy": 15320,"btc": 1.392,"mona": 2600,"kaori": 0.1}}}

#
# withdraw
#
client.withdraw(currency='btc', address='xxxxxxx', amount=1)
# {"success": 1,"return": {"id": 23634,"fee": 0.001,"txid":,"funds": {"jpy": 15320,"btc": 1.392,"xem": 100.2,"mona": 2600}}

#
# deposit_history
#
client.deposit_history(currency='jpy')
# {"success":1,"return":{"3816":{"timestamp":1435745065,"address":"12qwQ3sPJJAosodSUhSpMds4WfUPBeFEM2","amount":0.001,"txid":"64dcf59523379ba282ae8cd61d2e9382c7849afe3a3802c0abb08a60067a159f",},"3814":{"timestamp":1435548083,"address":"12qwQ3sPJJAosodSUhSpMds4WfUPBeFEM2","amount":0.001,"txid":"7d012cfff6e67a8938f93215367eef4177604459631ea62c85550980dca71819"},}}

#
# withdraw_history
#
client.withdraw_history(currency='jpy')
# {"success":1,"return":{"3816":{"timestamp":1435745065,"address":"12qwQ3sPJJAosodSUhSpMds4WfUPBeFEM2","amount":0.001,"txid":"64dcf59523379ba282ae8cd61d2e9382c7849afe3a3802c0abb08a60067a159f",},"3814":{"timestamp":1435548083,"address":"12qwQ3sPJJAosodSUhSpMds4WfUPBeFEM2","amount":0.001,"txid":"7d012cfff6e67a8938f93215367eef4177604459631ea62c85550980dca71819"},}}
```

### Futures
```python
#
# sync
#
from zaif_client.futures import Futures

client = Futures(public_key='your key', private_key='your secret key')
response = client.ticker()
print(response.status_code, response.json())

#
# async
#
import grequests
from zaif_client.futuresasync import FuturesAsync

client = FuturesAsync(public_key='your key', private_key='your secret key')
reqs = [client.ticker(), client.depth(), ...]
response = grequests.map(reqs)
for r in response:
	print(r.status_code, r.json())

#
# /groups/{group_id}
#
client.groups(group_id='all')
# [{"id": 1,"currency_pair": "btc_jpy","start_timestamp": 1480518000,"end_timestamp": 4102412399,"use_swap": false},{"id": 2,"currency_pair": "btc_jpy","start_timestamp": 1488294000,"end_timestamp": 1498834800,"use_swap": false}]

#
# /last_price/{group_id}/{currency_pair}
#
client.last_price(group_id='all', currency_pair='btc_jpy')
# [{"last_price": 112155.0, "group_id": 1},{"last_price": 106100.0, "group_id": 2},...]

#
# /ticker/{group_id}/{currency_pair}
#
client.ticker(group_id=1, currency_pair='btc_jpy')
# {"last": 112155.0,"high": 117000.0,"low": 112155.0,"vwap": 115847.1429,"volume": 150.0007,"bid": 116995.0,"ask": 117000.0}

#
# /trades/{group_id}/{currency_pair}
#
client.trades(group_id=1, currency_pair='btc_jpy')
# [{"date": 1491756592,"price": 135340.0,"amount": 0.02,"tid": 102659,"currency_pair": "btc_jpy","trade_type": "ask"},{"date": 1491756591,"price": 135345.0,"amount": 0.01,"tid": 102658,"currency_pair": "btc_jpy","trade_type": "bid"},...]

#
# /depth/{group_id}/{currency_pair}
#
client.depth(group_id=1, currency_pair='btc_jpy')
# {"asks": [[134875.0,0.0063],[134885.0,0.1639],...],"bids": [[134870.0,0.01],[134865.0,0.3066],...]}
```

### Leverage
```python
#
# sync
#
from zaif_client.leverage import Leverage

client = Leverage(public_key='your key', private_key='your secret key')
response = client.ticker()
print(response.status_code, response.json())

#
# async
#
import grequests
from zaif_client.leverageasync import LeverageAsync

client = LeverageAsync(public_key='your key', private_key='your secret key')
reqs = [client.ticker(), client.depth(), ...]
response = grequests.map(reqs)
for r in response:
	print(r.status_code, r.json())

#
# get_positions
#
client.get_positions(group_id=1, type='margin')
# {"success": 1,"return": {"182": {"group_id": 1,"currency_pair": "btc_jpy","action": "bid","leverage": 2.5,"price": 110005,"limit": 130000,"stop": 90000,"amount": 0.03,"fee_spent": 0,"timestamp": 1402018713,"term_end": 1404610713,"timestamp_closed": 1402019000,"deposit": 35.76 ,"deposit_jpy": 35.76,"refunded": 35.76 ,"refunded_jpy": 35.76,"swap": 0,}}}

#
# position_history
#
client.position_history(group_id=1, type='margin', leverage_id=1)
# {"success": 1,"return": {"182": {"group_id": 1,"currency_pair": "btc_jpy","action": "bid","amount": 0.0001,"price": 499000"timestamp": 1504251232"your_action": "bid","bid_leverage_id": 182,},"183": {"group_id": 1,"currency_pair": "btc_jpy","action": "ask","amount": 0.0001,"price": 450000"timestamp": 1504251267"your_action": "ask","ask_leverage_id": 182,},}}

#
# active_positions
#
client.active_positions(group_id=1, type='margin')
# {"success": 1,"return": {"184": {"group_id": "1","currency_pair": "btc_jpy","action": "ask","amount": 0.0001,"price": 450000,"timestamp": 1402021125,"term_end": 1404613125,"leverage": 1,"fee_spent": 0.0015,"price_avg": 450000,"amount_done": 0.0001,"deposit_jpy": 48.72}}}

#
# create_position
#
client.create_position(group_id=1, type='margin', currency_pair='btc_jpy', action='bid', price=1, amount=1, leverage=1)
# {"success": 1,"return": {"leverage_id": 22258,"timestamp": 1504253833,"term_end": 1506845833,"price_avg": 118000,"amount_done": 0.0001,"deposit_jpy": 11.92,"funds": {"jpy": 325,"btc": 1.392,"mona": 2600}}}

#
# change_position
#
client.change_position(group_id=1, type='margin', leverage_id=1, price=1)
# {"success": 1,"return": {"leverage_id": 22258,"price_avg": 118000,"amount_done": 0.0001,}}

#
# cancel_position
#
client.cancel_position(group_id=1, type='margin', leverage_id=1)
# {'success': 1,'return': {'leverage_id': 2072,'refunded_jpy': 645.96,'funds': {'btc': 0.496,'jpy': 1564.96,'xem': 0.0,'mona': 10.0},'fee_spent': 0.0,'timestamp_closed': '1508384951','swap': 0.0}}
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request