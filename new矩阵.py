ATC_CID_SET = open("E:/work/end_chemical1.csv","r")
W_ATC_CID_SET = open("E:/work/text/similatity1.txt","w")
R_ATC_CID_SET = ATC_CID_SET.readlines()
Dict_ATC_CID_SET =[]
List_ATC_CID_SET = []
temp = []
for i in range(len(R_ATC_CID_SET)):
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[0])
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[1:1025])
    List_ATC_CID_SET.append(temp)
    temp = []
    length=len(List_ATC_CID_SET)
#print(List_ATC_CID_SET)
temp01 = []

for i in range(1,length-1):
    for j in range(i+1,length-1):
        key = List_ATC_CID_SET[i][0] + '\t' +List_ATC_CID_SET[j][0]
        sum1 = 0
        sum2 = 0
        for a in range(0, 1023):

            if (List_ATC_CID_SET[i][1][a] == '1') & (List_ATC_CID_SET[j][1][a] == '1'):
                sum1 = sum1 + 1
            if (List_ATC_CID_SET[i][1][a] == '1') | (List_ATC_CID_SET[j][1][a] == '1'):
                sum2 = sum2 + 1
            if sum2 != 0:
                value = round(sum1/sum2,6)
                temp01.append(key)
                temp01.append(value)
                Dict_ATC_CID_SET.append(temp01)
                temp01 = []
for i in range(len(Dict_ATC_CID_SET)):
    W_ATC_CID_SET.write(Dict_ATC_CID_SET[i][0] + "\t" + str(Dict_ATC_CID_SET[i][1])+"\n")
