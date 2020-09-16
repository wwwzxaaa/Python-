
# f1 = open("E:\work\drug\drug-effect1.csv","r")
# list_ds = f1.readlines()
# len1 = len(list_ds)
# drug_side = []
# for d in range(len1):
#     drug_side.append(list_ds[d].strip("\n").split("\t"))
# len_d = len(drug_side)
# print(drug_side[0])
#
#
# f2 = open("sample1.txt","r")
# list_s= f2.readlines()
# len2 = len(list_s)
# sample = []
# for s in range(len2):
#     sample.append(list_s[s].strip("\n").split("\t"))
# len_s = len(sample)
#
# print(sample[0])
#
# nagetive_sample_set = [item for item in sample if item not in drug_side]
#
# len_nagetive = len(nagetive_sample_set)
#
# # print(nagetive_sample_set)
# # print(len_d)
# # print(len_s)
# # print(len_nagetive)
# if __name__=="__main__":
#     fw = open("total_nagetive_sample1.txt","w")
#     for line in range(len_nagetive):
#         str1 = nagetive_sample_set[line]
#         s = str1[0] + "\t" + str1[1] + "\n"
#         fw.write(s)
#     fw.close()
#     print("save")