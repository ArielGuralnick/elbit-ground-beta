from flask import render_template
import pandas as pd


async def maintenance_technician_mafil_Handler(request):
    if request.method == 'GET':
        data = pd.read_csv('elbit-ground-beta/maintenance/app/db/maintenance.csv')
        dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
        r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
        '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
        '\n' + '</a>' + '\n' + '<h1>פערי מאמן</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
        '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
        '\n' + '<form action="" method="post">' + '\n')
        dphtml += data.to_html(classes = "table table-hover", border=0)
        with open('elbit-ground-beta/app/templates/maintenance_technician_mafil.html','w', encoding='utf-8-sig') as f:
#            f.writelines([dphtml + '\n' + r'<br>' + '\n' + 
            r'''
            
        
        return render_template('maintenance_technician_mafil.html')
 '''

    elif request.method == 'POST': # אנחנו צריכים תאריך, מלל חופשי לפער שיש, מצב בחירה מטופל / לא טופל
        date_upload = request.form.get('date_upload')
        time_error = request.form.get('time_error')
        name_identifier = request.form.get('name_identifier')
        '''

        field_content = ['תאריך', 'שעה', 'שם מזהה', 'עיתוי התקלה', 'עמדה', 'סוג התקלה', 'הסבר','תפעול התקלה', 'מחשב', 'טופל/לא טופל', 'זמן השבתה']
        data_errors = pd.DataFrame([{'תאריך' : date_error, 'שעה' : time_error, 'שם מזהה':name_identifier,
        'עיתוי התקלה': timing_fault, 'עמדה' : position, 'סוג התקלה' : type_of_fault,'הסבר' : explanation,
        'תפעול התקלה' : fault_operation,'מחשב' : computer, 'טופל/לא טופל' : situation, 'זמן השבתה' : downtime}], columns=field_content)
        with open('elbit-ground-beta/app/db/data_errors.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_errors.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'התקלה נקלטה בהצלחה!', category="success")
        return redirect(url_for('skyLark_instructor'))
        '''
