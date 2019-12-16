import pandas as pd
from pandas import DataFrame

da = pd.read_csv('E:\work\china\\after\\1.csv', sep=',', low_memory=False, header=0)
wb = pd.read_csv('E:\\work\\china\\after\\wangba.csv', sep=',', low_memory=False, header=0)
#打开表1和表2，pd.read_csv(“路径”，“以，为分隔符”，“采用较大的数据类型来储存”)
wb = wb.drop(['TITLE', 'Unnamed: 4'], axis=1)
# 计算每个网吧的上网人数
M = da['SITEID'].value_counts()
dict_m = {'SITEID': M.index, 'cishu': M.values}
df_m = pd.DataFrame(dict_m)
merged1 = pd.merge(wb, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
merged1.fillna(0, inplace=True)
merged1[['cishu']] = merged1[['cishu']].astype(int)