from flask import render_template,send_file
import pandas as pd

async def tzevet_show_data_activity_Handler(request):
    if request.method == 'GET':       
        data_activity = pd.read_csv('app/db/tzevet/data_activity.csv')
        
        dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>דוח פעילות מתקן</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">
<div class="container">
<div class="row">
    <div class="col form-group">
        <label for="">סוג מאמן</label>
        <select class="form-control" name="type_of_simulator">
            <option>נייד</option>
            <option>שיזפון</option>
            <option>צאלים</option>
            <option>נחשונים</option>
        </select>
        <br>
    </div>
    <div class="col-sm">
    <form method="POST">
        <button type="sumbit" name="options" value="option1" class="btn btn-outline-success">חפש</button>
    </form>
    </div>
    <div class='col-md-3 form-group'>
    <form method="POST">
        <button type="sumbit" name="options" value="option2" class="btn btn-phone btn-outline-secondary">פתיחת דוח באקסל</button>
    </form>
    </div>
</div>
</div>''')  
        index = data_activity.index + 1    # adding 1 to index (start from 1, not 0)
        for i in index:
            data_activity.index = index      
        dphtml += data_activity.to_html(table_id="show_activity", classes = "table table-hover", border=0)
        with open('app/templates/tzevet/show/tzevet_show_data_activity.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' + '\n' +
            r"</form>" + '\n' + r"</section>" + '\n' + 
            r'<script type="text/javascript">' + '\n' + r"$('#show_activity').DataTable();" + 
            '\n' + r"</script>" + r"</body>" + '\n' + r"{% endblock %}"])
            f.close()
        return render_template('tzevet/show/tzevet_show_data_activity.html')


    if request.method == 'POST':
        if request.form.get('options') == 'option1':
            data_activity = pd.read_csv('app/db/tzevet/data_activity.csv')
            type_of_simulator = request.form.get('type_of_simulator')
            specific_type_of_simulator = data_activity.loc[data_activity['מאמן'] == type_of_simulator]
    
            dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>דוח פעילות מתקן</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">
<div class="container">
<div class="row">
    <div class="col form-group">
        <label for="">סוג מאמן</label>
        <select class="form-control" name="type_of_simulator">
            <option>שיזפון</option>
            <option>בהל"צ</option>
            <option>ביסל"ח</option>
            <option>צאלים</option>
        </select>
        <br>
    </div>
    <div class="col-sm">
    <form method="POST">
        <button type="sumbit" name="options" value="option1" class="btn btn-outline-success">חפש</button>
    </form>
    </div>
    <div class='col-md-3 form-group'>
    <form method="POST">
        <button type="sumbit" name="options" value="option2" class="btn btn-phone btn-outline-secondary">דוח אקסל</button>
    </form>
    </div>
</div>
</div>''')  
            dphtml += specific_type_of_simulator .to_html(table_id="show_activity", classes = "table table-hover", border=0)
            with open('app/templates/tzevet/show/tzevet_show_data_activity.html','w', encoding='utf-8-sig') as f:
                f.writelines([dphtml + '\n' + r'<br>' +
                r"</form>" + '\n' + r"</section>" + '\n' + 
                r'<script type="text/javascript">' + '\n' + r"$('#show_activity').DataTable();" + 
                '\n' + r"</script>" + r"</body>" + '\n' + r"{% endblock %}"])
                f.close()
            return render_template('tzevet/show/tzevet_show_data_activity.html')
            
        elif request.form.get('options') == 'option2':
            return send_file('db/tzevet/data_activity.csv',
            mimetype='text/csv',attachment_filename='דוח פעילות מאמני צוות.csv',
            as_attachment=True)