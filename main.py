# coding=utf-8
from flask import Flask, request
from flask_cors import CORS
import mpvAdapter as mpv
app = Flask(__name__)
CORS(app)


@app.route('/play', methods=['POST'])
def play():
    print("play")
    name=request.get_data().decode()
    mpv.play(name)
    return "200"

@app.route('/pause', methods=['GET'])
def pause():
    mpv.pause()
    return "200"

@app.route('/stop', methods=['GET'])
def stop():
    mpv.stop()
    return "200"

@app.route('/resume', methods=['GET'])
def resume():
    mpv.resume()
    return "200"

@app.route('/set/pos', methods=['POST'])
def seek():
    v = int(request.get_data().decode())
    mpv.seek(v)
    return "200"


@app.route('/get/info', methods=['GET'])
def getSongInfo():
    return mpv.getInfo()

'''
@app.route('/volUp', methods=['GET'])
def volUp():
    mpv.volUp()
    return "200"

@app.route('/volDown', methods=['GET'])
def volDown():
    mpv.volDown()
    return "200"

@app.route('/set/volume', methods=['POST'])
def setVol():
    v = int(request.get_data().decode())
    mpv.setVol(v)
    return "200"'''
