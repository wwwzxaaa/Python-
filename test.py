# 正式代码

import pandas as pd
import numpy as np
import os
from pandas import DataFrame
list_file = os.listdir('C:\\Users\\lenovo\\Desktop\\no')
for m in range(len(list_file)):
    filename = 'C:\\Users\\lenovo\\Desktop\\no\\'+list_file[m]
    RF_true_best = pd.read_csv(filename,sep=',',header=0)
    # print(RF_true_best['5'])
    f = pd.DataFrame({'TP':[],'FN':[],'FP':[],'TN':[],'P':[],'R':[],'FPR':[],'TPR':[]})
    for i in np.arange(0,1.00,0.01):
        RF_true_best['test'] = i
        # 先找出类别为'2:c0'的
        RF_true_best.loc[RF_true_best['test'] < RF_true_best['6'],'5'] = '1:T'
        # 再找出类别为'1:c1'的
        RF_true_best.loc[RF_true_best['test'] >= RF_true_best['6'],'5'] = '2:F'
        TP=0
        FN=0
        FP=0
        TN=0
        P=0
        R=0
        FPR=0
        TPR=0
        # 统计4种类型个数
        # print(RF_true_best)
        for j in range(RF_true_best.shape[0]):
            if RF_true_best.loc[j,'2']=='1:T' and RF_true_best.loc[j,'5']=='1:T':
                TP+=1
            elif RF_true_best.loc[j,'2']=='1:T' and RF_true_best.loc[j,'5']=='2:F':
                FN+=1
            elif RF_true_best.loc[j,'2']=='2:F' and RF_true_best.loc[j,'5']=='1:T':
                FP+=1
            elif RF_true_best.loc[j,'2']=='2:F' and RF_true_best.loc[j,'5']=='2:F':
                TN+=1
        # print(TP,FN,FP,TN)
    #      # 计算坐标
        P = TP/(TP+FP)
        R = TP/(TP+FN)
        FPR=FP/(FP+TN)
        TPR=TP/(TP+FN)
        print(P,R,FPR,TPR)
        e = pd.DataFrame({'TP':[TP],'FN':[FN],'FP':[FP],'TN':[TN],'P':[P],'R':[R],'FPR':[FPR],'TPR':[TPR]})
    #     f = f.append(e,ignore_index=True,sort=False)
        f = pd.concat([f,e],axis=0,ignore_index=True,sort=False)
        aa = list_file[m]
    f.to_csv(aa,index=False)