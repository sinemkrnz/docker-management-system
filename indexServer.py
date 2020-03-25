from flask import Flask
from flask import request, jsonify
import requests
import json
import os
import subprocess


app = Flask(__name__)
@app.route('/pullImage', methods=['GET'])
def pullImage():
    imageName = request.args.get('imageName')
    resultList = os.popen('docker image pull '+str(imageName)).readlines()
    return jsonify(resultList)


@app.route('/runImage', methods=['GET'])
def runImage():
    imageName = request.args.get('imageName')
    resultList = os.popen(
        'docker run -d --rm -ti --name test -p 5000:5000 '+str(imageName)).readlines()
    return jsonify(resultList)


@app.route('/getImageID', methods=['GET'])
def getImageID():
    imageName = request.args.get('imageName')
    resultList = os.popen('docker images '+str(imageName)).readlines()
    result = resultList[1].split(' ')
    data = []
    for i in result:
        if (i != ""):
            data.append(i)
    return jsonify(data[2])


@app.route('/statusByName', methods=['GET'])
def getContainerID():
    imageName = request.args.get('imageName')
    resultList = os.popen('docker ps --filter ancestor=' +
                          str(imageName)).readlines()
    return jsonify(resultList)


@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    imageID = request.args.get('imageID')
    resultList = os.popen('docker rmi -f '+str(imageID)).readlines()
    return jsonify(resultList)


@app.route('/deleteContainer', methods=['GET'])
def deleteRunningContainers():
    containerID = request.args.get('containerID')
    resultList = os.popen('docker rm -f '+str(containerID)).readlines()
    return jsonify(resultList)


@app.route('/login', methods=['GET'])
def login():
    resultList = os.popen('docker login -u 1864 -p Everest.1997').readlines()
    return jsonify(resultList)


@app.route('/listRunning', methods=['GET'])
def listRunningContainers():
    resultList = os.popen('docker ps -a').readlines()
    return jsonify(resultList)


@app.route('/listContainers', methods=['GET'])
def listContainers():
    resultList = os.popen('docker image ls').readlines()
    return jsonify(resultList)


app.run(host='0.0.0.0', port=5003, debug=True)