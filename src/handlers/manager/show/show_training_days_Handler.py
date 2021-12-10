from flask import render_template, send_file
import pandas as pd

async def show_training_days_Handler(request):
    if request.method == 'GET':       
      data_training = pd.read_csv('elbit-ground-beta/app/db/manager/order_training.csv')
      driving_training = pd.read_csv('elbit-ground-beta/app/db/manager/driving_order_training.csv')
        
      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>דוחות סיכום ימי אימון</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')        
      dphtml += data_training.to_html(table_id="show_activity", classes = "table table-hover", border=0)
      dphtml += driving_training.to_html(table_id="driving_show_activity", classes = "table table-hover", border=0)
      with open('elbit-ground-beta/app/templates/manager/show/show_training_days.html','w', encoding='utf-8-sig') as f:
          f.writelines([dphtml + '\n' + r'<br>' + '\n' +
        r'''
<div class='col form-group'>
  <button type="sumbit" name="options" value="option1" class="btn btn-outline-secondary">ייצא לאקסל מאמני שוטף</button>
  <button type="sumbit" name="options" value="option2" class="btn btn-outline-secondary">ייצא לאקסל מאמני נהיגה</button>
</div>
</form>
</section>
<script type="text/javascript">
  $('#show_activity').DataTable();
  $('#driving_show_activity').DataTable();
</script>
</body>
{% endblock %}'''])
          f.close()
      return render_template('manager/show/show_training_days.html')

    if request.method == 'POST': 
      if request.form.get('options') == 'option1':
        return send_file('db/manager/order_training.csv',
        mimetype='text/csv',attachment_filename='Full_Training_days.csv',
        as_attachment=True)

      elif request.form.get('options') == 'option2':
        return send_file('db/manager/driving_order_training.csv',
        mimetype='text/csv',attachment_filename='Full_Driving_Training_days.csv',
        as_attachment=True)
    
