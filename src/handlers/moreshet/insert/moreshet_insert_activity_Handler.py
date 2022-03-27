import pandas as pd
from flask import render_template, flash, redirect, url_for


async def moreshet_insert_activity_Handler(request):
    if request.method == 'GET':
        return render_template('moreshet/insert/moreshet_insert_activity.html')
    elif request.method == 'POST':
        date_upload = request.form.get('date_upload')
        type_of_training = request.form.get('type_of_training')
        num_of_cell = request.form.get('num_of_cell')
        time_upload = request.form.get('time_upload')
        time_download = request.form.get('time_download')
        name_updater = request.form.get('name_updater')
        num_of_position = request.form.get('num_of_position')
        num_of_practicing = request.form.get('num_of_practicing')

        field_content = ['תאריך העלאה','סוג אימון','מספר תא','שעת התחלה','שעת סיום','שם המדריכה','מספר עמדות','מספר מתאמנים']
        data_activity = pd.DataFrame([{'תאריך העלאה': date_upload, 'סוג אימון' : type_of_training, 'מספר תא' : num_of_cell,
        'שעת התחלה' : time_upload, 'שעת סיום' : time_download,'שם המדריכה' : name_updater,
        'מספר עמדות' : num_of_position, 'מספר מתאמנים' : num_of_practicing}], columns=field_content)
        with open('elbit-ground-beta/app/db/moreshet/data_activity.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'תיעוד האימון נקלט בהצלחה!', category="success")
        return redirect(url_for('moreshet_instructor'))