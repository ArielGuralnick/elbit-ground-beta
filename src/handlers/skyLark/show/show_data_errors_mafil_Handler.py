from flask import render_template, redirect, url_for, send_file
import pandas as pd

async def show_data_errors_mafil_Handler(request):
    if request.method == 'GET':       
        data_errors = pd.read_csv('app/db/skyLark/data_errors.csv')
        dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>דוח תקלות למפעיל</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')
        index = data_errors.index + 1    # adding 1 to index (start from 1, not 0)
        for i in index:
            data_errors.index = index        
        dphtml += data_errors.to_html(table_id="show_data_errors_mafil", classes = "table table-see-all-errors table-hover", border=0)
        with open('app/templates/skyLark/show/show_data_errors_mafil.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>'  + '\n' + r"</form>",r"</section>",
            r'''
<div class="container">
<div class="col form-group" style="text-align: center;">
    <form method="POST">
        <button type="sumbit" class="btn btn-outline-success" name="options" value="option1">הוספת תקלה</button>
        <button type="sumbit" class="btn btn-outline-danger" name="options" value="option2">עריכה</button>
        <button type="sumbit" class="btn btn-phone btn-outline-secondary" name="options" value="option3">דוח אקסל</button>
        <button type="sumbit" class="btn btn-outline-dark btn-phone" name="options" value="option_back">לדשבורד</button>
    </form>
</div>
</div>
<script type="text/javascript">
$('#show_data_errors_mafil').DataTable();
</script>"
</body>
{% endblock %}'''])
            f.close()
        return render_template('skyLark/show/show_data_errors_mafil.html')

    elif request.method == 'POST':
        if request.form.get("options") == 'option1':
            return redirect(url_for('insert_error'))
        elif request.form.get("options") == 'option2':
            return redirect(url_for('edit_data_errors_mafil'))
        elif request.form.get("options") == 'option3':
            return send_file('db/skyLark/data_errors.csv',
            mimetype='text/csv',attachment_filename='דוח תקלות.csv',
            as_attachment=True)
        elif request.form.get("options") == 'option_back':
            return redirect(url_for('skyLark_mafil'))