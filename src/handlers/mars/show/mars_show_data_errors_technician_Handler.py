from flask import render_template, send_file, redirect, url_for
import pandas as pd

async def mars_show_data_errors_technician_Handler(request):
    if request.method == 'GET':       
        important_columns = ['תאריך העלאה','מספר מחולל','סוג התקלה', 'תפעול התקלה', 'סוג עמדה', 'באיזה מחשב','זמן השבתה']
        data_errors = pd.read_csv('app/db/mars/data_errors.csv')
        
        dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1 style="padding-left: 15%;">דוח תקלות לטכנאי</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')  
        index = data_errors.index + 1    # adding 1 to index (start from 1, not 0)
        for i in index:
            data_errors.index = index
        dphtml += data_errors.to_html(table_id="mars_show_data_errors_technician", classes = "table table-see-all-errors table-hover", border=0, columns=important_columns)
        with open('app/templates/mars/show/mars_show_data_errors_technician.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' +'\n' +
            r'''
<form method="POST">
    <button type="sumbit" class="btn btn-outline-secondary" name="options" value="option3">דוח אקסל</button>
    <button type="sumbit" class="btn btn-outline-dark btn-phone" name="options" value="option_back">לדשבורד</button>   
</form>
</div>   
</form>
</section>
<script type="text/javascript">
    $('#mars_show_data_errors_technician').DataTable();
</script>
</body>
{% endblock %}'''])
            f.close()
        return render_template('mars/show/mars_show_data_errors_technician.html')
   
    elif request.method == 'POST':
        if request.form.get("options") == 'option3':
            return send_file('db/mars/data_errors.csv',
            mimetype='text/csv',attachment_filename='דוח תקלות מרס.csv',
            as_attachment=True)
    
        elif request.form.get("options") == 'option_back':
            return redirect(url_for('mars_technician'))