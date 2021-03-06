from flask import render_template, flash, url_for, redirect 
import pandas as pd
from myboto3 import upload_files
import os, sys

async def insert_error_Handler(request):
    if request.method == 'GET':
        return render_template('skyLark/insert/insert_error.html')
    elif request.method == 'POST':
        date_error = request.form.get('date_error')
        time_error = request.form.get('time_error')
        name_identifier = request.form.get('name_identifier')
        timing_fault = request.form.get('timing_fault')
        position = request.form.get('position')
        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        computer = request.form.get('computer')
        situation = request.form.get('situation')
        downtime = request.form.get('downtime')
        
        field_content = ['תאריך', 'שעה', 'שם מזהה', 'עיתוי התקלה', 'עמדה', 'סוג התקלה', 'תפעול התקלה', 'מחשב', 'טופל/לא טופל', 'זמן השבתה']
        data_errors = pd.DataFrame([{'תאריך' : date_error, 'שעה' : time_error, 'שם מזהה':name_identifier,
        'עיתוי התקלה': timing_fault, 'עמדה' : position, 'סוג התקלה' : type_of_fault,
        'תפעול התקלה' : fault_operation,'מחשב' : computer, 'טופל/לא טופל' : situation, 'זמן השבתה' : downtime}], columns=field_content)
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/skyLark/data_errors.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_errors.to_csv(file, index=False, na_rep='null',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נשלחה בהצלחה', category="success")
        
        src_upload_file_path = "app/db/skyLark/data_errors.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('skyLark_instructor'))