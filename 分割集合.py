f1 = open("E:\work\\text\\end_ATC1.csv", "r")
list1 = f1.readlines()
len1 = len(list1)

list_cid = []
for i in range(len1):
    list_cid.append(list1[i].strip("\n").split(("\t")))
len_ = len(list_cid)

d1 = {}

for i in range(len_):
    item = list_cid[i]
    cid = item[0]
    atc = item[2]
    atc_set = atc[0] + "\t" + atc[0:3] + "\t" + atc[0:4] + "\t" + atc[0:5] + "\t" + atc[0:7]
    print (atc_set)