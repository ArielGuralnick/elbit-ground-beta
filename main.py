import flask
import pandas as pd
from flask import Flask,render_template,request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/skyLark", methods=['GET','POST'])
def skyLark():
    if request.method == 'GET':
        return render_template('skyLark.html', title_simulator = "מאמן רוכב שמיים")

@app.route("/errors", methods=['GET','POST'])
def errors():
    if request.method == 'GET':
        return render_template('errors.html')

@app.route("/mars", methods=['GET','POST'])
def mars():
    if request.method == 'GET':
        return render_template('mars.html', title_simulator = "מאמן מרס")

@app.route("/moreshet", methods=['GET','POST'])
def moreshet():
    if request.method == 'GET':
        return render_template('moreshet.html', title_simulator = "מאמן מורשת")

if __name__ == "__main__":
    app.run(debug=True)
