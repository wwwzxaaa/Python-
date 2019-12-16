
import os
import pandas as pd
import numpy as np
from pandas import DataFrame


df_c = pd.read_csv(r"E:/work/D.csv",sep=',',header=None)

def replace(d):
    print(d)
    return(df_c[df_c[0]==d][1].values[0])
def fun(file_df):
    df=file_df[file_df['d_ID'].isin(df_c[0])]
    df['d_ID']=df['d_ID'].apply(replace)
    return df
for filename in os.listdir('E:/work/subcomp1/'):
    file=os.path.join(os.path.abspath('E:/work/subcomp1/'),filename)
    file_df=pd.read_table(file,names=['d_ID','value'])
    print(file_df)
    df_res=fun(file_df)
    df_res.to_csv('E:/work/subcomp_replace/%s'%filename,index=None,header=None)

# def output2excel(file_dir):
#     '''
#     把文件夹下的文件名称输出到文件目录
#     :param file_dir: 文件目录
#     :return:
#     '''
#     # 获取文件目录下所有文件名，存入data列表
#     data = get_file_name(file_dir)
#
#     # 把data输出到该目录下，并以目录名保存为excel格式
#     wb = openpyxl.Workbook()
#     sheet = wb.active
#     # 设置表名为文件目录名
#     # sheet.title = file_dir
#     for i in range(1, len(data) + 1):
#          sheet['A{}'.format(i)] = data[i - 1]
#     wb.save('E:/work/data1.xlsx'.format(file_dir))
# output2excel(file_dir)

