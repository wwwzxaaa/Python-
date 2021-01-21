import pandas as pd
import os

data = pd.read_csv('chemical_result.csv', encoding='utf-8')
with open('chemical_result.txt', 'a+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0]) + '\t' + str(line[1])+ '\t' + str(line[2]) + '\n'))