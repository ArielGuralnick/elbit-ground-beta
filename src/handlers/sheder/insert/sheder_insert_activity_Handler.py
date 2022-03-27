import pandas as pd
from flask import render_template, flash, redirect, url_for


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
        with open('elbit-ground-beta/app/db/sheder/data_activity.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'תיעוד האימון נקלט בהצלחה!', category="success")
        return redirect(url_for('sheder_instructor'))