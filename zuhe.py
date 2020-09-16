
fo = open('E:\work\\xunlian\\all9.txt', 'w')
for name in ['E:\work\\fuyangben\\n9.txt','E:\work\\fuyangben\\z9.txt']:
    fi = open(name)
    while True:
        s = fi.read(16*1024)
        if not s:
            break
        fo.write(s)
    fi.close()
fo.close()
