import os
import json

def record(fileName):
    with open('Config.txt') as json_file:
        data = json.load(json_file)
        for item in data['config']:
            os.system("raspivid -o projects/" + fileName + ".h264 -t 0 --framerate 24 " + "--exposure " + item['exposure'])

def recordPrint(fileName):
    with open('Config.txt') as json_file:
        data = json.load(json_file)
        for item in data['config']:
            print("raspivid -o projects/" + fileName + ".h264 -t 0 --framerate 24 " + "--exposure " + item['exposure'])
                
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
    os.system("raspistill -n -o projects/" + fileName + ".png")

def update():
    os.system("git pull; pkill python3; python3 app.py")
