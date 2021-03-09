from flask import render_template, url_for, flash, redirect, request
from app import app
from stockDL import main
from app.forms import TickerForm

@app.route('/')
@app.route('/home')
def home():
    return "<h>Welcome to pyBhushan<h>"

@app.route('/predict', methods=['GET'])
def readTicker():
    ticker = TickerForm()
    return render_template('predict.html')

