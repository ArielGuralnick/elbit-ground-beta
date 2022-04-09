from flask import render_template, send_file
import pandas as pd

async def moreshet_show_data_errors_technician_Handler(request):
    if request.method == 'GET':       
        important_columns = ['תאריך העלאה','מספר תא','סוג התקלה', 'תפעול התקלה', 'סוג עמדה', 'באיזה מחשב','זמן השבתה']
        data_errors = pd.read_csv('app/db/moreshet/data_errors.csv')
        
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
        dphtml += data_errors.to_html(table_id="moreshet_show_data_errors_technician", classes = "table table-see-all-errors table-hover", border=0, columns=important_columns)
        with open('app/templates/moreshet/show/moreshet_show_data_errors_technician.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' +'\n' +
            r'''
<form method="POST">
    <button type="sumbit" class="btn btn-outline-secondary">דוח אקסל</button>
</form>
</div>   
</form>
</section>
<script type="text/javascript">
    $('#moreshet_show_data_errors_technician').DataTable();
</script>
</body>
{% endblock %}'''])
            f.close()
        return render_template('moreshet/show/moreshet_show_data_errors_technician.html')
   
    elif request.method == 'POST':
        return send_file('db/moreshet/data_errors.csv',
        mimetype='text/csv',attachment_filename='דוח תקלות מורשת.csv',
        as_attachment=True)