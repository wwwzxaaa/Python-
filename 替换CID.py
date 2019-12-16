
import xlrd

worksheet = xlrd.open_workbook(u'E:\work\zhaoDB\\1.xlsx')

sheet_names= worksheet.sheet_names()

for sheet_name in sheet_names:
    sheet1 = worksheet.sheet_by_name(sheet_name)
    cols = sheet1.col_values(0) # 获取第二列内容
    lens=len(cols)-1
    i=0
    while lens:
        i=i+1
        data=cols[i].replace('0','CID',3)
        print(data)
