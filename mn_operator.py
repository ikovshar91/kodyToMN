import pandas as pd
import os
import warnings
from tabulate import tabulate


homedir = os.path.expanduser('~')

kody = pd.read_excel(homedir + '\\Desktop\\Операторы_МН\\kody.xlsx', index_col=False)

kody2 = kody.copy()

data = {'Номер': [], 'Код': [], 'Оператор': []}
dataframe = pd.DataFrame(data)


def fxn():
    warnings.warn("deprecated", DeprecationWarning)

while True:
    try:
        if not dataframe.empty:
            print('Если хотите записать в файл, введите W')
            print(f"{tabulate(dataframe,headers='keys',tablefmt='psql',showindex=False)} \n \n")

        number = input('Введите номер или "w" для записи файла \n')

        if str(number) == 'w':
            dataframe.to_excel(homedir + '\\Desktop\\Операторы_МН\\numbers.xlsx',sheet_name='itog', index=False)
            input('Файл записан, для завершения программы нажмите Enter ..... \n')
            break

        kod = int(number)
        for i in range(1, len(str(kod))):
            mem = kody2.query('DialCodes == @kod')
            if mem['DialCodes'].empty:
                kod = kod // 10
                if len(str(kod)) == 1:
                    print('Номер не найден, попробуйте ещё раз')
            else:
                td = {'Номер': str(number), 'Код': str(kod), 'Оператор': mem["Destination"].to_string(index=False)}
                warnings.simplefilter("ignore")
                dataframe = dataframe.append(td, ignore_index=True)
                break
    except:
        print('\nВведите номер корректно \n \n')

