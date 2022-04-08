from flask import render_template, flash, redirect, url_for
import pandas as pd
import time

async def driving_edit_tasks_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('app/db/driving/tasks.csv')
      achievements = data["הישגים נדרשים"]
      
      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1 style="margin-left: 15%;">עריכת משימות</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')       
      with open('app/templates/driving/edit/driving_edit_tasks_mafil.html','w', encoding='utf-8-sig') as f:
        f.writelines([dphtml + '\n' + r'''
<div class="container">
    <div class="col form-group">
    <label for="">בחר הישג נדרש לעריכה</label>
    <select class="form-control" name="achievements">
        {% for i in data %}
            <option>{{ i }}</option>
        {% endfor %}
    </select>
    </div>
    <div class="col form-group">
    <label for="">סטטוס ביצוע</label>
    <select class="form-control" name="status">
        <option>לא בוצע</option>
        <option>בהרצה</option>
        <option>בוצע</option>
    </select>
    </div>
    <div class="col form-group">
          <label for="" class="labelSettings">תאריך לביצוע</label>
          <input type="date" name="date" class="form-control" min="2022-01-01">
          <br>
    </div>
</div>

<script>
    function fireDeletAlert() {
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: '!המשימה נמחקה בהצלחה',
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
            title: '!המשימה עודכנה בהצלחה',
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
      return render_template('driving/edit/driving_edit_tasks_mafil.html', data = achievements)
  
    elif request.method == 'POST':
      time.sleep(1.5)
      if request.form.get('options') == 'option_edit':
        achievements = request.form.get('achievements')
        status = request.form.get('status')
        date = request.form.get('date')
        data = pd.read_csv('app/db/driving/tasks.csv')
        row_to_edit = data.index[data['הישגים נדרשים'] == achievements]
        data.loc[row_to_edit,['סטטוס ביצוע','תאריך לביצוע']] = [status,date]
        with open('app/db/driving/tasks.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!המשימה עודכנה בהצלחה', category="success")
        return redirect(url_for('driving_show_tasks_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        achievements = request.form.get('achievements')
        data = pd.read_csv('app/db/driving/tasks.csv')
        row_to_delet = data.index[data['הישגים נדרשים'] == achievements]
        data.drop(row_to_delet, inplace=True, axis=0)
      
        with open('app/db/driving/tasks.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!המשימה נמחקה בהצלחה', category="success")
        return redirect(url_for('driving_show_tasks_mafil'))

      if request.form.get("options") == 'option_back':
        return redirect(url_for('driving_mafil'))