import configparser
import quandl as q
import pandas as pd
config = configparser.ConfigParser()
config.read('festbot.cfg')

data = q.get('BCHAIN/MKPRU', api_key=config['quandl']['api_key'])
h5 = pd.HDFStore('data.h5', 'w')
h5['data'] = data
