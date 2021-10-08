import pandas as pd
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/skyLark", methods=['GET','POST'])
def skyLark():
    if request.method == 'GET':
        return render_template('skyLark.html', title_simulator = "רוכב שמיים")

@app.route("/skyLark/errorsInSkyLark", methods=['GET','POST'])
def errorsInSkyLark():
    if request.method == 'GET':
        return render_template('errorsInSkyLark.html')

print("itay")

if __name__ == "__main__":
    app.run(debug=True)
