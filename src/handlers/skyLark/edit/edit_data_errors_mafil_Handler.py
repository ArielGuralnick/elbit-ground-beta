from flask import render_template, flash, redirect, url_for
import pandas as pd
from pandas.core.indexes.base import Index
import time

async def edit_data_errors_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('app/db/skyLark/data_errors.csv')
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
      with open('app/templates/skyLark/edit/edit_data_errors_mafil.html','w', encoding='utf-8-sig') as f:
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
  <label for="">סוג התקלה</label>
  <input type="text" name="type_of_fault"class="form-control" placeholder="אנא הכנס תקלה">
</div>
<div class="col form-group">
  <label for="">תפעול התקלה</label>
  <input type="text" name="fault_operation"class="form-control" placeholder="אנא הכנס תפעול">
</div>
</div>

<div class="row">
<div class="col form-group">
  <label for="">באיזה מחשב</label>
  <select class="form-control" name="computer">
    <option>IGS</option>
    <option>STU</option>
    <option>IOS</option>
    <option>LOGGER</option>
    <option>BE</option>
    <option>INST</option>
    <option>מקודד חוזי</option>
    <option>מגש</option>
    <option>אחר</option>
  </select>
</div>
<div class="col form-group">
  <label for="">טופל \ לא טופל</label>
  <select class="form-control" name = "situation">
    <option>V</option>
    <option>X</option>
  </select>
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
      return render_template('skyLark/edit/edit_data_errors_mafil.html', data = error)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        error = int(request.form.get('error'))
        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        computer = request.form.get('computer')
        situation = request.form.get('situation')
        
        data = pd.read_csv('app/db/skyLark/data_errors.csv')
        row_to_edit = data.index[error]
        data.loc[row_to_edit,['סוג התקלה','תפעול התקלה','באיזה מחשב','טופל \ לא טופל']] = [type_of_fault,fault_operation,computer,situation]
        with open('app/db/skyLark/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה עודכנה בהצלחה', category="success")
        return redirect(url_for('show_data_errors_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        time.sleep(1.5)
        error = int(request.form.get('error'))
        data = pd.read_csv('app/db/skyLark/data_errors.csv')
        row_to_delet = data.index[error]
        data.drop(row_to_delet, inplace=True, axis=0)
        with open('app/db/skyLark/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נמחקה בהצלחה', category="success")
        return redirect(url_for('show_data_errors_mafil'))

      if request.form.get("options") == 'option_back':
        return redirect(url_for('skyLark_mafil'))