from flask import render_template, flash, redirect, url_for
import pandas as pd
from pandas.core.indexes.base import Index

async def edit_data_errors_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('elbit-ground-beta/app/db/skyLark/data_errors.csv')
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
      with open('elbit-ground-beta/app/templates/skyLark/edit/edit_data_errors_mafil.html','w', encoding='utf-8-sig') as f:
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
  <label for="">סוג תקלה</label>
  <select class="form-control" name="type_of_fault">
            <option>לא ניתן לשגר מטוס קרקע</option>
            <option>חוזי מתוח / שטוח</option>
            <option>טעינת תרגיל נכשלה ב INST</option>
            <option>הפסקות חשמל</option>
            <option>עכבר \ מקלדת לא עובד</option>
            <option>dubgger - נופל TVIEW</option>
            <option>dubgger - נופל SIMENGINE</option>
            <option>מגש תקוע</option>
            <option>תקלת בסיס נתונים - מופיע מצלמה עם חוזי שחור</option>
            <option>אל תשלח - קרסה אפליקצייה במגש</option>
            <option>ריצודי לל"ק</option>
            <option>מקודד חוזי</option>
            <option>הפצת תרגיל נכשלה במחולל זירה</option>
            <option>מחולל זירה נתקע</option>
            <option>לא רוכש מטוס</option>
            <option>מיתוג IP חוזי</option>
            <option>לל"ק מלא</option>
            <option>תקלת רזולוציה</option>
            <option>טעינת תרגיל נכשלה ב INST</option>
            <option>INST קפוא</option>
            <option>הרוחות ב IOS לא נטענות</option>
            <option>נורת RT מהבהבת</option>
            <option>אחר - קרא למפעיל לתיעוד</option>
  </select>
</div>
<div class="col form-group">
  <label for="">הסבר מורחב במידת הצורך</label>
  <textarea class="form-control" name= "explanation" id="exampleFormControlTextarea1" rows="2" placeholder="אנא הסבר"></textarea>
</div>
</div>

<div class="row">
<div class="col form-group">
  <label for="">תפעול התקלה</label>
  <textarea class="form-control" name = "fault_operation" id="exampleFormControlTextarea1" rows="2" placeholder="אנא הסבר"></textarea>
</div>
<div class="col form-group">
  <label for="">באיזה מחשב</label>
  <select class="form-control" name="computer" id="exampleFormControlSelect1">
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
  <select class="form-control" name = "situation" id="exampleFormControlSelect1">
    <option>V</option>
    <option>X</option>
  </select>
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
      return render_template('skyLark/edit/edit_data_errors_mafil.html', data = error)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        error = int(request.form.get('error'))
        type_of_fault = request.form.get('type_of_fault')
        explanation = request.form.get('explanation')
        fault_operation = request.form.get('fault_operation')
        computer = request.form.get('computer')
        situation = request.form.get('situation')
        data = pd.read_csv('elbit-ground-beta/app/db/skyLark/data_errors.csv')
        row_to_edit = data.index[error]
        data.loc[row_to_edit,['סוג התקלה','הסבר','תפעול התקלה','מחשב','טופל/לא טופל']] = [type_of_fault,explanation,fault_operation,computer,situation]
        with open('elbit-ground-beta/app/db/skyLark/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה עודכנה בהצלחה', category="success")
        return redirect(url_for('show_data_errors_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        error = int(request.form.get('error'))
        data = pd.read_csv('elbit-ground-beta/app/db/skyLark/data_errors.csv')
        row_to_delet = data.index[error]
        data.drop(row_to_delet, inplace=True, axis=0)
      
        with open('elbit-ground-beta/app/db/skyLark/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נמחקה בהצלחה', category="success")
        return redirect(url_for('show_data_errors_mafil'))