import random

fr = open("E:\work\ceshi\\np1.txt","r")
list_n= fr.readlines()
len_n = len(list_n)
negative_sample = []
for s in range(len_n):
    negative_sample.append(list_n[s].strip("\n").split("\t"))
len_negative = len(negative_sample)

# print(len_negative)
# print(negative_sample)

negative_sample3 = random.sample(negative_sample, 13976) # 从list中随机获取5个元素，作为一个片断返回
# print (negative_sample1)
# print (len(negative_sample1)) # 原有序列并没有改变

len2 = len(negative_sample3)

fw = open("E:\work\\fuyangben\\n9.txt","w")
for line in range(len2):
    str1 =negative_sample3[line]
    s = str1[0] + "\t" + str1[1] + "\n"
    fw.write(s)
fw.close()
print("save")
