from flask import render_template, flash,redirect,url_for
import pandas as pd
from myboto3 import upload_files
import os, sys


async def order_training_Handler(request):
    if request.method == 'GET':
        return render_template('order_training.html')
    
    elif request.method=='POST':
        type_simulator = request.form.get('type_simulator')
        date_start = request.form.get('date_start')
        time_start = request.form.get('time_start')
        date_end = request.form.get('date_end')
        time_end = request.form.get('time_end')
       
        field_content = ['סוג מאמן', 'תאריך התחלה', 'שעת התחלה', 'תאריך סיום', 'שעת סיום']
        data = pd.DataFrame([{'סוג מאמן': type_simulator, 'תאריך התחלה': date_start, 'שעת התחלה':time_start,
        'תאריך סיום':date_end ,'שעת סיום':time_end}], columns=field_content)
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/manager/order_training.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!הבקשה נקלטה בהצלחה', category="success")
        
        src_upload_file_path = "app/db/manager/order_training.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('order_training'))

