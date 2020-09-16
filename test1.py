#coding=utf-8


f1 = open("E:\work\\ceshi\\Fall0.txt", "r")
# f1 = open("negative_sample_set1.txt", "r")
list1 = f1.readlines()
positive_set = []
len1 = len(list1)
for i in range(len1):
    positive_set.append(list1[i].strip("\n").split("\t"))
len_positive = len(positive_set)

f2 = open("E:\work\\file\\chemicall.txt", "r")
list2 = f2.readlines()
len2 = len(list2)
screen_values = []
for i in range(len2):
    screen_values.append(list2[i].strip("\n").split("\t"))
len_screen_values = len(screen_values)
# print(screen_values[2])

d1 = {}
i = 1
for i in range(len_positive):
    c1 = positive_set[i-1]
    c2 = positive_set[i]
    if c1[1] == c2[1]:
        d1.setdefault(c1[1], set()).add(c2[0])
    else:
        d1.setdefault(c2[1],set()).add(c2[0])


def writetxt(ss):
    with open("result1.txt","a+",encoding="utf-8") as f:
        f.write(str(ss))
        f.write("\n")


max_screen_values = []
#----------------------------------------------------------------------------------------
for j in range(len_positive):
    p1 = positive_set[j]
    p1_ = p1[1]
    key_values = d1.get(p1_,())
    values = []

    for i in range(len_screen_values):
        cc = screen_values[i]
        if p1[0] == cc[0] and cc[1] in key_values:
            values.append(cc[2])

    if values:
        max_t = max(values)
        print(max_t )
        writetxt(max_t)
    else:
        max_t = 0
        print(max_t)
        writetxt(max_t)