import pandas as pd
import re
import os
import cmath
for filename in os.listdir('E:\work\weka\weka2\qb20\MP'):
    file = os.path.join(os.path.abspath('E:\work\weka\weka2\qb20\MP'), filename)
    data = pd.read_table(file,header=None,encoding="utf-8",sep="\t",index_col=None)
    data1=data.drop(index=[0, 1])

    def writetxt(ss):
        with open("E:\work\weka\weka2\qb20\MP\\result.txt","a+",encoding="utf-8") as f:
            f.write(ss)
            f.write("\n")
    for i in range(2,len(data1)+2):
        # print(data1[0][i])
        p = re.compile('(?<=:)\w')
        s1=list(map(str,p.findall(data1[0][i])))
    # # data1['split'] = data1[0] .str.split('\s')
        all_s=s1[0]+s1[1]
        print(all_s)
        writetxt(str(all_s))