import pandas as pd
from pandas import DataFrame

df= pd.read_table(r"E:\work\text\data.txt",sep='\t',header=None)
df1= pd.read_table(r"E:\work\text\data2.txt",sep='\t',header=None)

df=df[df[4].isin(df1[0])]
print(df)
# df.to_csv(r"E:\work\text\data_C.csv",index=False)