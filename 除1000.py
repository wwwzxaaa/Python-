import pandas as pd

data = pd.read_csv('E:\work\weka\weka4\初始文件\\cclink.csv',header=None,encoding="utf-8",sep=",",index_col=False)

# new_data=[]
# for i in range(len(data)-1):
# print(type(data))
data1=data.div(1000, axis='rows')
data1.to_csv(r"E:\work\weka\weka4\初始文件\\cclink3.txt",index=False)

#     for j in range(data[i].count()):
#         new_data=str(data[i][j]/1000)+'\r'
#         print(new_data)


# fw = open("测试chem结果.txt", "w")
# for line in range(len(cid_vector_value)):
#     fw.writelines(cid_vector_value[line] + "\n")
# fw.close()
# print("save")