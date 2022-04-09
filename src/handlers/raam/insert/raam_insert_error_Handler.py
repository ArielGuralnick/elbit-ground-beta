from flask import render_template, flash, url_for, redirect 
import pandas as pd


async def raam_insert_error_Handler(request):
    if request.method == 'GET':
        return render_template('raam/insert/raam_insert_error.html')
    elif request.method == 'POST':
        start_date_error = request.form.get('start_date_error')
        num_of_poisition = request.form.get('num_of_poisition')
        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        computer = request.form.get('computer')
        end_date_error = request.form.get('end_date_error')
        situation = request.form.get('situation')
        
        field_content = ['תאריך זיהוי', 'מספר עמדה', 'סוג התקלה', 'תפעול', 'מחשב', 'תאריך טיפול', 'מצב']
        data_errors = pd.DataFrame([{'תאריך זיהוי' : start_date_error, 'מספר עמדה' : num_of_poisition,
        'סוג התקלה' : type_of_fault, 'תפעול' : fault_operation,'מחשב' : computer, 'תאריך טיפול' : end_date_error, 'מצב' : situation}], columns=field_content)
        with open('app/db/raam/data_errors.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_errors.to_csv(file, index=False, na_rep='null',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נשלחה בהצלחה', category="success")
        return redirect(url_for('raam'))