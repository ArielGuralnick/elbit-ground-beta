import pandas as pd
from flask import render_template, flash, redirect, url_for


async def tzevet_insert_error_Handler(request):
    if request.method == 'GET':
        return render_template('tzevet/insert/tzevet_insert_error.html')
    elif request.method == 'POST':
        type_of_simulator = request.form.get('type_of_simulator')
        type_of_tank = request.form.get('type_of_tank')
        date_error = request.form.get('date_error')
        time_error = request.form.get('time_error')
        name_identifier = request.form.get('name_identifier')
        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        computer = request.form.get('computer')
        tank_or_simulator = request.form.get('tank_or_simulator')
        timing_fault = request.form.get('timing_fault')
        time_download = request.form.get('time_download')
        situation = request.form.get('situation')
        name_treat = request.form.get('name_treat')
        time_treatment = request.form.get('time_treatment')


        field_content = ['מאמן','סוג טנק','תאריך','שעה','שם מזהה','סוג התקלה','תפעול התקלה','באיזה מחשב','טנק / מאמן','עיתוי התקלה','זמן השבתה','טופל \ לא טופל','שם המטפל','שעת טיפול']
        data_activity = pd.DataFrame([{'מאמן': type_of_simulator, 'סוג טנק' : type_of_tank, 'תאריך' : date_error,
        'שעה' : time_error, 'שם מזהה' : name_identifier,'סוג התקלה' : type_of_fault,
        'תפעול התקלה' : fault_operation, 'באיזה מחשב' : computer, 'טנק / מאמן': tank_or_simulator,
        'עיתוי התקלה': timing_fault, 'זמן השבתה': time_download, 'טופל \ לא טופל' : situation, 'שם המטפל': name_treat, 'שעת טיפול' : time_treatment}], columns=field_content)
        with open('app/db/tzevet/data_errors.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'!התקלה נקלטה בהצלחה', category="success")
        return redirect(url_for('tzevet_instructor'))