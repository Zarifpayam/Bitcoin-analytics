import pandas as pd
import Nov11

feestotal,minedblock,transactioncount,volume,circulatingsupply,price,RCHodlewave, sendingent,percentutxosinprofit,\
    FRM,asopr,mvrvratio,liveliness,puellmultiple,nvtsignal,relativeunrealizedprofit = Nov11.load_indicator_data()


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


    data2=tempdata[['feepertxn','volumepertxn','feeperblock','supplypervol','%UTXOinprofit','FRM','mvrv','liveliness','nvtsig','RelativeUprofit','Puell','delta']]\
    .join(price[['pd','stdev']])

    data2=data2[data2['stdev']<0.07]

#    data2.to_csv(r'C:\Users\User\Google Drive\Boule cristale de Bitcoin\Bitcoin serious\Nov11\data.csv', sep=',')
    return data2