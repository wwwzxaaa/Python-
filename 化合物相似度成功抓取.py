import pandas as pd

#打开csv并读取它的文件目录
import csv
csv_reader = csv.reader(open('E:\\work\\D1.csv',encoding='utf-8'))
error_list = []
for row in csv_reader:
    try:
        path1 = 'http://rest.genome.jp/subcomp/' + ''.join(row)+'/drug/cutoff=0.1 '
        path2 = 'http://rest.genome.jp/simcomp/' + ''.join(row)+ '/drug/cutoff=0.1 '

        data1 = pd.read_csv(path1,sep='\t')
        data2 = pd.read_csv(path2,sep='\t')


        file1 = 'E:/work/subcomp1/'+ ''.join(row)+'.txt'
        file2 = 'E:/work/simcomp1/'+''.join(row)+'.txt'

        data1.to_csv(file1, sep='\t',index=False)
        data2.to_csv(file2, sep='\t', index=False)
    except Exception as result:

        print(''.join(row)+"的错误为：%s" % result)
        error_list.append(''.join(row)+"的错误为：%s" % result)
        continue
dff = pd.DataFrame()
dff['error'] = error_list
dff.to_csv('E:/work/error1.csv',index=False,encoding='utf-8')

