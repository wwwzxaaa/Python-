#coding=utf-8
import pandas as pd
import re
import os
for filename in os.listdir('E:/work/tezheng/c1.2e1.0/'):
    file = os.path.join(os.path.abspath('E:/work/tezheng/c1.2e1.0/'), filename)
    data = pd.read_table(file,header=None,encoding="utf-8",sep="\t",index_col=None)
    data1=data.drop(index=[0, 1])

    def writetxt(ss):
        with open("E:\work\\tezheng\\t_1.txt","a+",encoding="utf-8") as f:
            f.write(ss)
            f.write("\n")
    for i in range(2,len(data1)+2):
        # print(data1[0][i])
        p = re.compile('(?<=:)\w')
        s1=list(map(str,p.findall(data1[0][i])))
    # # data1['split'] = data1[0].str.split('\s')
        print(s1[0]+s1[1])
        writetxt(str(s1))


