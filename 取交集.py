# -*- coding=utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame
# def calc_func(count,df,list):
#     temp={}
#     for i in range(0,count-1):
#         i = i + 1
#         for j in range(i+1,count-1):
#             j = j + 1
#             ret1 = set(list[i]).union(set(list[j]))#并集
#                 # print(ret1)
#             ret2 = set(list[i]).intersection(set(list[j]))#交集
#                 # print(ret2)
#             same=(len(ret2)-1)/(len(ret1)-1)
#                 # print(same)
#             if same:
#                 df_index="{0} {1}".format(i,j)
#                 temp[df_index]='%03f'%same
#     return temp
# df=pd.read_csv(r"E:\work\data_protein.csv",index_col = 'column')
# mylist=df.values.tolist()
# D1=calc_func(len(mylist),df,mylist)
# path = r"E:\work\text\same.txt"	#文件路径
# f = open(path,'w',encoding='utf-8')		#以'w'方式打开文件
# for k,v in D1.items():			# 遍历字典中的键值
#     s2 = str(v)                 # 把字典的值转换成字符型
#     f.write(k+' '+s2+'\n')             # 键和值分行放，键在单数行，值在双数行
# f.close()
ATC_CID_SET = open("E:\work\\text1\data_protein.csv","r")
W_ATC_CID_SET = open("E:\work\\text\same1.txt","w")
R_ATC_CID_SET = ATC_CID_SET.readlines()
Dict_ATC_CID_SET =[]
List_ATC_CID_SET = []
temp = []
for i in range(len(R_ATC_CID_SET)):
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[0])
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[1:])
    List_ATC_CID_SET.append(temp)
    temp = []
#print(List_ATC_CID_SET)
temp01 = []
for i in range(1,718):
    for j in range(i,718):
        key = List_ATC_CID_SET[i][0] + '\t' +List_ATC_CID_SET[j][0]
        denominator= len(set(List_ATC_CID_SET[i][1]).union(set(List_ATC_CID_SET[j][1])))-1
        numerator = len(set(List_ATC_CID_SET[i][1]).intersection(set(List_ATC_CID_SET[j][1])))-1
        if denominator!=0:
            value = round(numerator/denominator,6)
            if value>0:
                temp01.append(key)
                temp01.append(value)
                Dict_ATC_CID_SET.append(temp01)
                temp01 = []
for i in range(len(Dict_ATC_CID_SET)):
    W_ATC_CID_SET.write(Dict_ATC_CID_SET[i][0] + "\t" + str(Dict_ATC_CID_SET[i][1])+"\n")
print(Dict_ATC_CID_SET)
print(len(Dict_ATC_CID_SET))