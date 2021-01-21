import os
import re


def writetxt(ss):
    with open("E:\work\\all_data\\text1.txt", "a+", encoding="utf-8") as f:
        f.write(ss)
        f.write("\n")
def getOneValue(txtPath, decimalsValue):
    beforeList = []
    afterList = []
    global writeValue
    with open(txtPath, "r") as f:
        lines = f.readlines()
    fileTotalLine = len(lines)


    for line in lines:
        lineList = re.split("\t", line)
        if "\n" in lineList:
            lineList.remove("\n")
        newLineList = [i for i in lineList if i !=""]
        lineNum = len(newLineList)
        changdu = lineNum * decimalsValue
        if  changdu < 1:
            writeValue = newLineList[0]
            # beforeList.append(writeValue)
            writetxt(writeValue)
        elif str(changdu).isdigit():
            for a in range(0,changdu):
                writeValue = newLineList[a]
                # beforeList.append(writeValue)
                writetxt(writeValue)
        else:
            beforeIndex = int(changdu)
            for b in range(0,beforeIndex):
                beforeList.append(newLineList[b])
            writetxt(str(beforeList))
    print('\n'.join(beforeList))


# txt文件路径
txtPath = r"E:\work\all_data\text.txt"
# 百分数
decimalsValue = 0.05
getOneValue(txtPath, decimalsValue)