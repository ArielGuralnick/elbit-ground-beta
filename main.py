import csv
import pandas as pd
from flask import Flask,render_template,request, redirect, flash,url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = '\xe0\\\x17\xb3\xca_\x82\x94\xf4\xa8w/;\x17&\xbbr\xf4;\xb6\x8f@\xcd\x7f'
# for safety - we go to terminal, import os, then - os.urandom(12).hex(), and copy the result and paste here.

@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route("/skyLark", methods=['GET','POST'])
def skyLark():
    if request.method == 'GET':
        return render_template('skyLark.html', title_simulator = "מאמן רוכב שמיים")

@app.route("/activity", methods=['GET','POST'])
def activity():
    if request.method == 'GET':
        return render_template('activity.html')
    
    elif request.method == 'POST':
        position_upload = request.form.get('position_upload')
        number_training = request.form.get('number_training')
        date_upload = request.form.get('date_upload')
        group_training = request.form.get('group_training')
        name_updater = request.form.get('name_updater')
        time_upload = request.form.get('time_upload')
        name_downloader = request.form.get('name_downloader')
        time_download = request.form.get('time_download')

        field_content = ['סוג מאמן', 'מספר אימון', 'תאריך העלאה', 'פעילות עבור','שם המעלה', 'שעת התחלה', 'שם המורידה', 'שעת סיום']
        with open('data_activity.csv', 'a', encoding='UTF8',newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_content)
#            writer.writeheader()
            writer.writerow({'סוג מאמן': position_upload, 'מספר אימון' : number_training, 'תאריך העלאה' : date_upload,
             'פעילות עבור' : group_training, 'שם המעלה' : name_updater,
             'שעת התחלה' : time_upload, 'שם המורידה' : name_downloader, 'שעת סיום' : time_download})
            flash(f'תיעוד האימון נקלט בהצלחה!', category="success")
        return redirect(url_for('skyLark'))


@app.route("/error", methods=['GET','POST'])
def error():
    if request.method == 'GET':
        return render_template('error.html')

    elif request.method == 'POST':
        date_error = request.form.get('date_error')
        time_error = request.form.get('time_error')
        name_identifier = request.form.get('name_identifier')
        timing_fault = request.form.get('timing_fault')
        position = request.form.get('position')
        type_of_fault = request.form.get('type_of_fault')
        explanation = request.form.get('explanation')
        fault_operation = request.form.get('fault_operation')
        computer = request.form.get('computer')
        situation = request.form.get('situation')
        downtime = request.form.get('downtime')

        field_content = ['תאריך', 'שעה', 'שם מזהה', 'עיתוי התקלה', 'עמדה', 'סוג התקלה', 'הסבר','תפעול התקלה', 'מחשב', 'טופל/לא טופל', 'זמן השבתה']
        with open('dataa.csv', 'a', encoding='UTF8',newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_content)
#            writer.writeheader()
            writer.writerow({'תאריך' : date_error, 'שעה' : time_error, 'שם מזהה':name_identifier, 'עיתוי התקלה': timing_fault, 'עמדה' : position, 'סוג התקלה' : type_of_fault,
             'הסבר' : explanation, 'תפעול התקלה' : fault_operation,
             'מחשב' : computer, 'טופל/לא טופל' : situation, 'זמן השבתה' : downtime})
            flash(f'התקלה נקלטה בהצלחה!', category="success")
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
