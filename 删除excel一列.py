import pandas as pd
import numpy as np
from pandas import DataFrame
df=pd.read_excel(r"E:\work\result_subcomp1.xlsx",header=None)
height,width = df.shape
df = df.T.drop_duplicates().T
df.to_excel("E:\work\\result_subcomp2.xlsx")