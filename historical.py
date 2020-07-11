# historical.py to get historical data from Binance

from datetime import datetime

# https://requests.readthedocs.io/en/master/user/quickstart/
import requests

# symbol we are using
symbol = 'BTCUSDT'

# required kline interval
interval = '1d'

# start time in ms
start_time = 0
limit = 1

# base url
base_url = 'https://api.binance.com'

# ping endpoint
get_ping = '/api/v3/ping'

# server time
get_time = '/api/v3/time'

# kline endpoint
get_klines = '/api/v3/klines'


# check server is connected
ping = requests.get(base_url+get_ping)
if '{}' in ping.text:
    print('Connected')
else:
    print('Error not connected')

# request server time, convert to dictionary and then print
time = requests.get(base_url+get_time)
time_dict = time.json()
server_time_in_ms = (time_dict['serverTime'])
date = datetime.fromtimestamp(server_time_in_ms / 1000)
print('Server Time: ',date)

# get klines
klines = requests.get(base_url+get_klines, params={'symbol': symbol, 'interval': interval, 'limit': limit, 'startTime': start_time})
print(klines.text)

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