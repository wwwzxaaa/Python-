ATC_CID_SET = open("E:\work\\text\\t.csv","r")
W_ATC_CID_SET = open("E:\work\\text\\t2.csv","w")
R_ATC_CID_SET = ATC_CID_SET.readlines()
Dict_ATC_CID_SET =[]
List_ATC_CID_SET = []
temp = []
for i in range(len(R_ATC_CID_SET)):
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[0])
    temp.append(R_ATC_CID_SET[i].strip("\n").split(",")[1:])
    List_ATC_CID_SET.append(temp)
    temp = []
temp01 = []
for i in range(1,1094):
    for j in range(1,1094):
        for m in range(0,1093):
            if List_ATC_CID_SET[0][1][m]==List_ATC_CID_SET[i][0]:
                List_ATC_CID_SET[i][1][m]=1
                key=List_ATC_CID_SET[i][0]
                value=List_ATC_CID_SET[i][1]
                temp01.append(key)
                temp01.append(value)
                Dict_ATC_CID_SET.append(temp01)
                temp01 = []
W_ATC_CID_SET.write(Dict_ATC_CID_SET)
