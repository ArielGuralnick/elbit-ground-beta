from flask import render_template, redirect, url_for
import pandas as pd


async def show_maintenance_technician_mafil_Handler(request):

    if request.method == 'GET':
        data = pd.read_csv('elbit-ground-beta/app/db/maintenance.csv')
        dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>פערי מאמן</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')
        dphtml += data.to_html(classes = "table table-hover", border=0, index=False)
        with open('elbit-ground-beta/app/templates/show_maintenance_technician_mafil.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' + '\n' + r"</form>" + '\n' + r"</section>" + '\n' +
            r'''
<div class="container">
<div class="row col form-group" style="text-align: center;">
    <form method="POST">
        <button type="sumbit" class="btn btn-outline-success" name="options" value="option1">הוספת פער</button>
        <button type="sumbit" class="btn btn-outline-danger" name="options" value="option2">עריכת שורה</button>
    </form>
</div>
</div>
</body>
{% endblock %}'''])
            f.close()
        return render_template('show_maintenance_technician_mafil.html')

    elif request.method == 'POST':
        if request.form.get("options") == 'option1':
            return redirect(url_for('insert_maintenance_technician_mafil'))
        elif request.form.get("options") == 'option2':
            return redirect(url_for('edit_maintenance_technician_mafil'))
        
