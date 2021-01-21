file1 = open(r'E:\work\weka1\前10\p100i100\0.txt',  mode='r')
file2 = open(r'E:\work\weka1\前10\p100i100\t_0.txt', 'a+')
line = file1.readline()
i = 0
while line:
    if i < 4:
        i = i+1
        line = file1.readline()
    else:
        line = file1.readline()
        list1 = line.split(' ')
        list2 = [j for j in list1 if(len(str(j))!=0)]
        print(list2)
        a = list2[1]
        b = list2[2]
        a = a[-2:]
        c = 'P'
        if(a[0] == c):
            a = a[-1]
        b = b[-2:]
        if (b[0] == c):
            b = b[-1]
        file2.write(a)
        file2.write('   ')
        file2.write(b)
        file2.write('\n')
file1.close()
file2.close()
