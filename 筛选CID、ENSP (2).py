import pandas as pd
# from pandas import DataFrame
#
# # df=pd.read_csv(r"E:\work\drug\sum_drug.csv",sep=',',header=None)
# # # df=pd.read_table(r"E:\work\CID0.txt",sep='\t',header=None)
# # df1=pd.read_csv(r"E:\work\drug\\text1.csv",sep=',',header=None)
# # df=df[df[0].isin(df1[0])]
# # # 将筛选后的新文件输出
# # df.to_csv(r"E:\work\drug\end_drug.csv",index=False)
# df = pd.read_csv("E:\work\drug\end_drug.csv",header=None)
# df = df.drop_duplicates(keep='last')
# df.to_csv(r"E:\work\drug\drug-effect.csv",index=False)
import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5) # 从list中随机获取5个元素，作为一个片断返回
print (slice)