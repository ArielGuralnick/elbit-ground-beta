import pandas as pd
from flask import render_template, flash, redirect, url_for
from myboto3 import upload_files
import os, sys

async def mars_insert_error_Handler(request):
    if request.method == 'GET':
        return render_template('mars/insert/mars_insert_error.html')
    elif request.method == 'POST':
        date_error = request.form.get('date_error')
        time_error = request.form.get('time_error')
        name_identifier = request.form.get('name_identifier')
        num_of_meholel = request.form.get('num_of_meholel')
        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        type_of_position = request.form.get('type_of_position')
        computer = request.form.get('computer')
        downtime = request.form.get('downtime')
        situation = request.form.get('situation')
        timing_fault = request.form.get('timing_fault')


        field_content = ['תאריך העלאה','שעת העלאה','שם המזהה','מספר מחולל','סוג התקלה','תפעול התקלה','סוג עמדה','באיזה מחשב','זמן השבתה','טופל \ לא טופל','עיתוי התקלה']
        data_activity = pd.DataFrame([{'תאריך העלאה': date_error, 'שעת העלאה' : time_error, 'שם המזהה' : name_identifier,
        'מספר מחולל' : num_of_meholel, 'סוג התקלה' : type_of_fault,'תפעול התקלה' : fault_operation,
        'סוג עמדה' : type_of_position, 'באיזה מחשב' : computer, 'זמן השבתה': downtime, 'טופל \ לא טופל': situation, 'עיתוי התקלה': timing_fault}], columns=field_content)
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/mars/data_errors.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'!התקלה נקלטה בהצלחה', category="success")
        
        src_upload_file_path = "app/db/mars/data_errors.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('mars_instructor'))