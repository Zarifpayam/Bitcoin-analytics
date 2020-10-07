import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

pd.set_option('display.max_columns',13)
pd.set_option('display.width',1820)

Txnperminute= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\Trades-per-minute.csv', sep=',')
Txnperminute.Time = Txnperminute.Time.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S UTC"))
Txnperminute = Txnperminute[['Time','bitfinex']]
Txnperminute = Txnperminute[Txnperminute['Time']<='2020-10-01']
#print(Txnperminute)

blocksize = pd.read_json(r'C:\Users\User\Desktop\Bitcoin serious\block-size-mean.json')
blocksize.t= blocksize.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
#print(blocksize)

with open(r'C:\Users\User\Desktop\Bitcoin serious\hash-rate.json') as f1:
    d1=json.load(f1)
hashrate = pd.json_normalize(d1)
hashrate.t = hashrate.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
hashrate.v=hashrate.v.values.astype(float)
#print(hashrate)

with open(r'C:\Users\User\Desktop\Bitcoin serious\difficulty.json') as f1:
    d2=json.load(f1)
difficulty = pd.json_normalize(d2)
difficulty.t= difficulty.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
difficulty.v=difficulty.v.values.astype(float)
#print(difficulty)

Timebb = pd.read_json(r'C:\Users\User\Desktop\Bitcoin serious\Time between blocks.json')
Timebb.t= Timebb.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
#print('Timebb',Timebb)

#Je l'ai enlevé faute de donnée recente.
# TXNnum = pd.read_json(r'C:\Users\User\Desktop\Bitcoin serious\transaction-count.json')
# TXNnum.t= TXNnum.t.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
#print('TXNnm',TXNnum)

TXNconfirmed= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\Confirmed transactions per day.csv', sep=',')
TXNconfirmed.Timestamp = TXNconfirmed.Timestamp.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").date())
#print('TXNconfirmed',TXNconfirmed)

mempooltxn= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\mempool-count.csv', sep=',')
mempooltxn.Timestamp = mempooltxn.Timestamp.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").date())
#print('mempooltxn',mempooltxn)

Marketcap= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\market-cap.csv', sep=',')
Marketcap.Timestamp = Marketcap.Timestamp.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").date())
#print('Marketcap',Marketcap)

txnvalue= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\estimated-transaction-volume-usd.csv', sep=',')
txnvalue.Timestamp = txnvalue.Timestamp.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").date())
#print('txnvalue',txnvalue)

price= pd.read_csv(r'C:\Users\User\Desktop\Bitcoin serious\price_by_venue.csv', sep=',')
price.Time = price.Time.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S UTC"))
price['%chng_kraken']= price['kraken'].pct_change()
price['pd'] = np.where(price['%chng_kraken'] > 0 ,1,-1)
#print(price)

data=Txnperminute.set_index('Time').join(blocksize.set_index('t')).join(hashrate.set_index('t'),rsuffix='hashrate')\
    .join(difficulty.set_index('t'),rsuffix='difficulty').join(Timebb.set_index('t'),rsuffix='Timebb').join(TXNconfirmed.set_index('Timestamp')).join(mempooltxn.set_index('Timestamp'))\
    .join(Marketcap.set_index('Timestamp')).join(txnvalue.set_index('Timestamp')).join(price[['Time','pd']].set_index('Time'))
#print(data.info())
target = data.pop('pd')
data = data.fillna(method='ffill')
columns_names = pd.Series(data.columns)
print(columns_names)
X = data
Y = target
print(f'Dataset X shape: {X.shape}')
print(f'Dataset y shape: {Y.shape}')

(X_train, X_test, y_train, y_test) = train_test_split(X, Y, test_size=0.35, random_state=1)
lr = LogisticRegression()
lr.fit(X_train, y_train)

print(f"Intercept per class: {lr.intercept_}\n")
print(f"Coeficients per class: {lr.coef_}\n")

print(f"Available classes: {lr.classes_}\n")
print(f"Named Coeficients for class 1: {pd.DataFrame(lr.coef_[0], columns_names)}\n")

print(f"Number of iterations generating model: {lr.n_iter_}")
