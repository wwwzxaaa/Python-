import os
import re
input_dir = ''  # 批量处理的输入文件夹
output_dir = ''  # 批量处理的输出文件夹
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith('.3dc'): # 只匹配后缀名为'.3dc'的文件
            file_path = os.path.join(root, filename)
            print(file_path)
            f2 = open(file_path, 'r')
            for line in f2.readlines():
                x = re.split(r' ', line)[0]  # 正则化以空格分割一行数据，取分割出来的第一个数据
                y = re.split(r' ', line)[1]
                z = re.split(r' ', line)[2]
                line = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + '\n' # 重新写行数据
                xyz_file = os.path.join(output_dir, filename)
                with open(xyz_file, 'a') as mon:
                    mon.write(line)
            f2.close()