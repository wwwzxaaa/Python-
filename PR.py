import pandas as pd
import os
from pandas import DataFrame
AUC=[]
list_file = os.listdir('E:/python/auc值')
# df=pd.read_csv('E:\python\\auc\\5-abm1.csv',sep=',',header=0)
# print(df)
#list_test = []
for m in range(len(list_file)):
    filename = 'E:/python/auc值/'+list_file[m]
    # list_test.append(filename)
    # df_test = pd.DataFrame(list_test)
    # df_test.to_csv('E:\python\\test.csv')
    #print(filename)
    df1 = pd.read_csv(filename,sep=',',header=0,error_bad_lines=False)
#     print(df1)
    S=[]
    for i in range(0,101):
        # print(i)
        s=(df1.loc[i,'P']+df1.loc[i+1,'P'])*(df1.loc[i,'R']-df1.loc[i+1,'R'])/2
        S.append(s)
    S.append(filename)
    AUC.append(S)
print(AUC[0])
print(type(AUC[0][1]))
#遍历计算每列值之和，即求得AUC的值
# for i in range(len(AUC)):
#     AUC[i].append(sum(AUC[i]))
# AUC由列表转为DataFrame格式时，列变为行
AUC=pd.DataFrame(AUC)
AUC.to_csv("E:/python/PR_ALL.csv",index=False,header=None)