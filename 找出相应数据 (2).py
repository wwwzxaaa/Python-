# import csv
# csvFile = open("./data1.csv",'w',newline='',encoding='utf-8')
# writer = csv.writer(csvFile)
# csvRow = []
#
# f = open("E:\work\\text\\t1.txt",'r',encoding='GB2312')
# for line in f:
#     csvRow = line.split()
#     writer.writerow(csvRow)
#
# f.close()
# csvFile.close()
# import csv
#
# with open("data1.csv", "r") as F1:  #文件1是原始文件，有两列
#     # 使用空格作为分隔符拆分文件并将其读取到内存：
#     F1_d = sorted(csv.reader(F1,delimiter=' '))
#
# with open("data.csv", "r") as F2:  #保存数据集的位置
#     # 再次使用空格拆分文件，并将其读入字典
#     # 由第二列和第四列索引的结构：
#     F2_d = {(col[0], col[1]): col for col in csv.reader(F2,delimiter=' ')}
#
# with open("data2.csv", "w") as F3: #存在相同的地方
#     for match1 in F1_d:
#         if tuple(match1) in F2_d: #使用定义的索引搜索匹配项
#             F3.write(' '.join(F2_d[match1]) + '\n')
rd3 = open('data.csv')

base = open('data1.csv')

wr3 = open('data2.csv','w+')

bsData = base.readlines()

i = 1

for key in rd3:
    if key in bsData:
        wr3.write(key)
        if i == 1:
            print(key)
            i = (i + 1)%100

rd3.close()

base.close()

wr3.close()