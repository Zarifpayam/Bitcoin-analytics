import pandas as pd
import nov4data

addresseswithbalanceover100, marketcaptothermocapratio, asol, reserverisk, puellmultiple,nvtsignal, relativeunrealizedprofit, stocktoflowdeflection, \
blocksizemean, blockintervalmean,transactioncount, percentutxosinprofit, sendingent, price, asopr, minedblock, circulatingsupply,\
FRM, feestotal, liveliness, mvrvratio, txncount, volume, tempdata = nov4data.load_indicator_data()

def create_data_object():
    data2=sendingent[['timestamp','delta']].set_index('timestamp')\
        .join(FRM.set_index('timestamp'))\
        .join(addresseswithbalanceover100.set_index('timestamp'),rsuffix=' addresseswithbalanceover100')\
        .join(marketcaptothermocapratio.set_index('timestamp'),rsuffix=' marketcaptothermocapratio')\
        .join(asol.set_index('timestamp'),rsuffix='asol') \
        .join(puellmultiple.set_index('timestamp'), rsuffix='puellmultiple') \
        .join(nvtsignal.set_index('timestamp'), rsuffix='nvtsignal') \
        .join(stocktoflowdeflection.set_index('timestamp'), rsuffix='stocktoflowdeflection')\
        .join(relativeunrealizedprofit.set_index('timestamp'), rsuffix='relativeunrealizedprofit') \
        .join(blocksizemean.set_index('timestamp'), rsuffix='blocksizemean')\
        .join(transactioncount.set_index('timestamp'), rsuffix='transactioncount') \
        .join(percentutxosinprofit.set_index('timestamp'), rsuffix='percentutxosinprofit') \
        .join(tempdata['feepertxn'], rsuffix='feepertxn')\
        .join(tempdata['feeperblock'],rsuffix='feeperblock')\
        .join(tempdata['volumepertxn'],rsuffix='volumepertxn')\
        .join(tempdata['supplypervol'],rsuffix='supplypervol')\
        .join(blockintervalmean.set_index('timestamp'), rsuffix='blockinterval')\
        .join(mvrvratio.set_index('timestamp'), rsuffix='mvrvratio')\
        .join(asopr.set_index('timestamp'), rsuffix='asopr')\
        .join(price[['timestamp','pd','c']].set_index('timestamp'))
    print(data2.info())

 #   data.to_csv(r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\data.csv', sep=',')
    return data2