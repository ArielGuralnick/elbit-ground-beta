from flask import render_template, flash, url_for, redirect 
import pandas as pd

async def insert_maintenance_technician_mafil_Handler(request):
    if request.method == 'GET':
        return render_template('skyLark/insert/insert_maintenance_technician_mafil.html')
    elif request.method == 'POST':
        date_upload = request.form.get('date_upload')
        disparity = request.form.get('disparity')
        status = request.form.get('status')
        

        field_content = ['תאריך','מה הפער','טופל / לא טופל']
        data_errors = pd.DataFrame([{'תאריך' : date_upload, 'מה הפער' : disparity, 'טופל / לא טופל':status}], columns=field_content)
        with open('elbit-ground-beta/app/db/skyLark/maintenance.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_errors.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!תיעוד הפער בהצלחה', category="success")
        return redirect(url_for('show_maintenance_technician_mafil'))