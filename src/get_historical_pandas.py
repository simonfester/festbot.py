import os
import sys
import json
import pandas as pd
import numpy as np 

from datetime import date
from binance.client import Client

# need helpers.py in the same folder to work
from helpers import date_to_milliseconds 

# public api, so leave api_key and secret empty
client = Client('','')
from time import time
time_now_in_ms = int(time() * 1000) 

# options for request
start = "1 Dec, 2017" # binance opening time
end = time_now_in_ms
interval = Client.KLINE_INTERVAL_1HOUR
symbol = "ETHUSDT"

# get the data from the api
data = client.get_historical_klines(symbol, interval, start, end)
df = pd.DataFrame(data) 

# format columns with human names
df.rename(columns={0: 'open_time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'vol', 6: 'close_time', 7: 'asset_vol', 8: 'num_trades', 9: 'taker_buy', 10: 'taker_quote', 11: 'ignore'})
print(df.head)

file_name = 'binance_' + symbol + '_' + interval +'.h5'
# write data to pandas h5 frame
h5 = pd.HDFStore('data/'+file_name, 'w')
h5['data'] = df
h5.close()



