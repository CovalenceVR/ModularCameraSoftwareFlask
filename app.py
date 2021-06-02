from importlib import import_module
import os
import flask
from markupsafe import escape
import Pi
from multiprocessing import Process
import time
import UpdateJson

#import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_pi import Camera


app = flask.Flask(__name__)
DOWNLOAD_FOLDER = './projects'
BASE_DIR = './'

@app.route('/')
def index():
    return flask.render_template('cam.html')

@app.route('/cam/')
@app.route('/cam/<status>', methods=['GET','POST'])
def cam(status=None):
    return flask.render_template('cam.html', status=status, ip=flask.request.host)
    
@app.route('/led/off', methods=['GET','POST'])
def ledOff(status=None):
    Pi.ledOff()
    return flask.render_template('cam.html', status=status, ip=flask.request.host)
    
@app.route('/led/on', methods=['GET','POST'])
def ledOn(status=None):
    Pi.ledOn()
    return flask.render_template('cam.html', status=status, ip=flask.request.host)

@app.route('/record/<fileName>', methods=['GET','POST'])
def start(fileName=None):
    Pi.ledOn()
    Pi.record(fileName + "__" + str(time.time_ns()))
    return flask.render_template('cam.html', ip=flask.request.host, status='record')

@app.route('/still/<fileName>', methods=['GET','POST'])
def still(fileName=None):
    Pi.ledOn()
    Pi.still(fileName + "__" + str(time.time_ns()))
    Pi.ledOff()
    return flask.render_template('cam.html', ip=flask.request.host, status='still')

@app.route('/delete/<fileName>', methods=['GET','POST'])
def remove(fileName=None):
    Pi.delete(fileName)
    return flask.render_template('cam.html', ip=flask.request.host, status='list')

@app.route('/deleteall', methods=['GET','POST'])
def removeall():
    Pi.deleteall()
    return flask.render_template('cam.html', ip=flask.request.host, status='list')

@app.route('/stop', methods=['GET','POST'])
def stop():
    Pi.ledOff()
    Pi.stop()
    return flask.render_template('cam.html', ip=flask.request.host, status='stop')

@app.route('/update', methods=['GET','POST'])
def update():
    Pi.update()
    return redirect("http://" + flask.request.host + "/cam")

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return flask.send_from_directory(DOWNLOAD_FOLDER, filename=filename, as_attachment=True)

@app.route('/downloadall/<path:filename>', methods=['GET', 'POST'])
def downloadall(filename):
    Pi.downloadall(filename)
    return flask.send_from_directory(DOWNLOAD_FOLDER, filename=filename, as_attachment=True)

@app.route('/updateCamName/<path:camName>', methods=['GET','POST'])
def updateCamName(camName):
    UpdateJson.updateCamName(camName)
    return flask.render_template('cam.html', ip=flask.request.host, status='update')
    
def gen(camera):
    """video streaming generator function"""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'content-type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/<path:req_path>')
def dir_listing(req_path):
    # Show directory contents
    abs_path = os.path.join(BASE_DIR, req_path)
    files = os.listdir(abs_path)
    return flask.render_template('cam.html', files=files, ip=flask.request.host, status='list')

@app.route('/preview')
def video_feed():
    """video streaming route put this in the src attribute of an img tag"""
    return flask.Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000, debug=False)
