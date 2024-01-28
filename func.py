import json
from datetime import datetime

def open_file():
    dates = []
    with open('operations.json', encoding='utf-8') as f:
        data = json.load(f)
        for oper in data:
            if oper: #проверяем есть ли пустой словарь
                date_string = oper['date']

                # преобразовываем строку в формат год, часы, минуты, секунды, миллисекунды
                date_time = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')

                #форматируем в строку
                formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S %f')[:-3]
                dates.append((formatted_date_time, oper))

        sorted_list = sorted(dates, key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S %f'), reverse=True)
        return [item[1] for item in sorted_list]

