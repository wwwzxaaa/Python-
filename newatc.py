import pandas as pd
from pandas import DataFrame
df= pd.read_table(r"E:\work\text\t_cid.txt",sep='\t',header=None)
for i in range(0,len(df[0])):
    for j in range(0,len(df[1])):
        if (df[0][i]==df[1][j])&(df[1][i]==df[0][j]):
            df[2][i] = df[2][j]
            df[2][j]=df[2][i]
df.to_csv('E:\work\\text\\text1.txt',index=False,encoding='utf-8')
# ATC_CID_SET = open("E:\work\\text\\t.csv","r")
# R_ATC_CID_SET = ATC_CID_SET.readlines()
# Dict_ATC_CID_SET =[]
# List_ATC_CID_SET = []
# temp = []
# for i in range(len(R_ATC_CID_SET)):
#     temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[0])
#     temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[1:])
#     List_ATC_CID_SET.append(temp)
#     temp = []
# temp01 = []
# for i in range(1,1094):
#     for j in range(1,1094):
#         for m in range(0,1093):
#             if List_ATC_CID_SET[0][1][m]==List_ATC_CID_SET[i][0]:
#                 List_ATC_CID_SET[i][1][m]=1


