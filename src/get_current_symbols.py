from binance.client import Client
import sys
import json
from datetime import date

client = Client('','') # public api, so leave empty

def get_current_symbols():
    index = 0
    index_length = 856 #hack for now, should get length automatically
    list = []
    supported_symbols = client.get_exchange_info()
    while index < index_length:
        list.append((supported_symbols['symbols'][index]['symbol']))
        index = index + 1
    return(list)

current = get_current_symbols()

# write out to json file

f = open("data/binance_symbols.json","w")
f.write(json.dumps(current))
f.close()



