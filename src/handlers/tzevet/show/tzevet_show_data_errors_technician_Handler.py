from flask import render_template, send_file, redirect, url_for
import pandas as pd

async def tzevet_show_data_errors_technician_Handler(request):
    if request.method == 'GET':       
        data_errors = pd.read_csv('app/db/tzevet/data_errors.csv')
        
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
        index = data_errors.index + 1    # adding 1 to index (start from 1, not 0)
        for i in index:
            data_errors.index = index
        dphtml += data_errors.to_html(table_id="tzevet_show_data_errors_technician", classes = "table table-hover", border=0)
        with open('app/templates/tzevet/show/tzevet_show_data_errors_technician.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' +'\n' +
            r'''
<div class="container">
  <div class="col form-group" style="text-align: center;">
    <form method="POST">
        <button type="sumbit" class="btn btn-outline-success" name="options" value="option_add">הוספת תקלה</button>
        <button type="sumbit" class="btn btn-outline-danger" name="options" value="option_edit">עריכת שורה</button>
        <button type="sumbit" class="btn btn-phone btn-outline-secondary" name="options" value="option_csv">דוח אקסל</button>
        <button type="sumbit" class="btn btn-outline-dark btn-phone" name="options" value="option_back">לדשבורד</button>
    </form>
  </div>
</div>
</form>
</section>
<script type="text/javascript">
    $('#tzevet_show_data_errors_technician').DataTable();
</script>
</body>
{% endblock %}'''])
            f.close()
        return render_template('tzevet/show/tzevet_show_data_errors_technician.html')
   
    elif request.method == 'POST':
        if request.form.get("options") == 'option_csv':
            return send_file('db/tzevet/data_errors.csv',
            mimetype='text/csv',attachment_filename='דוח תקלות מאמני צוות.csv',
            as_attachment=True)
        
        elif request.form.get("options") == 'option_edit':
            return redirect(url_for('tzevet_edit_data_errors'))

        elif request.form.get("options") == 'option_add':
            return redirect(url_for('tzevet_insert_error'))

        elif request.form.get("options") == 'option_back':
            return redirect(url_for('tzevet_technician'))