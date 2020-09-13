import os
import sys
import json

from datetime import date
from binance.client import Client
from helpers import date_to_milliseconds # need helpers.py in the same folder to work

client = Client('','') # public api, so leave empty

start = "1 Dec, 2017"
end = "20 Jul, 2020"
interval = Client.KLINE_INTERVAL_1DAY
symbol = "BTCUSDT"

klines = client.get_historical_klines(symbol, interval, start, end)

# open a file with filename including symbol, interval and start and end converted to milliseconds
with open(
    "data/binance_{}_{}_{}-{}.json".format(
        symbol, 
        interval, 
        date_to_milliseconds(start),
        date_to_milliseconds(end)
    ),
    'w' # set file write mode
) as f:
    f.write(json.dumps(klines))

