from app import app # importing app variable from app package
import pandas as pd
from flask import render_template,request, redirect, flash,url_for, send_file

    
@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route("/user", methods=['GET'])
def user():
    if request.method == 'GET':
        return render_template('user.html', title_simulator = "מאמן רוכב שמיים", second_paragraph = "אֵין כָּאֵל יְשֻׁרוּן רֹכֵב שָׁמַיִם בְּעֶזְרֶךָ וּבְגַאֲוָתוֹ שְׁחָקִים")

@app.route("/skyLark_instructor", methods=['GET','POST'])
def skyLark_instructor():
    if request.method == 'GET':
        return render_template('skyLark_instructor.html', title_simulator = "מאמן רוכב שמיים")

@app.route("/skyLark_technician", methods=['GET','POST'])
def skyLark_technician():
    if request.method == 'GET':
        return render_template('skyLark_technician.html')

@app.route("/skyLark_mafil", methods=['GET','POST'])
def skyLark_mafil():
    if request.method == 'GET':
        return render_template('skyLark_mafil.html')

@app.route("/literature", methods=['GET'])
def literature():
    if request.method == 'GET':
        return render_template('literature.html')

@app.route("/order_training", methods=['GET'])
def order_training():
    if request.method == 'GET':
        return render_template('order_training.html')

@app.route('/user/skyLark_mafil/show-static-pdf-safrot_mafil')
def show_static_pdf_safrot_mafil():
    if request.method == 'GET':
        static_file =  open('elbit-ground-beta/app/safrot_mafil.pdf', 'rb')
        return send_file(static_file, attachment_filename='safrot_mafil.pdf')

@app.route('/user/skyLark_mafil/show-static-pdf-safrot_simulator')
def show_static_pdf_safrot_simulator():
    if request.method == 'GET':
        static_file =  open('elbit-ground-beta/app/safrot_simulator.pdf', 'rb')
        return send_file(static_file, attachment_filename='safrot_simulator.pdf')

@app.route('/user/skyLark_instructor/show-static-pdf-solutions')
def show_static_pdf_solutions():
    if request.method == 'GET':
        static_file =  open('elbit-ground-beta/app/solutions.pdf', 'rb')
        return send_file(static_file, attachment_filename='solutions.pdf')

@app.route('/show_data_errors', methods=['GET','POST'])
def show_data_errors():
    if request.method == 'GET':       
        important_columns = ['עמדה', 'סוג התקלה', 'הסבר', 'זמן השבתה']
        data_errors = pd.read_csv('elbit-ground-beta/app/data_errors.csv')
        dphtml = r'<meta charset="utf-8-sig">' + '\n' + r'<link rel="stylesheet" href="static/style.css">' + '\n' + r'<link rel="stylesheet" href="static/css/bootstrap.css">' + '\n'
        dphtml += data_errors.to_html(border=0)
        with open('elbit-ground-beta/app/templates/show_data_errors.html','w', encoding='utf-8-sig') as f:
            f.write(dphtml)
            f.close()
        return render_template('show_data_errors.html')
    
#        data_errors = pd.read_csv('elbit-ground-beta/data_errors.csv', encoding="ISO-8859-8")
#        data_errors.to_html("elbit-ground-beta/templates/show_data_errors.html", classes="table table-hover", na_rep='NaN', border="0")
#        return render_template('show_data_errors.html')

@app.route("/feedback", methods=['GET','POST'])
def feedback():
    if request.method == 'GET':
        return render_template('feedback.html', title_simulator = "מאמן רוכב שמיים")
    elif request.method == 'POST':
        question_1 = request.form.get('question_1')
        question_2 = request.form.get('question_2')
        question_3 = request.form.get('question_3')
        question_4 = request.form.get('question_4')
        question_5 = request.form.get('question_5')
        print(question_1, question_2,question_3,question_4,question_5)
        field_content = ['אנא דרג את איכות האימון','לפי דעתך עד כמה המאמן מתאר את המציאות','עד כמה אתה מרגיש בנוח בתפעול המאמן','עד כמה אתה מת עכשיו להיות בתאילנד','עד כמה אתה מת לאכול עכשיו פיצה']
        feedback_information = pd.DataFrame([{'אנא דרג את איכות האימון' : question_1, 'לפי דעתך עד כמה המאמן מתאר את המציאות' : question_2, 'עד כמה אתה מרגיש בנוח בתפעול המאמן' : question_3, 'עד כמה אתה מת עכשיו להיות בתאילנד' : question_4, 'עד כמה אתה מת לאכול עכשיו פיצה' : question_5}], columns=field_content)
        with open('elbit-ground-beta/app/feedback.csv', 'a', newline='') as file:
            feedback_information.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'המשוב נקלט בהצלחה! תודה!', category="success")
        return redirect(url_for('skyLark_instructor'))

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
        data_activity = pd.DataFrame([{'סוג מאמן': position_upload, 'מספר אימון' : number_training, 'תאריך העלאה' : date_upload,
        'פעילות עבור' : group_training, 'שם המעלה' : name_updater,'שעת התחלה' : time_upload,
        'שם המורידה' : name_downloader, 'שעת סיום' : time_download}], columns=field_content)
        with open('elbit-ground-beta/app/data_activity.csv', 'a', newline='') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'תיעוד האימון נקלט בהצלחה!', category="success")
        return redirect(url_for('skyLark_instructor'))



@app.route("/insert_error", methods=['GET','POST'])
def insert_error():
    if request.method == 'GET':
        return render_template('insert_error.html')

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
        data_errors = pd.DataFrame([{'תאריך' : date_error, 'שעה' : time_error, 'שם מזהה':name_identifier,
        'עיתוי התקלה': timing_fault, 'עמדה' : position, 'סוג התקלה' : type_of_fault,'הסבר' : explanation,
        'תפעול התקלה' : fault_operation,'מחשב' : computer, 'טופל/לא טופל' : situation, 'זמן השבתה' : downtime}], columns=field_content)
        with open('elbit-ground-beta/app/data_errors.csv', 'a', newline='') as file:
            data_errors.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'התקלה נקלטה בהצלחה!', category="success")
        return redirect(url_for('skyLark_instructor'))


@app.route("/warehouse_inventory", methods=['GET','POST'])
def warehouse_inventory():
    if request.method == 'GET':
        return render_template('warehouse_inventory.html')

#    if request.method == 'POST':
#        item_type = request.form.get('th1_1')
#        item_type = request.form.get('th1_2')
#        item_type = request.form.get('th1_3')
#        item_type = request.form.get('th1_4')
#        item_type = request.form.get('th1_5')
#        item_type = request.form.get('th2_1')
#        item_type = request.form.get('th2_2')
#        item_type = request.form.get('th2_3')
#        item_type = request.form.get('th2_4')
#        item_type = request.form.get('th2_5')
#        item_type = request.form.get('th3_1')
#        item_type = request.form.get('th3_2')
#        item_type = request.form.get('th3_3')
#        item_type = request.form.get('th3_4')
#        item_type = request.form.get('th3_5')




@app.route("/mars", methods=['GET','POST'])
def mars():
    if request.method == 'GET':
        return render_template('user.html', title_simulator = "מאמן מרס", second_paragraph = "מרס מרס מרס מרס מרס מרס")

@app.route("/moreshet", methods=['GET','POST'])
def moreshet():
    if request.method == 'GET':
        return render_template('user.html', title_simulator = "מאמן מורשת", second_paragraph = "מורשת מורשת מורשת מורשת מורשת")