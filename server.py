from flask import Flask, jsonify
from flask import request
server = Flask(__name__)

data = {}

@server.route('/')
def index():
    return 'hello world'
    

@server.route('/data/<key>' , methods = ['POST'])
def addToData(key):
    print(request.json)
    data[key] = request.json
    return ""


@server.route('/data', methods = ['GET'])
def getData():
    return jsonify(data)

server.run(host='0.0.0.0', port=5000)