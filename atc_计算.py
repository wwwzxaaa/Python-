ATC_CID_SET = open("E:\python\\text\\分割后的atc.csv","r")
W_ATC_CID_SET = open("E:\python\\text\similatity_atc.txt","w")
R_ATC_CID_SET = ATC_CID_SET.readlines()
Dict_ATC_CID_SET =[]
List_ATC_CID_SET = []
temp = []
for i in range(len(R_ATC_CID_SET)):
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[0])
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[1:])
    List_ATC_CID_SET.append(temp)
    temp = []
#print(List_ATC_CID_SET)
temp01 = []
for i in range(1467):
    for j in range(i+1,1467):
        # 交集+1/并集+1
        key = List_ATC_CID_SET[i][0] + '\t' +List_ATC_CID_SET[j][0]
        numerator = (len(set(List_ATC_CID_SET[i][1])&set(List_ATC_CID_SET[j][1]))) + 1
        denominator = (len(set(List_ATC_CID_SET[i][1])|set(List_ATC_CID_SET[j][1]))) + 1
        value = round(numerator/denominator,6)
        temp01.append(key)
        temp01.append(value)
        Dict_ATC_CID_SET.append(temp01)
        temp01 = []
for i in range(len(Dict_ATC_CID_SET)):
    W_ATC_CID_SET.write(Dict_ATC_CID_SET[i][0] + "\t" + str(Dict_ATC_CID_SET[i][1])+"\n")
print(Dict_ATC_CID_SET)
print(len(Dict_ATC_CID_SET))

