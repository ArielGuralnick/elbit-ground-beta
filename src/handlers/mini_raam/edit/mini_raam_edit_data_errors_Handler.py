from flask import render_template, flash, redirect, url_for
import pandas as pd
from pandas.core.indexes.base import Index
import time

async def mini_raam_edit_data_errors_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('app/db/mini_raam/data_errors.csv')
      index = data.index + 1    # adding 1 to index (start from 1, not 0)
      for i in index:
        data.index = index 
      error = data.index
      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1 style="padding-left: 19%;">עריכת תקלה</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')       
      with open('app/templates/mini_raam/edit/mini_raam_edit_data_errors.html','w', encoding='utf-8-sig') as f:
        f.writelines([dphtml + '\n' + r'''
<div class="col form-group second-paragraph">
<label>שים לב ! </label>
<br>
<label>למחיקת שורה יש לבחור רק מספר תקלה!</label>
<br>
<label>בעריכת שורה יש להכניס את כל הערכים מחדש</label>
</div>
<br>
<div class="row">
  <div class="col form-group">
    <label for="">בחר מספר תקלה</label>
    <select class="form-control" name="error">
      {% for i in data %}
        <option>{{ i }}</option>
      {% endfor %}
    </select>
  </div>
  <div class="col form-group">
    <label for="">תפעול</label>
    <input type="text" name="fault_operation" class="form-control" placeholder="אנא הכנס תפעול">
    <br>
  </div>
</div>

<div class="row">
  <div class="col form-group">
    <label for="" class="labelSettings">תאריך סגירה</label>
    <input type="date" name="end_date_error" class="form-control" min="2022-01-01">
    <br>
  </div>
  <div class="col form-group">
    <label for="">מצב</label>
    <select class="form-control" name="situation">
      <option>טופל</option>
      <option>במעקב</option>
      <option>לא טופל</option>
    </select>
    <br>
  </div>
</div>

<div class="container">
  <div class="col form-group" style="text-align: center;">
    <form method="POST">
      <button type="sumbit" name="options" value="option_edit" class="btn btn-outline-success">עדכן</button>
      <button type="sumbit" name="options" value="option_delet" class="btn btn-outline-danger" onclick="fireDeletAlert()">מחיקת שורה</button>
      <button type="sumbit" class="btn btn-outline-dark btn-phone" name="options" value="option_back">לדשבורד</button>
    </form>
  </div>
</div>

<script>
    function fireDeletAlert() {
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: '!התקלה נמחקה בהצלחה',
            showConfirmButton: false,
            timer: 1500
        })
    }      
</script>
</div>
</form>
</section>
</body>
{% endblock %}'''])
        f.close()
      return render_template('mini_raam/edit/mini_raam_edit_data_errors.html', data = error)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        error = int(request.form.get('error')) -1
        fault_operation = request.form.get('fault_operation')
        end_date_error = request.form.get('end_date_error')
        situation = request.form.get('situation')
        
        data = pd.read_csv('app/db/mini_raam/data_errors.csv')
        row_to_edit = data.index[error]
        data.loc[row_to_edit,['תפעול','תאריך טיפול','מצב']] = [fault_operation,end_date_error,situation]
        with open('app/db/mini_raam/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה עודכנה בהצלחה', category="success")
        return redirect(url_for('mini_raam_show_data_errors_technician'))
      
      
      if request.form.get('options') == 'option_delet':
        time.sleep(1.5)
        error = int(request.form.get('error')) -1
        data = pd.read_csv('app/db/mini_raam/data_errors.csv')
        row_to_delet = data.index[error]
        data.drop(row_to_delet, inplace=True, axis=0)
        with open('app/db/mini_raam/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נמחקה בהצלחה', category="success")
        return redirect(url_for('mini_raam_show_data_errors_technician')) 

      if request.form.get("options") == 'option_back':
        return redirect(url_for('mini_raam'))