import re
import os
import sys
filePath = os.path.abspath(__file__)
curPath = os.path.dirname(filePath)
projectPath = os.path.dirname(curPath)
sys.path.append(projectPath)

def getOneLine(txtFile, dealTxt ,decimalsValue):
    with open(txtFile, "r") as f:
        lines = f.readlines()
    listLenList = []
    newLineList = []
    for line in lines:
        lineList = re.split("\t", line)
        lineList[-1] = lineList[-1].replace("\n", "")
        listLenList.append(len(lineList))
        newLineList.append(lineList)
    maxCount = max(listLenList)
    lineCount = int(maxCount * decimalsValue)
    f = open(dealTxt, "a")
    for newList in newLineList:
        if len(newList) < lineCount:
            addCount = lineCount - len(newList)
            for a in range(addCount):
                newList.append("0")
        else:
            newList = newList[:lineCount]
        wLine = "\t".join(newList)
        f.write(wLine)
        f.write("\n")
    f.close()
        


if __name__ == "__main__":
    txtFile = os.path.join(projectPath, "data", "text.txt")
    dealFile = os.path.join(projectPath, "data", "deal.txt")
    # 填要处理的文件位置
    txtFile = r"E:\work\weka\weka4\初始文件\atc.txt"
    # # # 填要输出到那个文件的位置
    dealFile = r"E:\work\weka\weka4\初始文件\qb40_atc.txt"
    decimalsValue = 0.4
    getOneLine(txtFile, dealFile, decimalsValue)
    
