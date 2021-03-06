from flask import render_template, flash, redirect, url_for
import pandas as pd
import time
from myboto3 import upload_files
import os, sys

async def moreshet_edit_warehouse_inventory_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('app/db/moreshet/warehouse_inventory.csv')
      type_of_item = data["סוג הפריט"]
      
      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1 style="margin-left: 15%;">עריכת מחסן</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')       
      with open('app/templates/moreshet/edit/moreshet_edit_warehouse_inventory.html','w', encoding='utf-8-sig') as f:
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
<label for="">בחר פריט לעריכה</label>
<select class="form-control" name="type_of_item">
  {% for i in data %}
    <option>{{ i }}</option>
  {% endfor %}
</select>
</div>
<div class="col form-group">
    <label>כמות במלאי</label>
    <input type="number" class="form-control" name="quantity">
    <br>
</div>
</div>
<div class="row">
<div class="col form-group">
    <label >להשלים\לרכוש</label>
    <select class="form-control" name = "needs_to_complete">
        <option>לא</option>
        <option>כן</option>
    </select>
    <br>
</div>
<div class="col form-group">
    <label">הערות</label>
    <input type="text" name="remarks" class="form-control">
    <br>
</div>
</div>
</div>

<script>
    function fireDeletAlert() {
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: '!הפריט נמחק בהצלחה',
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
            title: '!הפריט עודכן בהצלחה',
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
      return render_template('moreshet/edit/moreshet_edit_warehouse_inventory.html', data = type_of_item)
  
    elif request.method == 'POST':
      time.sleep(1.5)
      if request.form.get('options') == 'option_edit':
        type_of_item = request.form.get('type_of_item')
        quantity = request.form.get('quantity')
        needs_to_complete = request.form.get('needs_to_complete')
        remarks = request.form.get('remarks')
        data = pd.read_csv('app/db/moreshet/warehouse_inventory.csv')
        row_to_edit = data.index[data['סוג הפריט'] == type_of_item]
        data.loc[row_to_edit, ['כמות במלאי','נדרש להשלים \ לרכוש','הערות']] = [quantity, needs_to_complete, remarks]
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/moreshet/warehouse_inventory.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!השורה עודכנה בהצלחה', category="success")
        
        src_upload_file_path = "app/db/moreshet/warehouse_inventory.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('moreshet_show_warehouse_inventory'))
      
      
      if request.form.get('options') == 'option_delet':
        type_of_item = request.form.get('type_of_item')
        data = pd.read_csv('app/db/moreshet/warehouse_inventory.csv')
        row_to_delet = data.index[data['סוג הפריט'] == type_of_item]
        data.drop(row_to_delet, inplace=True, axis=0)
        current_cd_path = os.getcwd()
        print("CD=", current_cd_path)
        sys.stdout.flush()
        with open('app/db/moreshet/warehouse_inventory.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!השורה נמחקה בהצלחה', category="success")
        
        src_upload_file_path = "app/db/moreshet/warehouse_inventory.csv"
        bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
        upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
        return redirect(url_for('moreshet_show_warehouse_inventory'))