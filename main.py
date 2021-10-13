import csv
from flask import Flask,render_template,request, redirect, flash,url_for

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route("/skyLark", methods=['GET','POST'])
def skyLark():
    if request.method == 'GET':
        return render_template('skyLark.html', title_simulator = "מאמן רוכב שמיים")

header = ['תאריך', 'שעה', 'שם מזהה']
@app.route("/error", methods=['GET','POST'])
def error():
    if request.method == 'GET':
        return render_template('error.html')

    elif request.method == 'POST':
        date = request.form.get('date')
        time = request.form.get('time')
        name_identifier = request.form.get('name_identifier')
        timing_fault = request.form.get('timing_fault')
        position = request.form.get('position')
        type_of_fault = request.form.get('type_of_fault')
        explanation = request.form.get('explanation')
        fault_operation = request.form.get('fault_operation')
        computer = request.form.get('computer')
        situation = request.form.get('situation')
        downtime = request.form.get('downtime')

        field_content = ['date', 'time', 'name_identifier',
         'timing_fault', 'position', 'type_of_fault', 'explanation',
         'fault_operation', 'computer', 'situation', 'downtime']
        with open('dataa.csv', 'a', encoding='UTF8',newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_content)
            writer.writerow({'date' : date, 'time' : time, 'name_identifier':name_identifier,
             'timing_fault': timing_fault, 'position' : position, 'type_of_fault' : type_of_fault,
             'explanation' : explanation, 'fault_operation' : fault_operation,
             'computer' : computer, 'situation' : situation, 'downtime' : downtime})
#        flash('התקלה נקלטה בהצלחה!', category="success")
        return redirect(url_for('skyLark'))

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
