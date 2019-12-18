import pandas as pd
from pandas import DataFrame

# df=pd.read_csv(r"E:\work\text\data.csv")
df1= pd.read_table(r"E:\work\text\data1.txt",sep='\n',header=None)
df= pd.read_table(r"E:\work\text\CID.txt",sep='\t',header=None)
# df[6] = df[[0,1]].apply(lambda x: ''.join(x), axis=1)
# df1[2] = df1[[0,1]].apply(lambda x: ''.join(x), axis=1)
# print(df1[2])
# print(df[6])
df=df[6].isin(df1[2])
print(df)
#将筛选后的新文件输出
# df.to_csv(r"E:\work\text\drug-detail.csv",index=False)
# df1.to_csv(r"E:\work\text\drug-detail1.csv",index=False)