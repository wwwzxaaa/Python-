import pandas as pd
import re
data = pd.read_table('E:\work\\10.23\\atc.txt',header=None,encoding="utf-8",sep="\t",low_memory=False,index_col=None)
for i in range(len(data)):
    str1 = str(data[0][0])
    # m = re.findall('\[\'([^"]+)\'\]', str1)
    # pattern = re.compile("'(.*)'")
    # m=pattern.findall(str1)
    m= re.findall(r'\d+\.?\d*', str1)
    for item in m:

        if not item.isdigit():
            print(item + ' ', end = '' +'\n')


import pandas as pd

def text_save(filename, data):#filename为写入文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','') #去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','')   #去除单引号，逗号，每行末尾追加换行符
        print(s)
        file.write(s)
    file.close()
    print("保存成功")

data1 = pd.read_table('E:\work\\10.23\\atc.txt',header=None,encoding="utf-8",sep="\t",low_memory=False,index_col=None)
for j in range(0,2):
    # str1 = str(data[0][j])
    text_save('E:\work\\10.23\\atc1.txt', data1[0][j])