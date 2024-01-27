from datetime import datetime
from func import open_file

def last_5_executes():
    '''
    Последние 5 успешных операции
    :return:
    '''
    last_five_operations = []
    executed_oper = open_file()
    for oper in executed_oper:
        if oper['state'] == 'EXECUTED':
            last_five_operations.append(oper)
    return last_five_operations[:5]


def hide_numbers():
    '''
    скрываем номер счета 'from' 'to'
    :return:
    '''
    hidden_oper = []
    last_five_operations = last_5_executes()
    for oper in last_five_operations:
        # звездочки для from
        if 'from' in oper:
            oper['from'] = oper['from'].replace(oper['from'][-9:-4], '******')

        # звездочки для to
        if 'to' in oper:
            oper['to'] = oper['to'].replace(oper['to'][-6:-4], '****')[-6:]

        hidden_oper.append(oper)

    return hidden_oper

def get_dates():
    '''
    отделяем дату от времени
    :return:
    '''
    date_list = []
    hiden_num = hide_numbers()
    for oper in hiden_num:
        if oper['date']:
            date_time = datetime.strptime(oper['date'], '%Y-%m-%dT%H:%M:%S.%f')
            formatted_date_time = date_time.strftime('%Y-%m-%d %H')[:-3]
            oper['date'] = formatted_date_time
            date_list.append(oper)
    return date_list


