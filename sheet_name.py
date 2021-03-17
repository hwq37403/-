import pandas as pd


def sheet_name():
    '''
    返回排序列表表名的list列表
    :return:
    '''
    read_path = 'D:\\财务数据\\结果居民\\表名.xlsx'

    df = pd.read_excel(read_path, sheet_name='Sheet1')

    num = df.iloc[:, 0]

    print(num)
    s_list = []

    for i in num:
        s_list.append(i)
    print(s_list)
    return s_list