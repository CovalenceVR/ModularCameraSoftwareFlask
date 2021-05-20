import json

def make():
    data = {}
    data['config'] = []
    data['config'].append({
        'exposure': 'sports',
        'awb': 'incandescent',
        'intra': '1',
        'name': 'Cam1'
    })

    with open('Config.txt', 'w') as outfile:
        json.dump(data, outfile)

def read():
    with open('Config.txt') as json_file:
        data = json.load(json_file)
        for item in data['config']:
            print(item['exposure'])
