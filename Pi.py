import os
import json

def record(fileName):
    with open('Config.json') as json_file:
        item = json.load(json_file)
        os.system("raspivid -o projects/" + item['name'] + "_" + fileName + ".h264 -n -t 0 --framerate 24" + " --exposure " + item['exposure'] + " --awb " + item['awb'] + " --intra " + item['intra'])

def recordPrint(fileName):
    with open('Config.json') as json_file:
        item = json.load(json_file)
        print("raspivid -o projects/" + item['name'] + "_" + fileName + ".h264 -n -t 0 --framerate 24" + " --exposure " + item['exposure'] + " --awb " + item['awb'] + " --intra " + item['intra'])

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
    with open('Config.json') as json_file:
        item = json.load(json_file)
        os.system("raspistill -n -o projects/" + item['name'] + "_" + fileName + ".png")

def update():
    os.system("git pull; pkill python3; python3 app.py")
