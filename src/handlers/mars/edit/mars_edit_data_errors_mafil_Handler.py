from flask import render_template, flash, redirect, url_for
import pandas as pd
from pandas.core.indexes.base import Index

async def mars_edit_data_errors_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('elbit-ground-beta/app/db/mars/data_errors.csv')
      error = data.index
      
      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>עריכת תקלה</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')       
      with open('elbit-ground-beta/app/templates/mars/edit/mars_edit_data_errors_mafil.html','w', encoding='utf-8-sig') as f:
        f.writelines([dphtml + '\n' + r'''
<div class="col form-group">
<label>למחיקת שורה יש דבר לבחור רק מספר תקלה</label>
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
    <label for="">סוג התקלה</label>
    <select class="form-control" name="type_of_fault">
        <option>תקלה כלשהי שיש אצל עדי</option>
        <option>תקלה כלשהי שיש אצל עדי</option>
        <option>תקלה כלשהי שיש אצל עדי</option>
        <option>תקלה כלשהי שיש אצל עדי</option>
        <option>תקלה כלשהי שיש אצל עדי</option>
        <option>תקלה כלשהי שיש אצל עדי</option>
    </select>
    <br>
</div>
<div class="col form-group">
    <label for="">תפעול התקלה</label>
    <textarea class="form-control" name = "fault_operation" rows="2" placeholder="אנא הסבר"></textarea>
    <br>
</div>
</div>

<div class="row">
<div class="col form-group">
    <label for="">סוג עמדה</label>
    <select class="form-control" name="type_of_position">
        <option>מבצעית</option>
        <option>מדריך</option>
        <option>כל הכיתה</option>    
    </select>
    <br>
</div>
<div class="col form-group">
    <label for="">באיזה מחשב</label>
    <select class="form-control" name="computer">
        <option>IGS</option>
        <option>STU</option>
        <option>IOS</option>
        <option>LOGGER</option>
        <option>BE</option>
        <option>INST</option>
        <option>אחר</option>
    </select>
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
      return render_template('mars/edit/mars_edit_data_errors_mafil.html', data = error)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        error = int(request.form.get('error'))

        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        type_of_position = request.form.get('type_of_position')
        computer = request.form.get('computer')
        
        data = pd.read_csv('elbit-ground-beta/app/db/mars/data_errors.csv')
        row_to_edit = data.index[error]
        data.loc[row_to_edit,['סוג התקלה','תפעול התקלה','סוג עמדה','באיזה מחשב']] = [type_of_fault,fault_operation,type_of_position,computer]
        with open('elbit-ground-beta/app/db/mars/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה עודכנה בהצלחה', category="success")
        return redirect(url_for('mars_show_data_errors_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        error = int(request.form.get('error'))
        data = pd.read_csv('elbit-ground-beta/app/db/mars/data_errors.csv')
        row_to_delet = data.index[error]
        data.drop(row_to_delet, inplace=True, axis=0)
      
        with open('elbit-ground-beta/app/db/mars/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נמחקה בהצלחה', category="success")
        return redirect(url_for('mars_show_data_errors_mafil'))