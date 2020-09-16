f1 = open("E:\work\drug\drugs.txt","r")
list_d = f1.readlines()
len1 = len(list_d)
drugs = []
for d in range(len1):
    drugs.append(list_d[d].strip("\n"))
len_d = len(drugs)
print(drugs)
print(len_d)

f2 = open("E:\work\drug\effect.txt","r")
list_s= f2.readlines()
len2 = len(list_s)
side_effect = []
for s in range(len2):
    side_effect.append(list_s[s].strip("\n"))
len_s = len(side_effect)
print(len_s)
drug_side_effect = []
for i in range(len_d):
    for j in range(len_s):
        drug_side_effect.append(drugs[i]+'\t'+side_effect[j])
len_ds = len(drug_side_effect)
print (len_ds)
#
fw = open("sample1.txt","w")
for line in range(len_ds):
    fw.writelines(drug_side_effect[line] + "\n")
fw.close()
print("save")


