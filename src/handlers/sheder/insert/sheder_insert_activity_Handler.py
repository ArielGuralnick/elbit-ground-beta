import pandas as pd
from flask import render_template, flash, redirect, url_for
from myboto3 import upload_files
import os, sys

async def sheder_insert_activity_Handler(request):
    if request.method == 'GET':
        return render_template('sheder/insert/sheder_insert_activity.html')
    elif request.method == 'POST':
        type_of_simulator = request.form.get('type_of_simulator')
        date_upload = request.form.get('date_upload')
        group_training = request.form.get('group_training')
        name_updater = request.form.get('name_updater')
        time_upload = request.form.get('time_upload')
        time_download = request.form.get('time_download')
        

        field_content = ['מאמן','תאריך העלאה','פעילות עבור','שם המעלה','שעת העלאה','שעת הורדה']
        data_activity = pd.DataFrame([{'מאמן': type_of_simulator, 'תאריך העלאה' : date_upload,
        'פעילות עבור' : group_training, 'שם המעלה' : name_updater,'שעת העלאה' : time_upload,
        'שעת הורדה' : time_download}], columns=field_content)
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/sheder/data_activity.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'תיעוד האימון נקלט בהצלחה!', category="success")
        
        src_upload_file_path = "app/db/sheder/data_activity.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('sheder_instructor'))