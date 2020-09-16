import random
f = open('E:\work\ceshi\\zheng.txt','r') #打开文件
list = f.readlines()
len1 = len(list)
list0 = []
for d in range(len1):
    list0.append(list[d].strip("\t"))
random.shuffle(list0)


# i = 0 #设置计数器
# while i<139733 : #这里12345表示文件行数，如果不知道行数可用每行长度等其他条件来判断
#     with open('E:\work\ceshi\\z1'+str(i)+'.txt','w') as f1:
#         for j in range(0,13973) : #这里设置每个子文件的大小
#             if i < 139733 : #这里判断是否已结束，否则最后可能报错
#                 f1.write(newlist)
#                 i = i+1
#             else:
#                 break

