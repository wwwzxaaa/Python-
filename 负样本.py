''''''
import pandas as pd
import random
df1 = pd.read_csv("F:/new_zhengyangben.csv",header=None)
df2 = pd.read_csv("F:/feikongdepathway.csv",header=None)
# print(type(df2))
df_concat = pd.DataFrame()
for i in range(10):
    print(i+1) #第一份...
    print("----------")
    c_name = list(set(df1[1][df1[4]==(i+1)]))
    # print(c_name)
    p_old = df1[[0,1]][df1[4]==(i+1)]
    p_new = df1[[0,1]][df1[4]==(i+1)].reset_index()   # 第一份中的正样本组合
    list2 = [] #存放负样本
    for j in range(len(df2)):
        print(j)
        for k in range(len(c_name)):
            # print(k)
            c_full = [df2[0][j] , c_name[k]] #第一份C与所有pathway的组合；
            # print(c_full)
            if c_full not in p_old.values.tolist():  #作比较
                fu_yangben = [df2[0][j],c_name[k],'N',i+1]#i+1用于标识第几份
                # print(fu_yangben)
                list2.append(fu_yangben)
    list_neg = random.sample(list2,len(p_old))
    # print(list_neg)
    # print(len(list_neg))
    df_neg = pd.DataFrame(list_neg)
    print(df_neg)  # 第一份

    df_concat = pd.concat([df_concat,df_neg])
    print("=============")
df_concat.to_csv("F:/new_fuyangben9.csv",index=False,header=False)




