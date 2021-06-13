from flask import Flask, json, jsonify, request
# import stockDL as sdl
from model import main
import concurrent.futures

app = Flask(__name__)

def predictions(ticker):
        print("Making predictions")
        stockDL = main.Main(ticker)
        return stockDL.result

@app.route('/')
def hello_world():
    return "Welcome to pyBhushan"

@app.route('/predict/<string:ticker>', methods=['GET'])
def predict_returns(ticker):

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(predictions, ticker)
        return_value = future.result()
        return (return_value.to_json())
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)