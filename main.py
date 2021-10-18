import csv
import pandas as pd
from flask import Flask,render_template,request, redirect, flash,url_for, send_file

app = Flask(__name__)

# for safety - we go to terminal, import os, then - os.urandom(12).hex(), and copy the result and paste here.
app.config['SECRET_KEY'] = '\xe0\\\x17\xb3\xca_\x82\x94\xf4\xa8w/;\x17&\xbbr\xf4;\xb6\x8f@\xcd\x7f'

@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route("/skyLark", methods=['GET','POST'])
def skyLark():
    if request.method == 'GET':
        return render_template('skyLark.html', title_simulator = "מאמן רוכב שמיים")
    
@app.route("/literature", methods=['GET'])
def literature():
    if request.method == 'GET':
        return render_template('literature.html')

@app.route('/skyLark/literature/show/static-pdf/')
def show_static_pdf():
    static_file =  open('elbit-ground-beta/safrot_mafil.pdf', 'rb')
    return send_file(static_file, attachment_filename='safrot_mafil.pdf')

@app.route('/skyLark/show/dataa-csv/')
def show_dataa_csv():
    df = pd.read_csv('elbit-ground-beta/dataa.csv', usecols= ['עמדה','סוג התקלה','הסבר','זמן השבתה'], encoding="utf-8")
    print(df)
    static_file =  open('elbit-ground-beta/dataa.csv', 'rb')
    return send_file(static_file, attachment_filename='dataa.csv')

@app.route("/skyLark/solutions/", methods=['GET','POST'])
def solutions():
    excel_file = 'elbit-ground-beta/ariel.xlsx'
    df = pd.read_excel(excel_file)
    return df.to_html()

@app.route("/feedback", methods=['GET','POST'])
def feedback():
    if request.method == 'GET':
        return render_template('feedback.html', title_simulator = "מאמן רוכב שמיים")

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
#        cities = pd.DataFrame([{'סוג מאמן': position_upload, 'מספר אימון' : number_training, 'תאריך העלאה' : date_upload,'פעילות עבור' : group_training, 'שם המעלה' : name_updater,'שעת התחלה' : time_upload, 'שם המורידה' : name_downloader, 'שעת סיום' : time_download}], columns=field_content)
#        cities.to_csv('elbit-ground-beta/cities.csv', index=False, na_rep='N/A' encoding='utf-8')
#        df = pd.read_csv('elbit-ground-beta/cities.csv')

        with open('elbit-ground-beta/data_activity.csv', 'a', encoding='UTF-8',newline='') as file:
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
        cities = pd.DataFrame([{'תאריך' : date_error, 'שעה' : time_error, 'שם מזהה':name_identifier, 'עיתוי התקלה': timing_fault, 'עמדה' : position, 'סוג התקלה' : type_of_fault,
             'הסבר' : explanation, 'תפעול התקלה' : fault_operation,
             'מחשב' : computer, 'טופל/לא טופל' : situation, 'זמן השבתה' : downtime}], columns=field_content)
        cities.to_csv('elbit-ground-beta/cities.csv', index=False, na_rep='N/A', encoding='utf-8')
        df = pd.read_csv('elbit-ground-beta/cities.csv')
        
        with open('elbit-ground-beta/dataa.csv', 'a', encoding='utf-8-sig',newline='') as file:
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
