from flask import render_template, flash, redirect, url_for
import pandas as pd
import time
from myboto3 import upload_files
import os, sys

async def edit_maintenance_technician_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('app/db/skyLark/maintenance.csv')
      disparity = data["מה הפער"]

      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1 style="padding-left: 19%;">עריכת פער</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')       
      with open('app/templates/skyLark/edit/edit_maintenance_mafil.html','w', encoding='utf-8-sig') as f:
        f.writelines([dphtml + '\n' + r'''
<div class="col form-group second-paragraph">
<label>שים לב ! </label>
<br>
<label>למחיקת שורה יש לבחור רק מספר תקלה!</label>
<br>
<label>בעריכת שורה יש להכניס את כל הערכים מחדש</label>
</div>
<br>
<div class="container">
<div class="row">
<div class="col form-group">
<label for="">בחר פער לעריכה</label>
<select class="form-control" name="disparity">
  {% for i in data %}
    <option>{{ i }}</option>
  {% endfor %}
</select>
</div>
<div class="col form-group">
  <label for="">טופל \ לא טופל</label>
  <select class="form-control" name="status">
    <option>V</option>
    <option>X</option>
  </select>
</div>
</div>
<div class="row">
<div class="col form-group">
  <label for="" class="labelSettings">תאריך טיפול</label>
  <input type="date" name="date_treatment" class="form-control" min="2021-01-01">
  <br>
</div>
</div>
</div>

<script>
    function fireDeletAlert() {
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: '!הפער נמחק בהצלחה',
            showConfirmButton: false,
            timer: 1500
        })
    }      
</script>
<script>
    function fireSweetAlert() {
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: '!הפער עודכן בהצלחה',
            showConfirmButton: false,
            timer: 1500
        })
    }      
</script>
<div class="container">
<div class="col form-group" style="text-align: center;">
  <form method="POST">
    <button type="sumbit" name="options" value="option_edit" class="btn btn-outline-success" onclick="fireSweetAlert()">עדכן</button>
    <button type="sumbit" name="options" value="option_delet" class="btn btn-outline-danger" onclick="fireDeletAlert()">מחיקה</button>
  </form>
</div>
</div>'''+ '\n' + r"</div>" + '\n' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
        f.close()
      return render_template('skyLark/edit/edit_maintenance_mafil.html', data = disparity)
  
    elif request.method == 'POST':
      time.sleep(1.5)
      if request.form.get('options') == 'option_edit':
        disparity = request.form.get('disparity')
        status = request.form.get('status')
        date_treatment = request.form.get('date_treatment')

        data = pd.read_csv('app/db/skyLark/maintenance.csv')
        row_to_edit = data.index[data['מה הפער'] == disparity]
        data.loc[row_to_edit, ['טופל / לא טופל','תאריך טיפול']] = [status, date_treatment]
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/skyLark/maintenance.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!הפער עודכן בהצלחה', category="success")
        
        src_upload_file_path = "app/db/skyLark/maintenance.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('show_maintenance_technician_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        disparity = request.form.get('disparity')
        data = pd.read_csv('app/db/skyLark/maintenance.csv')
        row_to_delet = data.index[data['מה הפער'] == disparity]
        data.drop(row_to_delet, inplace=True, axis=0)
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/skyLark/maintenance.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'הפער נמחק בהצלחה!', category="success")
        
        src_upload_file_path = "app/db/skyLark/maintenance.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('show_maintenance_technician_mafil'))
        
