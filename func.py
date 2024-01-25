import json
from datetime import datetime


with open('operations.json', encoding='utf-8') as f:
    data = json.load(f)
    for id, oper in enumerate(data):
        if not oper: #проверяем есть ли пустой словарь
            continue # если есть, пропускаем
        date_string = data[id]["date"]
        # преобразовываем строку в формат год, часы, минуты, секунды, миллисекунды
        date_time = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
        # print(date_time)
        #форматируем в строку
        formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S %f')[:-3]
        print(formatted_date_time)