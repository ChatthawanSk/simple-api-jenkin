from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=['GET'])
def getcode():
    return jsonify(message="Hello, World!"), 200

@app.route('/plus/<int:a>/<int:b>', methods=['GET'])
def plus(a, b):
    return jsonify(result=a + b), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)