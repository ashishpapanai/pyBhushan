from flask import Flask, json, jsonify, request
import stockDL as sdl
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/predict/<string:ticker>', methods=['GET'])
def predict_returns(ticker):
    def predictions():
        print("Making predictions")
        model = sdl.main.Main(ticker)
        return model.result
    
    thread = threading.Thread(target=predictions)
    thread.setDaemon(True)
    thread.start()
    print(thread)
    result = thread.join()
    print(result)
    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)