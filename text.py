import pandas as pd
from tqdm import tqdm
tqdm.pandas(desc='pandas bar')

def data_analysis(df):
    li = []
    results = pd.DataFrame()
    df1=df.copy()
    for index,row in tqdm(df.iteritems()):
        for index1,row1 in df1.iteritems():
            re_dic = {}
            results[index] = row + row1
            sum1 = results[results[index]!=0].count()[index] # 分母
            # results.loc[results[index] == 1, index] = 0
            # results.loc[results[index] == 2, index] = 1
            sum2 = results[results[index]==2].count()[index] # 分子
            re_dic['cid1'] = index
            re_dic['cid2'] = index1
            re_dic['value'] = round(sum2/sum1,6)
            li.append(re_dic)
            tmp=index1
        # df1.drop([tmp],axis=1,inplace=True)
    data = pd.DataFrame(li)
    return data

def read_data(file_name):
    return pd.read_csv(file_name,header=None).T

def read_temp():
    return pd.read_csv('chemicall_temp.csv',skiprows=1)

def save_results(df,file_name):
    df.to_csv(file_name,index=0)

if __name__ == '__main__':
    file_name = 'end_chemical1.csv'
    df = read_data(file_name)
    save_results(df,'chemicall_temp.csv')
    df = read_temp()
    df = data_analysis(df)
    save_results(df,'chemical_result.csv')