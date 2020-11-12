import pandas as pd
import Nov11
import nov4data

feestotal,minedblock,transactioncount,volume,circulatingsupply,price,RCHodlewave, sendingent,percentutxosinprofit,\
    FRM,asopr,mvrvratio,liveliness,puellmultiple,nvtsignal,relativeunrealizedprofit = Nov11.load_indicator_data()

# addresseswithbalanceover100,marketcaptothermocapratio,asol,reserverisk,puellmultiple,\
#            nvtsignal,relativeunrealizedprofit,stocktoflowdeflection,blocksizemean,blockintervalmean,\
#            transactioncount,percentutxosinprofit,sendingent,price,asopr,minedblock,circulatingsupply,\
#            FRM,feestotal,liveliness,mvrvratio,txncount,volume,tempdata=nov4data.load_indicator_data()
#
# def create_data_object_Nov4():
#     data2=sendingent[['timestamp','delta']].set_index('timestamp')\
#         .join(FRM.set_index('timestamp'))\
#         .join(addresseswithbalanceover100.set_index('timestamp'),rsuffix='addresseswithbalanceover100')\
#         .join(marketcaptothermocapratio.set_index('timestamp'),rsuffix=' marketcaptothermocapratio')\
#         .join(asol.set_index('timestamp'),rsuffix='asol') \
#         .join(puellmultiple.set_index('timestamp'), rsuffix='puellmultiple') \
#         .join(nvtsignal.set_index('timestamp'), rsuffix='nvtsignal') \
#         .join(stocktoflowdeflection.set_index('timestamp'), rsuffix='stocktoflowdeflection')\
#         .join(relativeunrealizedprofit.set_index('timestamp'), rsuffix='relativeunrealizedprofit') \
#         .join(blocksizemean.set_index('timestamp'), rsuffix='blocksizemean')\
#         .join(transactioncount.set_index('timestamp'), rsuffix='transactioncount') \
#         .join(percentutxosinprofit.set_index('timestamp'), rsuffix='percentutxosinprofit') \
#         .join(tempdata['feepertxn'], rsuffix='feepertxn')\
#         .join(tempdata['feeperblock'],rsuffix='feeperblock')\
#         .join(tempdata['volumepertxn'],rsuffix='volumepertxn')\
#         .join(tempdata['supplypervol'],rsuffix='supplypervol')\
#         .join(blockintervalmean.set_index('timestamp'), rsuffix='blockinterval')\
#         .join(mvrvratio.set_index('timestamp'), rsuffix='mvrvratio')\
#         .join(asopr.set_index('timestamp'), rsuffix='asopr')\
#         .join(price['pd'])
#     data2 = data2.dropna()



 #   data.to_csv(r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Oct28\data.csv', sep=',')
 #   return data2

def create_data_object():

    tempdata = feestotal.set_index('timestamp').join(minedblock.set_index('timestamp'),rsuffix='mb')\
        .join(transactioncount.set_index('timestamp'),rsuffix='tc').join(volume.set_index('timestamp'),rsuffix='v')\
        .join(circulatingsupply.set_index('timestamp'),rsuffix='cs').join(RCHodlewave['1m_3m']).join(sendingent['delta'])\
        .join(percentutxosinprofit).join(FRM).join(asopr).join(mvrvratio).join(liveliness).join(puellmultiple).join(nvtsignal)\
        .join(relativeunrealizedprofit)


    tempdata['feepertxn'] = tempdata['value']/tempdata['valuetc']
    tempdata['feeperblock']= tempdata['value']/tempdata['valuemb']
    tempdata['volumepertxn'] = tempdata['valuev']/tempdata['valuetc']
    tempdata['supplypervol'] = tempdata['valuecs']/tempdata['valuev']
    tempdata=tempdata[tempdata.index>'2015-01-17']


    data2=tempdata[['feepertxn','volumepertxn','feeperblock','supplypervol','%UTXOinprofit','FRM','mvrv','liveliness','nvtsig','RelativeUprofit','Puell']]\
    .join(price[['pd','stdev']])

    data2=data2[data2['stdev']<0.07]

    data2.to_csv(r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\data.csv', sep=',')
    return data2