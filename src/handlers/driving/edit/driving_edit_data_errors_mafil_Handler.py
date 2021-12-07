from flask import render_template, flash, redirect, url_for
import pandas as pd
from pandas.core.indexes.base import Index

async def driving_edit_data_errors_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('elbit-ground-beta/app/db/driving/data_errors.csv')
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
      with open('elbit-ground-beta/app/templates/driving/edit/driving_edit_data_errors_mafil.html','w', encoding='utf-8-sig') as f:
        f.writelines([dphtml + '\n' + r'''
<div class="col form-group">
<label>שים לב ! </label>
<br>
<label>למחיקת שורה יש לבחור רק מספר תקלה</label>
<br>
<label>בעריכת שורה יש להכניס את כל הערכים מחדש</label>
</div>
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
    <label for="">טופל \ לא טופל</label>
    <select class="form-control" name = "situation">
      <option>V</option>
      <option>X</option>
    </select>
    <br>
  </div>
</div>
<div class="row">
  <div class="col form-group">
    <label for="">שם המטפל</label>
    <input type="text" name="name_treat"class="form-control" placeholder="שם">
    <br>
  </div>
  <div class="col form-group">
    <label for="" class="labelSettings">שעת טיפול</label>
    <input type="time" name="time_treatment" class="form-control">
    <br>
  </div>
</div>

<div class="container">
  <div class="col form-group" style="text-align: center;">
    <form method="POST">
      <button type="sumbit" name="options" value="option_edit" class="btn btn-outline-success">עדכן</button>
      <button type="sumbit" name="options" value="option_delet" class="btn btn-outline-danger">מחיקת שורה</button>
    </form>
  </div>
</div>
</div>
</form>
</section>
</body>
{% endblock %}'''])
        f.close()
      return render_template('driving/edit/driving_edit_data_errors_mafil.html', data = error)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        error = int(request.form.get('error'))
        situation = request.form.get('situation')
        name_treat = request.form.get('name_treat')
        time_treatment = request.form.get('time_treatment')
        
        data = pd.read_csv('elbit-ground-beta/app/db/driving/data_errors.csv')
        row_to_edit = data.index[error]
        data.loc[row_to_edit,['טופל \ לא טופל','שם המטפל','שעת טיפול']] = [situation, name_treat, time_treatment]
        with open('elbit-ground-beta/app/db/driving/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה עודכנה בהצלחה', category="success")
        return redirect(url_for('driving_show_data_errors_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        error = int(request.form.get('error'))
        data = pd.read_csv('elbit-ground-beta/app/db/driving/data_errors.csv')
        row_to_delet = data.index[error]
        data.drop(row_to_delet, inplace=True, axis=0)
        with open('elbit-ground-beta/app/db/driving/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נמחקה בהצלחה', category="success")
        return redirect(url_for('driving_show_data_errors_mafil'))