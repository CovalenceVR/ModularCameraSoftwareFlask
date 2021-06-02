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

    with open('Config.json', 'w') as outfile:
        json.dump(data, outfile)
        
def updateCamName(camname):
    a_file = open("Config.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    
    json_object["name"] = camname
    a_file = open("Config.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
    
def read():
    with open('Config.json') as json_file:
        data = json.load(json_file)
        for item in data['config']:
            print(item['exposure'])
