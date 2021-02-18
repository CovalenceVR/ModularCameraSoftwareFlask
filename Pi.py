import picamera
import os

def record(fileName):
    os.system("raspivid -o projects/" + fileName + ".h264 -t 99999999999")
                
def stop():
    os.system("pkill raspivid")
            
def delete(fileName):
    os.remove("projects/" + fileName)

def update():
    os.system("pkill python3; git pull; python3 app.py")
