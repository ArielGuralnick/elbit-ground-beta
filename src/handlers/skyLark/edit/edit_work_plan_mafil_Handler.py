from flask import render_template, flash, redirect, url_for
import pandas as pd
import time
from myboto3 import upload_files
import os, sys

async def edit_work_plan_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('app/db/skyLark/work_plan_mafil.csv')
      achievements = data["הישגים נדרשים"]
      
      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1 style="margin-left: 15%;">עריכת תוכנית שנתית</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')       
      with open('app/templates/skyLark/edit/edit_work_plan_mafil.html','w', encoding='utf-8-sig') as f:
        f.writelines([dphtml + '\n' + r'''
<div class="container">
<div class="row">
<div class="col-md-3 form-group">
<label for="">בחר הישג נדרש לעריכה</label>
<select class="form-control" name="achievements">
  {% for i in data %}
    <option>{{ i }}</option>
  {% endfor %}
</select>
</div>
<div class="col-md-3 form-group">
  <label for="">סטטוס ביצוע</label>
  <select class="form-control" name="status">
    <option>לא בוצע</option>
    <option>בהרצה</option>
    <option>בוצע</option>
  </select>
</div>
</div>
</div>

<script>
    function fireDeletAlert() {
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: '!היעד נמחק בהצלחה',
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
            title: '!היעד עודכן בהצלחה',
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
    <button type="sumbit" class="btn btn-outline-dark btn-phone" name="options" value="option_back">לדשבורד</button>
  </form>
</div>
</div>'''+ '\n' + r"</div>" + '\n' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
        f.close()
      return render_template('skyLark/edit/edit_work_plan_mafil.html', data = achievements)
  
    elif request.method == 'POST':
      time.sleep(1.5)
      if request.form.get('options') == 'option_edit':
        achievements = request.form.get('achievements')
        status = request.form.get('status')
        data = pd.read_csv('app/db/skyLark/work_plan_mafil.csv')
        row_to_edit = data.index[data['הישגים נדרשים'] == achievements]
        data.loc[row_to_edit, 'סטטוס ביצוע'] = status
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/skyLark/work_plan_mafil.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!היעד עודכן בהצלחה', category="success")
        
        src_upload_file_path = "app/db/skyLark/work_plan_mafil.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('show_work_plan_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        achievements = request.form.get('achievements')
        data = pd.read_csv('app/db/skyLark/work_plan_mafil.csv')
        row_to_delet = data.index[data['הישגים נדרשים'] == achievements]
        data.drop(row_to_delet, inplace=True, axis=0)
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/skyLark/work_plan_mafil.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!היעד נמחק בהצלחה', category="success")
        
        src_upload_file_path = "app/db/skyLark/work_plan_mafil.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('show_work_plan_mafil'))

      if request.form.get("options") == 'option_back':
        return redirect(url_for('skyLark_mafil'))
