import numpy as np
import pandas as pd
import scipy.stats as sp
import statsmodels as sm
import datetime as dt
import matplotlib.pyplot as plt
import json

pd.set_option('display.max_columns',10)
pd.set_option('display.width',1820)


blocksize = pd.read_json(r'C:\Users\User\Desktop\Bitcoin serious\block-size-mean.json')
blocksize.t= blocksize.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
print(blocksize)

with open(r'C:\Users\User\Desktop\Bitcoin serious\hash-rate.json') as f1:
    d1=json.load(f1)
hashrate = pd.json_normalize(d1)
hashrate.t = hashrate.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
print(hashrate)

with open(r'C:\Users\User\Desktop\Bitcoin serious\difficulty.json') as f1:
    d2=json.load(f1)
difficulty = pd.json_normalize(d2)
difficulty.t= difficulty.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
print(difficulty)

Timebb = pd.read_json(r'C:\Users\User\Desktop\Bitcoin serious\Time between blocks.json')
Timebb.t= Timebb.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
print(Timebb)

TXNnum = pd.read_json(r'C:\Users\User\Desktop\Bitcoin serious\transaction-count.json')
TXNnum.t= TXNnum.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
print(TXNnum)

TXNconfirmed= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\Confirmed transactions per day.csv', sep=',')
TXNconfirmed.Timestamp = TXNconfirmed.Timestamp.apply(lambda x:dt.datetime.strptime(x, "%m/%d/%Y %H:%M"))
print(TXNconfirmed)

mempooltxn= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\mempool-count.csv', sep=',')
mempooltxn.Timestamp = mempooltxn.Timestamp.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
print(mempooltxn)

Marketcap= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\market-cap.csv', sep=',')
Marketcap.Timestamp = Marketcap.Timestamp.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
print(Marketcap)

txnvalue= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\estimated-transaction-volume-usd.csv', sep=',')
txnvalue.Timestamp = txnvalue.Timestamp.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
print(txnvalue)

Txnperminute= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\Trades-per-minute.csv', sep=',')
Txnperminute.Time = Txnperminute.Time.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S UTC"))
print(Txnperminute)

price= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\price_by_venue.csv', sep=',')
price.Time = price.Time.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S UTC"))
price['%chng_kraken']= price['kraken'].pct_change()
price['pd'] = np.where(price['%chng_kraken'] > 0 ,1,-1)
print(price)
