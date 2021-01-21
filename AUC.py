import pandas as pd
import os
from pandas import DataFrame
AUC=[]
df1 = pd.read_csv('E:\python\\auc\m20-rf.csv',sep=',',header=0,error_bad_lines=False)
    # print(df1)
S=[]
for i in range(0,101):
        # print(i)
    s=(df1.loc[i,'TPR']+df1.loc[i+1,'TPR'])*(df1.loc[i,'FPR']-df1.loc[i+1,'FPR'])/2
    S.append(s)
AUC.append(S)
print(AUC[0])
print(type(AUC[0][1]))
#遍历计算每列值之和，即求得AUC的值
for i in range(len(AUC)):
    AUC[i].append(sum(AUC[i]))
print(AUC[i])

0.96306398433
