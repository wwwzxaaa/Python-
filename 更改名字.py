import pandas as pd
from collections import ChainMap
import collections
df = pd.read_excel(r"E:\work\data.xlsx", header=0)
df1 = pd.read_csv(r"E:\work\end_D.csv", header=None)
lens=len(df1[0])
a=list(df1[1])
b=list(df1[0])
def rename():
    i = 0
    value = ChainMap()
    while i<lens:
        # dict = {a[i]:b[i]}
        value[a[i]]=b[i]
        value = value.new_child()  # 添加字典到集合
        value = value.parents
        i=i+1
    return value

value1=rename()
value2=dict(value1)
df[2] = df[1].map(value2)
df.to_excel(r"E:\work\rename.xlsx", index=False)