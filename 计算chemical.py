# ATC_CID_SET = open("测试chemical.csv","r")
# W_ATC_CID_SET = open("测试chemical结果.txt","w")
# R_ATC_CID_SET = ATC_CID_SET.readlines()
# Dict_ATC_CID_SET =[]
# List_ATC_CID_SET = []
# temp = []
# for i in range(len(R_ATC_CID_SET)):
#     temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[0])
#     temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[1:1025])
#     List_ATC_CID_SET.append(temp)
#     temp = []
#     length=len(List_ATC_CID_SET)
# # print( List_ATC_CID_SET[length-1])
# temp01 = []
#
# for i in range(length-1):
#     for j in range(length-1):
#         # print(List_ATC_CID_SET[i])
#         key = List_ATC_CID_SET[i][0] + '\t' +List_ATC_CID_SET[j][0]
#         sum1 = 0
#         sum2 = 0
#         for a in range(0, 1023):
#             if (List_ATC_CID_SET[i][1][a] == '1') & (List_ATC_CID_SET[j][1][a] == '1'):
#                 sum1 = sum1 + 1
#             elif (List_ATC_CID_SET[i][1][a] == '1') | (List_ATC_CID_SET[j][1][a] == '1'):
#                 sum2 = sum2 + 1
#             if sum2 != 0:
#                 value = round(sum1/sum2,6)
#                 print(value)
#                 temp01.append(key)
#                 temp01.append(value)
#                 Dict_ATC_CID_SET.append(temp01)
#                 temp01 = []
# for i in range(len(Dict_ATC_CID_SET)):
#     W_ATC_CID_SET.write(Dict_ATC_CID_SET[i][0] + "\t" + str(Dict_ATC_CID_SET[i][1])+"\n")
#encoding: UTF-8
"""
@author = 万玉文
@email = 1554091920@qq.com
@create_time =  21:36
"""
import pandas as pd
from tqdm import tqdm
tqdm.pandas(desc='pandas bar')

def data_analysis(df):
    li = []
    df1 = df.__deepcopy__()
    for index,row in tqdm(df.iteritems()):
        for index1,row1 in df1.iteritems():
            re_dic = {}
            results = pd.DataFrame()
            results[index] = row + row1
            sum1 = results[index].sum() # 分母
            sum2 = results[results[index]==2].count()[index] # 分子
            re_dic['cid1'] = index
            re_dic['cid2'] = index1
            re_dic['value'] = round(sum2/sum1,6)
            li.append(re_dic)
            tmp = index
        # df1.drop([tmp],axis=1,inplace=True)
    data = pd.DataFrame(li)
    return data

def read_data(file_name):
    return pd.read_csv(file_name,header=None).T

def read_temp():
    return pd.read_csv('temp.csv',skiprows=1)

def save_results(df,file_name):
    df.to_csv(file_name,index=0)

if __name__ == '__main__':
    file_name = 'end_chemical1.csv'
    df = read_data(file_name)
    save_results(df,'temp.csv')
    df = read_temp()
    df = data_analysis(df)
    save_results(df,'result.csv')