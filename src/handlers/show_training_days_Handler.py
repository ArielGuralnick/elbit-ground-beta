from flask import render_template, send_file
import pandas as pd


async def show_training_days_Handler(request):
    if request.method == 'GET':       
      data_training = pd.read_csv('elbit-ground-beta/app/db/order_training.csv')
        
      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>דוח סיכום ימי אימון</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')        
      dphtml += data_training.to_html(table_id="show_activity", classes = "table table-hover", border=0)
      with open('elbit-ground-beta/app/templates/show_training_days.html','w', encoding='utf-8-sig') as f:
          f.writelines([dphtml + '\n' + r'<br>' + '\n' + 
        r'''
<div class='col-md-3 form-group'>
  <button type="sumbit" name="options" value="option3" class="btn btn-outline-secondary">פתיחת דוח באקסל</button>
</div>
</form>
</section>
<script type="text/javascript">
  $('#show_activity').DataTable();
</script>
</body>
{% endblock %}'''])
          f.close()
      return render_template('show_training_days.html')

    if request.method == 'POST':   
      return send_file('db/order_training.csv',
      mimetype='text/csv',attachment_filename='Full_Training_days.csv',
      as_attachment=True)
    
