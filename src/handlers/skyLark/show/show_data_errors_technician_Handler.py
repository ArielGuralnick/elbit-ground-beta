from flask import render_template, send_file, redirect, url_for
import pandas as pd

async def show_data_errors_technician_Handler(request):
    if request.method == 'GET':       
        important_columns = ['תאריך','עיתוי התקלה','עמדה','סוג התקלה','תפעול התקלה','זמן השבתה']
        data_errors = pd.read_csv('app/db/skyLark/data_errors.csv')
        
        dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>דוח תקלות</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')  
        dphtml += data_errors.to_html(table_id="show_data_errors_technician", classes = "table table-hover", border=0, columns=important_columns)
        with open('app/templates/skyLark/show/show_data_errors_technician.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' +'\n' +
            r'''
<form method="POST">
    <button type="sumbit" class="btn btn-phone btn-outline-secondary" name="options" value="option3">פתיחת דוח באקסל</button>
    <button type="sumbit" class="btn btn-outline-dark btn-phone" name="options" value="option_back">לדשבורד</button>
</form>
</div>   
</form>
</section>
<script type="text/javascript">
    $('#show_data_errors_technician').DataTable();
</script>
</body>
{% endblock %}'''])
            f.close()
        return render_template('skyLark/show/show_data_errors_technician.html')
   
    elif request.method == 'POST':
        if request.form.get("options") == 'option3':
            return send_file('db/skyLark/data_errors.csv',
            mimetype='text/csv',attachment_filename='דוח תקלות רוכ"ש.csv',
            as_attachment=True)
        if request.form.get("options") == 'option_back':
            return redirect(url_for('skyLark_technician'))

      
