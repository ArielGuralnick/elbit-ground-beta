from flask import render_template, flash,redirect,url_for
import pandas as pd

async def driving_order_training_Handler(request):
    counter_long_skylark = 0
    counter_long_mars = 0
    counter_long_moreshet = 0
    counter_long_raam = 0

    if request.method == 'GET':
        return render_template('driving/insert/driving_order_training.html')
    

    elif request.method=='POST':
        type_simulator = request.form.get('type_simulator')
        name_of_vehicle = request.form.get('name_of_Vehicle')
        num_of_cell = request.form.get('num_of_cell')
        date_start = request.form.get('date_start')
        time_start = request.form.get('time_start')
        date_end = request.form.get('date_end')
        time_end = request.form.get('time_end')

        field_content = ['מאמן','שם הכלי','מספר תאים','תאריך התחלה','שעת התחלה','תאריך סיום','שעת סיום']
        data = pd.DataFrame([{'מאמן': type_simulator,'שם הכלי' : name_of_vehicle,'מספר תאים' : num_of_cell, 'תאריך התחלה': date_start, 'שעת התחלה':time_start,
        'תאריך סיום':date_end ,'שעת סיום':time_end}], columns=field_content)
        with open('elbit-ground-beta/app/db/manager/driving_order_training.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!הבקשה נקלטה בהצלחה', category="success")
        return redirect(url_for('driving_order_training'))