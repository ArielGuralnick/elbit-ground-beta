from flask import render_template, flash, redirect, url_for
import pandas as pd

async def driving_edit_maintenance_technician_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('elbit-ground-beta/app/db/moreshet/maintenance.csv')
      disparity = data["מה הפער"]

      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>עריכת פער</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')       
      with open('elbit-ground-beta/app/templates/moreshet/edit/moreshet_edit_maintenance_mafil.html','w', encoding='utf-8-sig') as f:
        f.writelines([dphtml + '\n' + r'''
<div class="container">
<div class="row">
<div class="col-md-3 form-group">
<label for="">בחר פער לעריכה</label>
<select class="form-control" name="disparity">
  {% for i in data %}
    <option>{{ i }}</option>
  {% endfor %}
</select>
</div>
<div class="col-md-3 form-group">
  <label for="">טופל \ לא טופל</label>
  <select class="form-control" name="status">
    <option>V</option>
    <option>X</option>
  </select>
</div>
</div>
</div>
<div class="container">
<div class="col form-group" style="text-align: center;">
  <form method="POST">
    <button type="sumbit" name="options" value="option_edit" class="btn btn-outline-success">עדכן</button>
    <button type="sumbit" name="options" value="option_delet" class="btn btn-outline-danger">מחיקה</button>
  </form>
</div>
</div>'''+ '\n' + r"</div>" + '\n' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
        f.close()
      return render_template('moreshet/edit/moreshet_edit_maintenance_mafil.html', data = disparity)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        disparity = request.form.get('disparity')
        status = request.form.get('status')
        data = pd.read_csv('elbit-ground-beta/app/db/moreshet/maintenance.csv')
        row_to_edit = data.index[data['מה הפער'] == disparity]
        data.loc[row_to_edit, 'טופל / לא טופל'] = status
        with open('elbit-ground-beta/app/db/moreshet/maintenance.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!הפער עודכן בהצלחה', category="success")
        return redirect(url_for('moreshet_show_maintenance_technician_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        disparity = request.form.get('disparity')
        data = pd.read_csv('elbit-ground-beta/app/db/moreshet/maintenance.csv')
        row_to_delet = data.index[data['מה הפער'] == disparity]
        data.drop(row_to_delet, inplace=True, axis=0)
      
        with open('elbit-ground-beta/app/db/moreshet/maintenance.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'הפער נמחק בהצלחה!', category="success")
        return redirect(url_for('moreshet_show_maintenance_technician_mafil'))