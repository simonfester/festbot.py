from binance.client import Client
client = Client('','')

#hack for now ... index_length = (len(supported_symbols['symbols'][856]))

def get_current_symbols():
    index = 0
    index_length = 856 
    list = []
    supported_symbols = client.get_exchange_info()
    while index < index_length:
        list.append((supported_symbols['symbols'][index]['symbol']))
        index = index + 1
    return(list)

current = get_current_symbols()
print(current)



