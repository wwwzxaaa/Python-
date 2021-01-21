import pandas as pd
import csv
# 文件处理函数(分割文件)
def data_handle(filename):
    # 因为+和空格混合，因此使用正则表达式提取数据
    import re
    p = re.compile('\s+(\d+?)\s{8}([\s\S]+?)\s{8}([\s\S]+?)\s{3}([\s\S]+?)\s{3}([\s\S]+?)\s+')

    # 将数据写到一个字典中，可以直接导入
    data = {'inst#': [], 'actual': [], 'predicted': [], 'error': [], 'prediction': []}

    with open(filename, 'r', encoding='utf-8') as f1:
        for i in range(6):
            c = f1.readline().strip('\n')
        while c:
            try:
                res_c = p.findall(c)[0]
            except:
                print('error content: %s' % c)
                break
            data['inst#'].append(res_c[0])
            data['actual'].append(res_c[1])
            data['predicted'].append(res_c[2])
            data['error'].append(res_c[3])
            data['prediction'].append(res_c[4])
            c = f1.readline().strip('\n')
    return data


# 调用文件处理函数进行分割
for i in range(10):
    path = 'E:\work\weka\weka0\qb20\SMOC1.0\\'+str(i)+'.txt'
    data = data_handle(path)
    RF_best = pd.DataFrame(data, columns=['inst#', 'actual', 'predicted', 'error', 'prediction'])
    RF_best.head()

    # 将'prediction'这一列复制两次
    RF_best['true_prediction'] = RF_best['prediction']
    RF_best['copy_prediction'] = RF_best['prediction']
    # 计算1-'copy_prediction'这一列
    RF_best['copy_prediction'] = RF_best['copy_prediction'].apply(lambda x: 1 - float(x))
    # 将'predicted'列值为'2:F'的行中的'true_prediction'值修改为对应行的'copy_prediction'值
    RF_best.loc[RF_best['predicted'] == '2:F', 'true_prediction'] = RF_best['copy_prediction']
    # 删除'copy_prediction'列
    RF_best = RF_best.drop(columns=['copy_prediction'])
    RF_best.head()
    aa = 'true_prediction_'+str(i)+'.txt'
    RF_best.to_csv(aa, sep='\t', index=None)
#
listre = []
for i in range(10):
    aa = 'true_prediction_' + str(i) + '.txt'
    f = open(aa,'r')
    str1 = f.read()
    f.close()
    list1 = str1.splitlines()
    del list1[0]
    listre = listre + list1
for i in range(len(listre)):
    listre[i] = listre[i].split('\t')
    listre[i][0] = i+1
header = ['1','2','3','4','5','6']
list_result = []
for i in range(len(listre)):
    dic = {header[j]:listre[i][j] for j in range(len(header))}
    list_result.append(dic)
with open('qb20-smo.csv','a',newline = '',encoding='utf-8') as f:
    w = csv.DictWriter(f,fieldnames=header)
    w.writeheader()
    w.writerows(list_result)
