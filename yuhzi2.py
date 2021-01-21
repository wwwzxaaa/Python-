import pandas as pd
from pandas import DataFrame
import random
# 每个化合物预测为致癌的概率和分类阈值比较。若大于等于阈值则分为致癌的，否则为非致癌的
df=pd.read_csv("E:\work\weka\weka0\max\ABM1\\max-abm1.csv",header=None)
print(df)
df1 = DataFrame()
# # 阈值t是从0到1,不取0,以0.01为步长增加,共计100个

df1[0] = df[0]

for i in range(1,101):
    t=i/100
    for r in range(0,114117):

        if t<=df.loc[r,5]:
            df1.loc[r,i]=1
        else:
            df1.loc[r,i]=0
df1.to_csv("E:\work\weka\weka0\max\ABM1\\rs-max-abm1.csv",index=False,header=None)