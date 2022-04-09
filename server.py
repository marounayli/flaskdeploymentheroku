from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

data = {}

@app.route('/')
def index():
    return 'hello world'
    

@app.route('/data/<key>' , methods = ['POST'])
def addToData(key):
    print(request.json)
    data[key] = request.json
    return ""


@app.route('/data', methods = ['GET'])
def getData():
    return jsonify(data)

app.run(host='0.0.0.0', port=5000)