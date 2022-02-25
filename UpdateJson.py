import json

def make():
    data = {}
    data['config'] = []
    data['config'].append({
        'name': 'Cam0'
    })

    with open('vidConfig.json', 'w') as outfile:
        json.dump(data, outfile)
    with open('stillConfig.json', 'w') as outfile:
        json.dump(data, outfile)

def update(type,item,value):
    a_file = open(type + "Config.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    
    json_object[item] = value
    
    a_file = open(type + "Config.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
    
def remove(type,item):
    a_file = open(type + "Config.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    
    del json_object[item]
    
    a_file = open(type + "Config.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

def read(type):
    with open(type + 'Config.json') as json_file:
        data = json.load(json_file)
        print(data)
