import shutil
a=0
readDir = "E:/python/text/protein_result.txt"  #old
writeDir = "E:/python/text/protein_result1.txt" #new
lines_seen = set()
outfile = open(writeDir, "w")
f = open(readDir, "r")
for line in f:
  a += 1
  if line not in lines_seen:
    outfile.write(line)
    lines_seen.add(line)
    print(a)
    print('\n')
outfile.close()
print("success")