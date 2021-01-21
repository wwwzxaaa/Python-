#encoding=utf-8
def trimLineSpace(finput, foutput):
    fInputHandle = open(fInput)
    fOutputHandle = open(fOutput, 'w')
    lines = fInputHandle.readlines()
    for line in lines:
        fOutputHandle.write(line.strip() + '\n')
    fInputHandle.close()
    fOutputHandle.close()

if __name__ == '__main__':
    fInput = 'E:\work\weka\weka4\初始文件\\a_ecfp.txt'
    fOutput = 'E:\work\weka\weka4\初始文件\\ecfp.txt'

trimLineSpace(fInput, fOutput)

# from __future__ import division
# f1 = open("E:\work\weka\weka4\\初始文件\\a_cclink.txt", "r")
# list1 = f1.readlines()
# paixu = []
# len1 = len(list1)
# for i in range(len1):
#     paixu.append(list1[i].strip("\n").split("\t"))
# len_paixu = len(paixu)
# print(paixu)
#
# def writetxt(ss):
#     with open("E:\work\weka\weka4\\初始文件\cclink1.txt", "a+", encoding="utf-8") as f:
#         f.write(ss)
#         f.write("\n")
#
# for m in range(len_paixu):
#     # print(paixu[m])
# # paixu[0]=int(float(str(paixu[0])))
#     paixu[m].sort(reverse=True,key=int)
#     print(paixu[m])
#     writetxt(str(paixu[m]))



