compound2side_effect = open("text1.csv","r")
compound2side_effect_list = compound2side_effect.readlines()
compound2side_effect_list_1 = []
compound2side_effect_dict = {}
list_length = len(compound2side_effect_list)
for i in range(list_length):
    compound2side_effect_list_1.append(compound2side_effect_list[i].strip("\n").split("\t"))
list_length1 = len(compound2side_effect_list_1)

i = 1
for i in range(list_length1):
    c1 = compound2side_effect_list_1[i-1]
    c2 = compound2side_effect_list_1[i]
    # print(c1[0])
    if c1[0] == c2[0]:
        compound2side_effect_dict.setdefault(c1[0], set()).add(c2[1])
    else:
        compound2side_effect_dict.setdefault(c2[0],set()).add(c2[1])
#
len_d = len(compound2side_effect_dict)

man_file=open('text2.csv','w')
print(compound2side_effect_dict, file=man_file)
man_file.close()