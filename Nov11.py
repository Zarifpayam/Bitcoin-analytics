import numpy as np
import pandas as pd
import datetime as dt

pd.set_option('display.max_columns', 13)
pd.set_option('display.width', 1820)

def load_indicator_data():

    price= pd.read_csv(r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\price.csv', sep=',')
    price.timestamp = price.timestamp.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").date())
    price=price.groupby(['timestamp']).max()
    price['c']= price['c'].pct_change()
    price['pd'] = np.where(price['c'] > 0 ,1,0)
    price['stdev'] = price['c'].rolling(2).std()

    transactioncount = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\transaction-count.csv', sep=',')
    transactioncount.timestamp = transactioncount.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    transactioncount.value = transactioncount.value.values.astype(float)
    # print(transactioncount)

    feestotal = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\fees-total.csv', sep=',')
    feestotal.timestamp = feestotal.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    feestotal.value = feestotal.value.values.astype(float)

    minedblock = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\blocks-mined.csv', sep=',')
    minedblock.timestamp = minedblock.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    minedblock.value = minedblock.value.values.astype(float)
    # print(percentutxosinprofit)

    circulatingsupply = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\circulating-supply.csv', sep=',')
    circulatingsupply.timestamp = circulatingsupply.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    circulatingsupply.value = circulatingsupply.value.values.astype(float)
    # print(percentutxosinprofit)

    volume = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\transfer-volume-total.csv', sep=',')
    volume.timestamp = volume.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    volume.value = volume.value.values.astype(float)

    RCHodlewave = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\realized-cap-hodl-waves.csv', sep=',')
    RCHodlewave.timestamp = RCHodlewave.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    RCHodlewave = RCHodlewave.set_index('timestamp')
    RCHodlewave = RCHodlewave.astype(float)

    receivingent = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\receiving-addresses.csv', sep=',')
    receivingent.timestamp = receivingent.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    receivingent.value = receivingent.value.values.astype(float)

    sendingent = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\sending-addresses.csv', sep=',')
    sendingent.timestamp = sendingent.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").date())
    sendingent.value = sendingent.value.values.astype(float)
    sendingent['delta'] = receivingent['value'] - sendingent['value']
    sendingent=sendingent.set_index('timestamp')

    percentutxosinprofit = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\percent-utx-os-in-profit.csv', sep=',')
    percentutxosinprofit.timestamp = percentutxosinprofit.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    percentutxosinprofit.value = percentutxosinprofit.value.values.astype(float)
    percentutxosinprofit = percentutxosinprofit.rename(columns={'value': '%UTXOinprofit'})
    percentutxosinprofit = percentutxosinprofit.set_index('timestamp')

    FRM = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\fee-ratio-multiple-frm.csv', sep=',')
    FRM.timestamp = FRM.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    FRM.value = FRM.value.values.astype(float)
    FRM = FRM.rename(columns={'value': 'FRM'})
    FRM = FRM.set_index('timestamp')

    asopr = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\a-sopr.csv', sep=',')
    asopr.timestamp = asopr.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    asopr.value = asopr.value.values.astype(float)
    asopr=asopr.set_index('timestamp')
    asopr=asopr.rename(columns={'value':'asopr'})

    mvrvratio = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\mvrv-ratio.csv', sep=',')
    mvrvratio.timestamp = mvrvratio.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    mvrvratio.value = mvrvratio.value.values.astype(float)
    mvrvratio=mvrvratio.set_index('timestamp')
    mvrvratio=mvrvratio.rename(columns={'value':'mvrv'})

    liveliness = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\liveliness.csv', sep=',')
    liveliness.timestamp = liveliness.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    liveliness.value = liveliness.value.values.astype(float)
    liveliness=liveliness.rename(columns={'value':'liveliness'})
    liveliness = liveliness.set_index('timestamp')

    puellmultiple = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\puell-multiple.csv', sep=',')
    puellmultiple.timestamp = puellmultiple.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    puellmultiple.value = puellmultiple.value.values.astype(float)
    puellmultiple=puellmultiple.set_index('timestamp')
    puellmultiple=puellmultiple.rename(columns={'value':'Puell'})
    # print(reserverisk)

    nvtsignal = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\nvt-signal.csv', sep=',')
    nvtsignal.timestamp = nvtsignal.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    nvtsignal.value = nvtsignal.value.values.astype(float)
    nvtsignal=nvtsignal.set_index('timestamp')
    nvtsignal=nvtsignal.rename(columns={'value':'nvtsig'})
    # print(nvtsignal)

    relativeunrealizedprofit = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\relative-unrealized-profit.csv', sep=',')
    relativeunrealizedprofit.timestamp = relativeunrealizedprofit.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    relativeunrealizedprofit.value = relativeunrealizedprofit.value.values.astype(float)
    relativeunrealizedprofit = relativeunrealizedprofit.set_index('timestamp')
    relativeunrealizedprofit = relativeunrealizedprofit.rename(columns={'value':'RelativeUprofit'})

    return feestotal,minedblock,transactioncount,volume,circulatingsupply,price,RCHodlewave,sendingent,percentutxosinprofit,FRM,asopr,\
           mvrvratio,liveliness,puellmultiple,nvtsignal,relativeunrealizedprofit