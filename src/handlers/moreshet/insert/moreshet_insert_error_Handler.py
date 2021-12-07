import pandas as pd
from flask import render_template, flash, redirect, url_for


async def moreshet_insert_error_Handler(request):
    if request.method == 'GET':
        return render_template('moreshet/insert/moreshet_insert_error.html')
    elif request.method == 'POST':
        date_error = request.form.get('date_error')
        time_error = request.form.get('time_error')
        name_identifier = request.form.get('name_identifier')
        num_of_cell = request.form.get('num_of_cell')
        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        type_of_position = request.form.get('type_of_position')
        computer = request.form.get('computer')
        downtime = request.form.get('downtime')
        situation = request.form.get('situation')
        timing_fault = request.form.get('timing_fault')


        field_content = ['תאריך העלאה','שעת העלאה','שם המזהה','מספר תא','סוג התקלה','תפעול התקלה','סוג עמדה','באיזה מחשב','זמן השבתה','טופל \ לא טופל','עיתוי התקלה']
        data_activity = pd.DataFrame([{'תאריך העלאה': date_error, 'שעת העלאה' : time_error, 'שם המזהה' : name_identifier,
        'מספר תא' : num_of_cell, 'סוג התקלה' : type_of_fault,'תפעול התקלה' : fault_operation,
        'סוג עמדה' : type_of_position, 'באיזה מחשב' : computer, 'זמן השבתה': downtime, 'טופל \ לא טופל': situation, 'עיתוי התקלה': timing_fault}], columns=field_content)
        with open('elbit-ground-beta/app/db/moreshet/data_errors.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'!התקלה נקלטה בהצלחה', category="success")
        return redirect(url_for('skyLark_instructor'))