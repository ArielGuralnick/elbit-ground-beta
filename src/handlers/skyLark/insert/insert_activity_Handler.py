import pandas as pd
from flask import render_template, flash, redirect, url_for
import psycopg2
from myboto3 import upload_files
import os, sys

async def insert_activity_Handler(request):
    if request.method == 'GET':
        return render_template('skyLark/insert/insert_activity.html')
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
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/skyLark/data_activity.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'התיעוד נשלח בהצלחה!', category="success")
        
        src_upload_file_path = "app/db/skyLark/data_activity.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('skyLark_instructor'))
