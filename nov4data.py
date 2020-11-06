import numpy as np
import pandas as pd
import datetime as dt


def create_data_object():
    pd.set_option('display.max_columns',13)
    pd.set_option('display.width',1820)

    accumbal = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\accumulation-balance.csv', sep=',')
    accumbal.timestamp = accumbal.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    accumbal.value = accumbal.value.values.astype(float)
   # print(accumbal)

    activent = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\active-entities.csv', sep=',')
    activent.timestamp = activent.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
   # print(activent)

    entgrowth = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\entities-net-growth.csv', sep=',')
    entgrowth.timestamp = entgrowth.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    #print(activent)

    Uprofit = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\entity-adjusted-unrealized-profit.csv', sep=',')
    Uprofit.timestamp = Uprofit.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
   # print(Uprofit)

    exchangebal = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\exchange-balance.csv', sep=',')
    exchangebal.timestamp = exchangebal.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    exchangebal.value = exchangebal.value.values.astype(float)
   # print(exchangebal)

    lthmvrv = pd.read_csv(r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\lth-mvrv.csv',
                             sep=',')
    lthmvrv.timestamp = lthmvrv.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
   # print(lthmvrv)

    minerstoexchanges = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\miners-to-exchanges.csv', sep=',')
    minerstoexchanges.timestamp = minerstoexchanges.timestamp.apply(
        lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    #print(minerstoexchanges)


    receivingent = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\receiving-entities.csv', sep=',')
    receivingent.timestamp = receivingent.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    receivingent.value = receivingent.value.values.astype(float)
   # print(receivingent)

    addresseswithbalanceover100 = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\addresses-with-balance-≥-100.csv', sep=',')
    addresseswithbalanceover100.timestamp = addresseswithbalanceover100.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    addresseswithbalanceover100.value = addresseswithbalanceover100.value.values.astype(float)
    # print(addresseswithbalanceover100)

    marketcaptothermocapratio = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\market-cap-to-thermocap-ratio.csv', sep=',')
    marketcaptothermocapratio.timestamp = marketcaptothermocapratio.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    marketcaptothermocapratio.value = marketcaptothermocapratio.value.values.astype(float)
    # print(marketcaptothermocapratio)

    asol = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\asol.csv', sep=',')
    asol.timestamp = asol.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    asol.value = asol.value.values.astype(float)
    # print(reserve-risk)

    reserverisk = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\reserve-risk.csv', sep=',')
    reserverisk.timestamp = reserverisk.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    reserverisk.value = reserverisk.value.values.astype(float)
    # print(reserverisk)

    puellmultiple = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\puell-multiple.csv', sep=',')
    puellmultiple.timestamp = puellmultiple.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    puellmultiple.value = puellmultiple.value.values.astype(float)
    # print(reserverisk)

    nvtsignal = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\nvt-signal.csv', sep=',')
    nvtsignal.timestamp = nvtsignal.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    nvtsignal.value = nvtsignal.value.values.astype(float)
    # print(nvtsignal)

    relativeunrealizedprofit = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\relative-unrealized-profit.csv', sep=',')
    relativeunrealizedprofit.timestamp = relativeunrealizedprofit.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    relativeunrealizedprofit.value = relativeunrealizedprofit.value.values.astype(float)
    # print(nvtsignal)

    stocktoflowdeflection = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\stock-to-flow-deflection.csv', sep=',')
    stocktoflowdeflection.timestamp = stocktoflowdeflection.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    stocktoflowdeflection.value = stocktoflowdeflection.value.values.astype(float)

    blocksizemean = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\block-size-mean.csv', sep=',')
    blocksizemean.timestamp = blocksizemean.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    blocksizemean.value = blocksizemean.value.values.astype(float)
    # print(nvtsignal)

    blockintervalmean = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\block-interval-mean.csv', sep=',')
    blockintervalmean.timestamp = blockintervalmean.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    blockintervalmean.value = blockintervalmean.value.values.astype(float)
    # print(blockintervalmean)

    transactioncount = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\transaction-count.csv', sep=',')
    transactioncount.timestamp = transactioncount.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    transactioncount.value = transactioncount.value.values.astype(float)
    # print(transactioncount)

    percentutxosinprofit = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\percent-utx-os-in-profit.csv', sep=',')
    percentutxosinprofit.timestamp = percentutxosinprofit.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    percentutxosinprofit.value = percentutxosinprofit.value.values.astype(float)
    # print(percentutxosinprofit)

    sendingent = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\sending-entities.csv', sep=',')
    sendingent.timestamp = sendingent.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    sendingent.value = sendingent.value.values.astype(float)
    # print(receivingent)
    sendingent['delta'] = receivingent['value'] - sendingent['value']
    #print(sendingent)

    price= pd.read_csv(r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\price.csv', sep=',')
    price.timestamp = price.timestamp.apply(lambda x:dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    price['c']= price['c'].pct_change()
    price['pd'] = np.where(price['c'] > 0 ,1,0)
    #print(price)

    asopr = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\a-sopr.csv', sep=',')
    asopr.timestamp = asopr.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    asopr.value = asopr.value.values.astype(float)
    # print(percentutxosinprofit)

    Blockinterval = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\block-interval-mean.csv', sep=',')
    Blockinterval.timestamp = Blockinterval.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    Blockinterval.value = Blockinterval.value.values.astype(float)
    # print(percentutxosinprofit)

    minedblock = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\blocks-mined.csv', sep=',')
    minedblock.timestamp = minedblock.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    minedblock.value = minedblock.value.values.astype(float)
    # print(percentutxosinprofit)

    circulatingsupply = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\circulating-supply.csv', sep=',')
    circulatingsupply.timestamp = circulatingsupply.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    circulatingsupply.value = circulatingsupply.value.values.astype(float)
    # print(percentutxosinprofit)

    FRM = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\fee-ratio-multiple-frm.csv', sep=',')
    FRM.timestamp = FRM.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    FRM.value = FRM.value.values.astype(float)

    feestotal = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\fees-total.csv', sep=',')
    feestotal.timestamp = feestotal.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    feestotal.value = feestotal.value.values.astype(float)

    # hodlwaves = pd.read_csv(
    #     r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\hodl-waves.csv', sep=',')
    # hodlwaves.timestamp = hodlwaves.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    # hodlwaves.value = hodlwaves.value.values.astype(float)

    liveliness = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\liveliness.csv', sep=',')
    liveliness.timestamp = liveliness.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    liveliness.value = liveliness.value.values.astype(float)

    mvrvratio = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\mvrv-ratio.csv', sep=',')
    mvrvratio.timestamp = mvrvratio.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    mvrvratio.value = mvrvratio.value.values.astype(float)


    txncount = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\transaction-count.csv', sep=',')
    txncount.timestamp = txncount.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    txncount.value = txncount.value.values.astype(float)

    volume = pd.read_csv(
        r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov4\transfer-volume-total.csv', sep=',')
    volume.timestamp = volume.timestamp.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))
    volume.value = volume.value.values.astype(float)

    tempdata = feestotal.set_index('timestamp').join(minedblock.set_index('timestamp'),rsuffix='mb')\
        .join(transactioncount.set_index('timestamp'),rsuffix='tc').join(volume.set_index('timestamp'),rsuffix='v')\
        .join(circulatingsupply.set_index('timestamp'),rsuffix='cs')


    tempdata['feepertxn'] = tempdata['value']/tempdata['valuetc']
    tempdata['feeperblock']= tempdata['value']/tempdata['valuemb']
    tempdata['volumepertxn'] = tempdata['valuev']/tempdata['valuetc']
    tempdata['supplypervol'] = tempdata['valuecs']/tempdata['valuev']
    print(tempdata)

    data2=sendingent[['timestamp','delta']].set_index('timestamp')\
        .join(FRM.set_index('timestamp'))\
        .join(accumbal.set_index('timestamp'),rsuffix=' accumbal')\
        .join(entgrowth.set_index('timestamp'),rsuffix=' entgrowth')\
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