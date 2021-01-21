#coding=utf-8
import pandas as pd
import re
import os
import math

data = pd.read_table('E:\work\weka\weka2\qb20\MP\\result.txt',header=None,encoding="utf-8",sep="\t",index_col=False)
len_tf=len(data[0])
TP=0
FP=0
FN=0
TN=0
SN=0
SP=0
ACC=0
MCC=0
Precision=0
F1_measure=0
for i in range(len_tf):
    if data[0][i]=='TT':
        TP+=1
    if data[0][i]=='FT':
        FP+=1
    if data[0][i] == 'TF':
        FN+=1
    if data[0][i] == 'FF':
        TN+=1

print(TP,FP,FN,TN)
SN=TP/(TP+FN)
SP=TN/(TN+FP)
ACC=(TP+TN)/(TP+TN+FP+FN)
MCC=((TP*TN)-(FP*FN))/math.sqrt((TN+FN)*(TN+FP)*(TP+FN)*(TP+FP))
Precision=TP/(TP+FP)
F1_measure=(2*Precision*SN)/(Precision+SN)
print(SN,SP,ACC,MCC,Precision,F1_measure)



