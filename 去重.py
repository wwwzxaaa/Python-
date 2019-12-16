import shutil
a=0
readDir = "E:\work\\text\\atc_s1.txt"  #old
writeDir = "E:\work\\text\\atc_s2.txt" #new
lines_seen = set()
outfile = open(writeDir, "w")
f = open(readDir, "r")
for line in f:
  if line not in lines_seen:
    a+=1
    outfile.write(line)
    lines_seen.add(line)
    print(a)
    print('\n')
outfile.close()
print("success")