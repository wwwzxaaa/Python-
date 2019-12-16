# -*- coding:utf8-*-
import re
import os
import openpyxl
from os.path import os
from xlwt.Workbook import Workbook
mypath = 'E:/work/simcomp_replace/'
myfiles = os.listdir(mypath)
fileList = []
excellist = []
for f in myfiles:
    if(os.path.isfile(mypath + '/' + f)):
        if os.path.splitext(f)[1] == '.txt':
            fileList.append(f)
# 添加文件          
for ff in fileList:
    f = open(mypath+ff,'r',encoding='utf-8')
    txt=f.read()
    f.close()
    # 把data输出到该目录下，并以目录名保存为excel格式
    wb = openpyxl.Workbook()
    sheet = wb.active
    for i in txt:
        sheet['A{}'.format(i)] = txt[i-1]
    wb.save('E:/work/data1.xlsx'.format(mypath+ff))
#f = open('D:/alltxt/test.txt', 'r',encoding='utf-8')
#     sourceInLines = f.readlines()
#     f.close()
#     for line in sourceInLines:
#         lists = []
#         temp1 = line.strip('\n')
#         lists.append(temp1)
#         excellist.append(lists)
# book = Workbook()
# sheet1 = book.add_sheet('Sheet1')
# row0 = ['CID','value']
# for i in range(len(row0)):
#     sheet1.write(0,i,row0[i])
#     for i, li in enumerate(excellist):
#         for j, lj in enumerate(li):
#             sheet1.write(i+1,j,lj)
# book.save('E:/work/result.xls')