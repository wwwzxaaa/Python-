import os
import pandas as pd
import numpy as np
from pandas import DataFrame

# def calc_func(count,df,list):
#     temp={}
#     for i in range(0,count-1):
#         for j in range(i+1,count-1):
#             sum1 = 0
#             sum2 = 0
#             for a in range(0,1023):
#                 if list[i][a]==1&list[j][a]==1:
#                     sum1=sum1+1
#                 if list[i][a]==1|list[j][a]==1:
#                     sum2=sum2+1
#                 if sum2!=0:
#                     similarity=sum1/sum2
#                     if similarity:
#                         df_index="{0} {1}".format(list[i][0],list[j][0])
#                         temp[df_index]='%03f'%similarity
#     return temp
# df= pd.read_csv(r"E:\work\end_chemical1.csv",index_col = 'chemId')
# mylist=df.values.tolist()
# print(mylist)
# D1=calc_func(len(mylist),df,mylist)
# path = r"E:\work\text\similatity.txt"	#文件路径
# f = open(path,'w',encoding='utf-8')		#以'w'方式打开文件
# for k,v in D1.items():			# 遍历字典中的键值
#     s2 = str(v)                 # 把字典的值转换成字符型
#     f.write(k+' '+s2+'\n')             # 键和值分行放，键在单数行，值在双数行
# f.close()
ATC_CID_SET = open("E:\\work\\text1\\end_chemical1.csv","r")
W_ATC_CID_SET = open("E:\\work\\text\\similatity.txt","w")
R_ATC_CID_SET = ATC_CID_SET.readlines()
Dict_ATC_CID_SET =[]
List_ATC_CID_SET = []
temp = []
for i in range(len(R_ATC_CID_SET)):
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[0])
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[1:])
    List_ATC_CID_SET.append(temp)
    temp = []
temp01 = []
for i in range(1,1094):
    for j in range(1,1094):
        key = List_ATC_CID_SET[i][0] + '\t' + List_ATC_CID_SET[j][0]
        sum1 = 0
        sum2 = 0
        for m in range(0,1023):
            a = List_ATC_CID_SET[i][1][m]
            b = List_ATC_CID_SET[j][1][m]
            if (a == '1') & (b == '1'):
                sum1=sum1+1
            if (a=='1') | (b=='1'):
                sum2=sum2+1
        if sum2!=0:
            value = round(sum1/sum2,6)
            if value!=0:
                temp01.append(key)
                temp01.append(value)
                Dict_ATC_CID_SET.append(temp01)
                temp01 = []
for n in range(len(Dict_ATC_CID_SET)):
    W_ATC_CID_SET.write(Dict_ATC_CID_SET[n][0] + "\t" + str(Dict_ATC_CID_SET[n][1])+"\n")
print(Dict_ATC_CID_SET)
print(len(Dict_ATC_CID_SET))
