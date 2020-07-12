import os
from binance.client import Client
client = Client(api_key, api_secret)

klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
print(os.environ)