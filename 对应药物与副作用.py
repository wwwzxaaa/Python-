import pandas as pd
from pandas import DataFrame
df= pd.read_csv(r"E:\work\text\meddra2.csv",header=0)
# df = df.groupby(by='DrugID').apply(lambda x :[','.join(x['GOID_seffect'])])
# # print(data,"E:\work\\text\end_meddra.csv")
# df.to_csv(r"E:\work\text\end_meddra.csv",index=False)
df['GOID_seffect'] = df['GOID_seffect'].apply(lambda x:','+ x)

drug_data = df.groupby(by='DrugID').sum()
length=len(drug_data['GOID_seffect'])
for i in range(0,length-1):
    drug_data['GOID_seffect'][i]=set(drug_data['GOID_seffect'][i].split(','))
    # print(len(drug_data['GOID_seffect'][i]))
    lens=len(drug_data['GOID_seffect'][i])-1
    # if lens >= 10:
    #     df = df[df['']
    #     drug_data['GOID_seffect'] = drug_data['GOID_seffect'][i]
    #     print(drug_data['GOID_seffect'])
    #     drug_data['GOID_seffect'] = drug_data['GOID_seffect'][i].apply(lambda x: [x[1:]])
    #     print(drug_data['GOID_seffect'])
    #     drug_data.head()
    #     drug_data.to_csv('E:\work\\text\end_meddra.csv')