import pandas as pd
from pandas import DataFrame

df= pd.read_table(r"E:\work\text1\CID0.txt",sep='\t',header=None)

df1= pd.read_table(r"E:\work\text\end_drug.txt",sep='\t',header=None)

df=df[df[0].isin(df1[1]) & df[1].isin(df1[1])]
df.to_csv(r"E:\work\text\end_cid.csv",index=False)