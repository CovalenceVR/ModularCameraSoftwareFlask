import os
import json

def record(fileName):
    with open('vidConfig.json') as json_file:
        item = json.load(json_file)
        configParam = "";
        for param in item:
            if param != "name":
                configParam += " --" + param + " " + item[param]
        os.system("raspivid -o projects/" + item['name'] + "_" + fileName + ".h264 -n -t 0" + configParam)

def recordPrint(fileName):
    with open('Config.json') as json_file:
        item = json.load(json_file)
        configParam = "";
        for param in item:
            if param != "name":
                configParam += " --" + param + " " + item[param]
        print("raspivid -o projects/" + item['name'] + "_" + fileName + ".h264 -n -t 0" + configParam)

def ledOff():
    with open("/sys/class/leds/led0/brightness","w") as f:
        f.write('0\n')
     
def ledOn():
    with open("/sys/class/leds/led0/brightness","w") as f:
        f.write('1\n')
        
def stop():
    os.system("pkill raspivid")
            
def delete(fileName):
    os.remove("projects/" + fileName)

def deleteall():
    for f in os.listdir("projects"):
        os.remove(os.path.join("projects", f))

def downloadall(fileName):
    os.system("zip -r " + fileName + ".zip projects")
    os.system("mv " + fileName + ".zip projects")

def still(fileName):
"""
raspistill -o projects/name_filename.png --exposure sports --nopreview --timeout 10
"""
    with open('stillConfig.json') as json_file:
        item = json.load(json_file)
        configParam = "";
        for param in item:
            if param != "name":
                configParam += " --" + param + " " + item[param]
        os.system("raspistill -o projects/" + item['name'] + "_" + fileName + ".png" + configParam)
        
def audio(fileName):
    with open('audioConfig.json') as json_file:
        item = json.load(json_file)
        configParam = "";
        for param in item:
            if param != "name":
                configParam += " -" + param + " " + item[param]
        os.system("arecord -v " + item['name'] + "_" + fileName + ".wav" + configParam)
        
def update():
    os.system("git reset --hard; git pull; pip install -r requirements.txt; pkill python3; python3 app.py")
    
def terminal(command):
    print(command)
    os.system(command)
