import os
import sys
import json
import configparser

from datetime import date
from binance.client import Client
from helpers import date_to_milliseconds # need helpers.py in the same folder to work

config = configparser.ConfigParser()
config.read('festbot.cfg')

api_key=config['binance']['api_key']
api_secret=config['binance']['api_secret']

client = Client(api_key, api_secret)

index = 0
index_length = 856 #hack for now ... index_length = (len(supported_symbols['symbols'][856]))
supported_symbols = client.get_exchange_info()
list = []

while index < index_length:
    list.append((supported_symbols['symbols'][index]['symbol']))
    index = index + 1

start = "1 Dec, 2017"
end = date.today()
print(end)
interval = Client.KLINE_INTERVAL_1DAY

# get symbol

print("Please enter a supported symbol: ETHBTC, BTCUSDT")
symbol = input()
if symbol not in list:
    print("Exiting .. Not a valid symbol")
    sys.exit()

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

