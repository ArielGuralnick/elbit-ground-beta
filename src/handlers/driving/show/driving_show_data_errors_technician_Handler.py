from flask import render_template, send_file, redirect, url_for
import pandas as pd

async def driving_show_data_errors_technician_Handler(request):
    if request.method == 'GET':       
        data_errors = pd.read_csv('elbit-ground-beta/app/db/driving/data_errors.csv')
        
        dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>דוח תקלות לטכנאי</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')  
        dphtml += data_errors.to_html(table_id="driving_show_data_errors_technician", classes = "table table-hover", border=0)
        with open('elbit-ground-beta/app/templates/driving/show/driving_show_data_errors_technician.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' +'\n' +
            r'''
<div class="container">
  <div class="col form-group" style="text-align: center;">
    <form method="POST">
        <button type="sumbit" class="btn btn-outline-success" name="options" value="option_add">הוספת תקלה לא יודע עוד לאיזה דף להפנות</button>
        <button type="sumbit" class="btn btn-outline-danger" name="options" value="option_edit">עריכת שורה</button>
        <button type="sumbit" class="btn btn-outline-secondary" name="options" value="option_csv">פתיחת דוח באקסל</button>
    </form>
  </div>
</div>
</form>
</section>
<script type="text/javascript">
    $('#driving_show_data_errors_technician').DataTable();
</script>
</body>
{% endblock %}'''])
            f.close()
        return render_template('driving/show/driving_show_data_errors_technician.html')
   
    elif request.method == 'POST':
        if request.form.get("options") == 'option_csv':
            return send_file('db/driving/data_errors.csv',
            mimetype='text/csv',attachment_filename='דוח תקלות מאמני נהיגה.csv',
            as_attachment=True)
        
        elif request.form.get("options") == 'option_edit':
            return redirect(url_for('driving_edit_data_errors'))

#        elif request.form.get("options") == 'option_add':
        

        

