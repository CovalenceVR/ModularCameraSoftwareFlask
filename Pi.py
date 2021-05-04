import picamera
import os
import time

def record(fileName):
    os.system("raspivid -o projects/" + fileName + "__" + time.time() + ".h264 -t 99999999999")
                
def stop():
    os.system("pkill raspivid")
            
def delete(fileName):
    os.remove("projects/" + fileName)

def update():
    os.system("git pull; pkill python3; python3 app.py")
