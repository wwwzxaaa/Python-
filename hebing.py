#将两个csv文件按列合并为一个csv
# import pandas as pd
# import os
# import numpy as np
# inputfile_txt_1="1.txt"
# inputfile_txt_2="2.txt"
# inputfile_txt_3="3.txt"
# inputfile_txt_4="4.txt"
# inputfile_txt_5="5.txt"
# outputfile="Fall0.csv"
# csv_1=pd.read_table(inputfile_txt_1)
# csv_2=pd.read_csv(inputfile_txt_2)
# csv_3=pd.read_csv(inputfile_txt_3)
# csv_4=pd.read_csv(inputfile_txt_4)
# csv_5=pd.read_csv(inputfile_txt_5)
# out_csv=pd.concat([csv_1,csv_2,csv_3,csv_4,csv_5],axis=1)
# out_csv.to_csv(outputfile,index=False)
import pandas as pd
import os
import numpy as np
inputfile_txt_1="E:\work\\tz_atc\\Fall9.txt"
inputfile_txt_5="E:\work\\tz_c_cid\\9.txt"
inputfile_txt_2="E:\work\\tz_chemicall\\Fall9.txt"
inputfile_txt_3="E:\work\\tz_protein\\Fall9.txt"
inputfile_txt_4="E:\work\\tz_simcomp\\Fall9.txt"
outputfile="Fall9.csv"
csv_1=pd.read_table(inputfile_txt_1)
csv_2=pd.read_table(inputfile_txt_2)
csv_3=pd.read_table(inputfile_txt_3)
csv_4=pd.read_table(inputfile_txt_4)
csv_5=pd.read_table(inputfile_txt_5)
out_csv=pd.concat([csv_1,csv_2,csv_3,csv_4,csv_5],axis=1)
out_csv.to_csv(outputfile,index=False)
