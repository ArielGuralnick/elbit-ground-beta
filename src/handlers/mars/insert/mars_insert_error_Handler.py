import pandas as pd
from flask import render_template, flash, redirect, url_for


async def mars_insert_error_Handler(request):
    if request.method == 'GET':
        return render_template('mars/insert/mars_insert_error.html')
    elif request.method == 'POST':
        date_upload = request.form.get('date_upload')
        time_upload = request.form.get('time_upload')
        name_updater = request.form.get('name_updater')
        num_of_meholel = request.form.get('num_of_meholel')
        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        type_of_position = request.form.get('type_of_position')
        computer = request.form.get('computer')
        downtime = request.form.get('downtime')

        field_content = ['תאריך העלאה','שעת העלאה','שם המזהה','מספר מחולל','סוג התקלה','תפעול התקלה','סוג עמדה','באיזה מחשב','זמן השבתה']
        data_activity = pd.DataFrame([{'תאריך העלאה': date_upload, 'שעת העלאה' : time_upload, 'שם המזהה' : name_updater,
        'מספר מחולל' : num_of_meholel, 'סוג התקלה' : type_of_fault,'תפעול התקלה' : fault_operation,
        'סוג עמדה' : type_of_position, 'באיזה מחשב' : computer, 'זמן השבתה': downtime}], columns=field_content)
        with open('elbit-ground-beta/app/db/mars/mars_data_error.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'!התקלה נקלטה בהצלחה', category="success")
        return redirect(url_for('skyLark_instructor'))