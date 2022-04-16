#Veri Setine İlk Bakış
import numpy as np
import pandas as pd
def check_df(dataframe, head=5):

    # boyut bilgisi
    print("################### Shape ###################")
    print(dataframe.shape)

    # tip bilgisi
    print("################### Types ###################")
    print(dataframe.dtypes)

    #Baştan gözlemleyelim
    print("################### Head ###################")
    print(dataframe.head(head))

    #Sondan gözlemleyelim
    print("################### Tail ###################")
    print(dataframe.tail(head))

    #Veri setinde herhangi bir eksik değer var mı bakalım
    print("################### NA ###################")
    print(dataframe.isnull().sum())

    #Sayısal değişkenlerin dağılımına bakalım
    print("################### Quantiles ###################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)



#Bazı veri setleri üzerinde tanımladığım check_df fonksiyonunun nasıl çalıştığını gözlemlemek istiyorum.

import seaborn as sns

df1 = sns.load_dataset("titanic")
check_df(df1)

df2 = sns.load_dataset("tips")
check_df(df2)

