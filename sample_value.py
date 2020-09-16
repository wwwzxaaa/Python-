#coding=utf-8
import pandas as pd

typedict={2:str}

# 这个放特征
data = pd.read_table("E:\work\\file\\t_cid.txt",header=None,encoding="utf-8",dtype=typedict,sep="\t",index_col=0)
data1 = pd.read_table("E:\work\\file\\t_cid.txt",header=None,encoding="utf-8",dtype=typedict,sep="\t")
#print(data.index)
print(data1[2])
//这里
#print("-----------------")
# 这个是提取某一个值
#cc = data.loc["CID071306834"]
#print(cc)
#print("======================")
#print(cc.values.tolist())


# data2 = pd.read_table("E:\work\ceshi\Fall0.txt",header=None,encoding="utf-8",sep="\t")
# data3 = pd.read_table("E:\work\ceshi\Fall0.txt",header=None,encoding="utf-8",sep="\t",index_col=1)
# print(data3)
# data2list = data2[0].tolist()
# print(len(data2list))
# # 逻辑  遍历第二个，如果第一个里边有，找到所有的，然后看第二个是否在data2，如果在就计入列表
# # 然后  这个完事儿之后找到一个最大值
#
# rr = data.isin(data2list)
# #print(rr)
#
# rr[2]=data1[0]
# rr[3]=data1[2]
# rr.set_index([2],inplace=True)
# #print(rr)
#
# print("================================================================")
#
# def writetxt(ss):
#     with open("t2.txt","a+",encoding="utf-8") as f:
#         f.write(ss)
#         f.write("\n")
#
# total = []
# print(len(data2))
# b=0
# for i in range(len(data2)):
#     print("==================================",b)
#     b=b+1
#     try:
#         d=data2[0][i]
#         ff=data2[1][i]
#         #print(d)
#         temp=[]
#         dc = data.loc[d]
#         #print("dddddddddddddddddddddddddddddddddddddd")
#         #print(dc)
#
#         rr = data3.loc[ff]
#         pilist = rr[0].tolist()
#         #print("cccccccccccccccccccccccccccccccccccccccccccccccc")
#         #print(dc)
#         dcc=dc.set_index(2)
#         #print(dcc)
#         #print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
#         rrr = dcc.isin(pilist)
#         #print(rrr)
#         rrr=rrr[1].tolist()
#         for r in range(len(rrr)):
#             if rrr[r]:
#                 temp.append(float(dc[2][r]))
#         if temp:
#             #print(temp)
#             t = max(temp)
#             print(t)
#             writetxt(str(t))
#             total.append(t)
#         else:
#             writetxt(str(0))
#     except:
#         try:
#             d = data2[0][i]
#             ff = data2[1][i]
#             # print(d)
#
#             dc = data.loc[d]
#             # print("dddddddddddddddddddddddddddddddddddddd")
#             # print(dc)
#             rr = data3.loc[ff]
#             pilist = rr[0].tolist()
#             if dc[1] in pilist:
#                 writetxt(str(dc[2]))
#             else:
#                 writetxt(str(0))
#         except:
#             writetxt(str(0))
#             pass
#
#
#
#
#
#
#
#
#
#




