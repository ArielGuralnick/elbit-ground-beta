from flask import render_template, flash, redirect, url_for
import pandas as pd

async def edit_work_plan_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('elbit-ground-beta/app/db/work_plan_mafil.csv')
      achievements = data["הישגים נדרשים"]
      
      dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
      r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
      '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
      '\n' + '</a>' + '\n' + '<h1>עריכת תוכנית שנתית</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
      '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
      '\n' + '<form action="" method="post">' + '\n')       
      with open('elbit-ground-beta/app/templates/edit_work_plan_mafil.html','w', encoding='utf-8-sig') as f:
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
<div class="container">
<div class="row col form-group" style="text-align: center;">
  <form method="POST">
    <button type="sumbit" name="options" value="option_edit" class="btn btn-outline-success">עדכן</button>
    <button type="sumbit" name="options" value="option_delet" class="btn btn-outline-danger">מחיקה</button>
  </form>
</div>
</div>'''+ '\n' + r"</div>" + '\n' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
        f.close()
      return render_template('edit_work_plan_mafil.html', data = achievements)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        achievements = request.form.get('achievements')
        status = request.form.get('status')
        data = pd.read_csv('elbit-ground-beta/app/db/work_plan_mafil.csv')
        row_to_edit = data.index[data['הישגים נדרשים'] == achievements]
        data.loc[row_to_edit, 'סטטוס ביצוע'] = status
        with open('elbit-ground-beta/app/db/work_plan_mafil.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!היעד עודכן בהצלחה', category="success")
        return redirect(url_for('show_work_plan_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        achievements = request.form.get('achievements')
        data = pd.read_csv('elbit-ground-beta/app/db/work_plan_mafil.csv')
        row_to_delet = data.index[data['הישגים נדרשים'] == achievements]
        data.drop(row_to_delet, inplace=True, axis=0)
      
        with open('elbit-ground-beta/app/db/work_plan_mafil.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!הפער נמחק בהצלחה', category="success")
        return redirect(url_for('show_work_plan_mafil'))