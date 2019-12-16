import xlrd
import pandas as pd
from pandas import DataFrame
worksheet = xlrd.open_workbook(u'E:\work\zhaoDB\\text.xlsx')
sheet_names= worksheet.sheet_names()

for sheet_name in sheet_names:

    sheet1 = worksheet.sheet_by_name(sheet_name)
    cols = sheet1.col_values(1) # 获取第二列内容
    # s=''.join(map(str,[cols]))
    lens=len(cols)-1
    i=0

    while lens:
        i = i + 1
        f = "%012d" % cols[i]
        a = f.split('\t')
        print(a[0])


        # a = f.split('\t')

        # t = open("E:\work\zhaoDB\\text1.txt", "w")
        # with open('E:\work\zhaoDB\\text1.txt', 'w') as t:
        #     t.write('\n'.join(a))
