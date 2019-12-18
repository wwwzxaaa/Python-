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




    #
    # list_dict_all = []  # 创建一个空列表，全局变量，用来存放字典
    #
    #
    # def AddtoDict(str_1):  # 定义一个函数，功能：把文件里面的内容添加到字典中
    #
    #     list_str1 = str_1.split(",")  # 读取的行内容以字符串的形式显示出来, 使用‘,’分隔字符串
    #
    #     line_str = []  # 创建一个空列表，用来接收去掉'\n'的行字符串
    #     for i in list_str1:
    #         x = i.strip("\n")
    #         line_str.append(x)
    #     # print(line_str)
    #
    #     dict_all = {}  # 创建一个空字典
    #     for item in line_str:  # 遍历列表中的行内容，列表中有3个元素
    #         if item[0:3] == "url":  # 列表中的元素，前3个字符是否等于“url”
    #             dict = {
    #                 item[0:3]: item[4:]}  # dict = {'url':'http://119.23.241.154:8080/futureloan/mvc/api/member/login'}
    #             dict_all.update(dict)  # 添加dict到空字典dict_all中
    #             # print(dict_all)
    #         else:
    #             dict = {item.split(":")[0]: item.split(":")[1]}  # 除url外，取其他数据key, value到字典中
    #             dict_all.update(dict)
    #     list_dict_all.append(dict_all)