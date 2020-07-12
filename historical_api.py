import os
import json
from binance.client import Client
from dotenv import load_dotenv
from helpers import date_to_milliseconds


project_folder = os.path.expanduser('~/pyhton')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")

client = Client(api_key, api_secret)

symbol = "ETHBTC"
start = "1 Dec, 2017"
end = "1 Jan, 2020"
interval = Client.KLINE_INTERVAL_30MINUTE

klines = client.get_historical_klines(symbol, interval, start, end)

# open a file with filename including symbol, interval and start and end converted to milliseconds
with open(
    "Binance_{}_{}_{}-{}.json".format(
        symbol, 
        interval, 
        date_to_milliseconds(start),
        date_to_milliseconds(end)
    ),
    'w' # set file write mode
) as f:
    f.write(json.dumps(klines))

