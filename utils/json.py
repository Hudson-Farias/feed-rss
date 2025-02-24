from json import dump


def json_creater(data, path = 'data.json'):
    with open(f'{path}', 'w+', encoding = 'UTF-8') as file:
        dump(data, file, indent = 4)
