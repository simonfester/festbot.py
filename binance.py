# historical.py to get historical data from Binance

from datetime import datetime
import requests                     # https://requests.readthedocs.io/en/master/user/quickstart/
import json

timeout = 10 # for the request request

# required kline values
symbol = 'BTCUSDT'
interval = '1d'
start_time = 0    # start time in ms
limit = 1

# params for our request

payload = {'symbol': symbol, 'interval': interval, 'limit': limit, 'startTime': start_time}


# urls
base_url = 'https://api.binance.com'   # base url, all others start from here
get_ping = '/api/v3/ping'              # ping endpoint
get_time = '/api/v3/time'              # server time
get_klines = '/api/v3/klines'          # kline endpoint

# function to check if the server is connected

def are_we_connected():
     ping = requests.get(base_url+get_ping)
     if '{}' in ping.text:
         print('Connected')
     else:
         print('Error not connected')

# function to get server time 

def get_server_time():
     time = requests.get(base_url + get_time)
     time_dict = time.json()
     server_time_in_ms = (time_dict['serverTime'])
     return datetime.fromtimestamp(server_time_in_ms / 1000)

# get symbol start time

def get_symbol_start_time():
     r = requests.get(base_url+get_klines, params = payload, timeout = timeout)
     return r.text[0][0]

print(get_symbol_start_time())

# kline json return structure

#  1499040000000,      // Open time
#  "0.01634790",       // Open
#  "0.80000000",       // High
#  "0.01575800",       // Low
#  "0.01577100",       // Close
#  "148976.11427815",  // Volume
#  1499644799999,      // Close time
#  "2434.19055334",    // Quote asset volume
#  308,                // Number of trades
#  "1756.87402397",    // Taker buy base asset volume
#  "28.46694368",      // Taker buy quote asset volume
#  "17928899.62484339" // Ignore. 