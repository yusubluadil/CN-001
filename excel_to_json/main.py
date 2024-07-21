import json
import random
import pandas as pd

from string import printable


DATAS = pd.read_excel('datas.xls')
col_names = [
    'First Name', 'Last Name', 'Gender', 'Country', 'Age', 'Date', 'Id'
]


counter = 1
while True:
    op = input("Transfer olunacaq sutun basliqlarini (ve ya basligini) daxil edin: ")
    col_list = op.split(',') # ['First Name', 'Age']

    flag = False
    for i in col_list:
        if i not in col_names:
            print('Daxil etdiyiniz sutun adi movcud deyil')
            flag = True
    
    if flag:
        continue

    list_datas = []
    for i in DATAS.to_dict('records'):
        print(i)
        new_data = {}
        for j in col_list:
            new_data[j] = i.get(j)
        list_datas.append(new_data)

    random_symbol_list = random.choices(printable, k=8)
    random_symbols = ''.join(random_symbol_list)

    filename = f'datas_{random_symbols}_{counter}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(list_datas, f, indent=4, ensure_ascii=False)

    counter += 1
