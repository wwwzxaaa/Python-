# coding:utf-8


# fo = open('E:\work\weka\weka0\qb40\\file\\xall0.csv', 'w')
# for name in ['E:\work\weka\weka0\qb40\data\\call1.csv','E:\work\weka\weka0\qb40\data\\call2.csv','E:\work\weka\weka0\qb40\data\call3.csv','E:\work\weka\weka0\qb40\data\call4.csv','E:\work\weka\weka0\qb40\data\call5.csv','E:\work\weka\weka0\qb40\data\call6.csv','E:\work\weka\weka0\qb40\data\call7.csv','E:\work\weka\weka0\qb40\data\call8.csv','E:\work\weka\weka0\qb40\data\call9.csv','E:\work\weka\weka0\qb40\data\\xall1.csv','E:\work\weka\weka0\qb40\data\\xall2.csv','E:\work\weka\weka0\qb40\data\\xall3.csv','E:\work\weka\weka0\qb40\data\\xall4.csv','E:\work\weka\weka0\qb40\data\\xall5.csv','E:\work\weka\weka0\qb40\data\\xall6.csv','E:\work\weka\weka0\qb40\data\\xall7.csv','E:\work\weka\weka0\qb40\data\\xall8.csv','E:\work\weka\weka0\qb40\data\\xall9.csv']:
#     fi = open(name)
#     while True:
#         s = fi.read(16*1024)
#         if not s:
#             break
#         fo.write(s)
#     fi.close()
# fo.close()




fo = open('E:\work\weka\weka3\qb30\\file\call9.csv', 'w')
for name in ['E:\work\weka\weka3\qb30\data\\call9.csv','E:\work\weka\weka3\qb30\data\\xall9.csv']:
    fi = open(name)
    while True:
        s = fi.read(16*1024)
        if not s:
            break
        fo.write(s)
    fi.close()
fo.close()