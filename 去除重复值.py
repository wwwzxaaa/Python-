import pandas as pd
import numpy as np
from pandas import DataFrame
df=pd.read_excel(r"E:\work\result_subcomp.xlsx",header=None)
height,width = df.shape
for i in range(1,width):
    for j in range(i+1,width):
        if df[i][0]==df[j][0]:
            for m in range(1,height):
                df[i][m]=max(df[i][m],df[j][m])
                df[j][m]=max(df[i][m],df[j][m])
print(df)
df.to_excel("E:\work\\result_subcomp1.xlsx")