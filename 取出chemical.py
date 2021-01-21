import pandas as pd
from pandas import DataFrame

# df= pd.read_excel(u"E:\\work\\text\\text.xlsx",header=None)
# 打开大文件前5行
# df = pd.read_table('E:\chemicals.v4.0.tsv',sep='\t',header=0,iterator = True)

# 分块读取大文件
df = pd.read_table('E:\chemicals.v4.0.tsv',sep='\t',header=0, chunksize=1000000)
df1= pd.read_table(r"E:\work\\text\data1.txt",sep='\t',header=None)

for chunk in df:
    # print(chunk['chemical'])
    chunk1 = chunk["chemical"].astype(str)
    # print(chunk1)
    # print(chunk[chunk1.isin(df1[1])])
    chunk=chunk[chunk1.isin(df1[1])]
    # f=open("E:\work\\text\data_f2.txt")
    # for i in range(len(chunk))
    chunk.to_csv(r"E:\work\text\data_f2.csv", index=False,mode= 'a')

