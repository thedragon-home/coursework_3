from message import *

def operations():
    operation = get_dates()
    result = []
    for item in operation:
        if not 'from' in item:
            result.append(f"{item['date']} {item['description']} {item['to']} {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")
        else:
            result.append(f"{item['date']} {item['description']} {item['from']} -> {item['to']} {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")

    return '\n'.join(result)

if __name__ == "__main__":
    # print("Script is run directly")
    print(operations())
