import pandas as pd
from flask import render_template, flash, redirect, url_for


async def driving_insert_error_Handler(request):
    if request.method == 'GET':
        return render_template('driving/insert/driving_insert_error.html')
    elif request.method == 'POST':
        type_of_simulator = request.form.get('type_of_simulator')
        type_of_cell = request.form.get('type_of_cell')
        date_error = request.form.get('date_error')
        time_error = request.form.get('time_error')
        name_identifier = request.form.get('name_identifier')
        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        computer = request.form.get('computer')
        hardware_or_system = request.form.get('hardware_or_system')
        timing_fault = request.form.get('timing_fault')
        time_download = request.form.get('time_download')
        situation = request.form.get('situation')


        field_content = ['מאמן','סוג תא','תאריך','שעה','שם מזהה','סוג התקלה','תפעול התקלה','באיזה מחשב','חומרה \ תוכנה','עיתוי התקלה','זמן השבתה','טופל \ לא טופל']
        data_activity = pd.DataFrame([{'מאמן': type_of_simulator, 'סוג תא' : type_of_cell, 'תאריך' : date_error,
        'שעה' : time_error, 'שם מזהה' : name_identifier,'סוג התקלה' : type_of_fault,
        'תפעול התקלה' : fault_operation, 'באיזה מחשב' : computer, 'חומרה \ תוכנה': hardware_or_system,
        'עיתוי התקלה': timing_fault, 'זמן השבתה': time_download, 'טופל \ לא טופל' : situation}], columns=field_content)
        with open('elbit-ground-beta/app/db/driving/data_errors.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'!התקלה נקלטה בהצלחה', category="success")
        return redirect(url_for('skyLark_instructor'))