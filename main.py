# coding=utf-8
from flask import Flask, jsonify, request
from flask_cors import CORS
import Pyro5.api

app = Flask(__name__)
CORS(app)

def getPlayer():
    nameserver = Pyro5.api.locate_ns("192.168.1.202")
    uri = nameserver.lookup("player-rmi")
    rmi = Pyro5.api.Proxy(uri)
    return rmi

@app.route('/play', methods=['POST'])
def play():
    print("play")
    name=request.get_data().decode()
    getPlayer().play(name)
    return "200"

@app.route('/next', methods=['GET'])
def next():
    getPlayer().next()
    return "200"

@app.route('/prev', methods=['GET'])
def prev():
    getPlayer().previous()
    return "200"

@app.route('/pause', methods=['GET'])
def pause():
    getPlayer().pause()
    return "200"

@app.route('/stop', methods=['GET'])
def stop():
    getPlayer().stop()
    return "200"

@app.route('/resume', methods=['GET'])
def resume():
    getPlayer().resume()
    return "200"


@app.route('/volUp', methods=['GET'])
def volUp():
    getPlayer().volUp()
    return "200"

@app.route('/volDown', methods=['GET'])
def volDown():
    getPlayer().volDown()
    return "200"

@app.route('/set/volume', methods=['POST'])
def setVol():
    v = int(request.get_data().decode())
    getPlayer().setVol(v)
    return "200"

