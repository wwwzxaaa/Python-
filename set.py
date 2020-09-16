fr = open("E:\work\drug\负样本\\negative_sample2.txt","r")
list_n= fr.readlines()
len_n = len(list_n)

arry = list(set(list_n))
lena = len(arry)
# print(list_n)
print(len_n)
print(lena)