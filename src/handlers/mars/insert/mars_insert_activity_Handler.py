import pandas as pd
from flask import render_template, flash, redirect, url_for
from flask import render_template, flash, redirect, url_for
from myboto3 import upload_files
import os, sys


async def mars_insert_activity_Handler(request):
    if request.method == 'GET':
        return render_template('mars/insert/mars_insert_activity.html')
    elif request.method == 'POST':
        date_upload = request.form.get('date_upload')
        type_of_training = request.form.get('type_of_training')
        num_of_meholel = request.form.get('num_of_meholel')
        time_upload = request.form.get('time_upload')
        time_download = request.form.get('time_download')
        name_updater = request.form.get('name_updater')
        num_of_position = request.form.get('num_of_position')
        num_of_practicing = request.form.get('num_of_practicing')

        field_content = ['תאריך העלאה','סוג אימון','מספר מחולל','שעת התחלה','שעת סיום','שם המדריכה','מספר עמדות','מספר מתאמנים']
        data_activity = pd.DataFrame([{'תאריך העלאה': date_upload, 'סוג אימון' : type_of_training, 'מספר מחולל' : num_of_meholel,
        'שעת התחלה' : time_upload, 'שעת סיום' : time_download,'שם המדריכה' : name_updater,
        'מספר עמדות' : num_of_position, 'מספר מתאמנים' : num_of_practicing}], columns=field_content)
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/mars/data_activity.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'תיעוד האימון נקלט בהצלחה!', category="success")
        
        src_upload_file_path = "app/db/mars/data_activity.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('mars_instructor'))
