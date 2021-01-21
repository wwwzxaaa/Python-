import os
import re


def getOneValue(txtPath, decimalsValue):
    beforeList = []
    afterList = []
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
            beforeList.append(writeValue)
            afterList.append(writeValue)
        elif str(changdu).isdigit():
            writeValue = newLineList[changdu -1 ]
            beforeList.append(writeValue)
            afterList.append(writeValue)
        else:
            beforeIndex = int(changdu)
            afterIndex = int(changdu) + 1
            beforeList.append(newLineList[beforeIndex-1])
            afterList.append(newLineList[afterIndex-1])
    basePath = os.path.dirname(txtPath)
    beforeTxt = os.path.join(basePath, "20_target.txt")
    # afterTxt = os.path.join(basePath, "after.txt")
    f1 = open(beforeTxt, "a")
    # f2 = open(afterTxt, "a",)
    for i in range(fileTotalLine):
        f1.write(beforeList[i])
        f1.write("\n")
        # f2.write(afterList[i])
        # f2.write("\n")

# txt文件路径
txtPath = r"E:\work\weka\weka4\初始文件\a_target.txt"
# 百分数
decimalsValue = 0.2
getOneValue(txtPath, decimalsValue)