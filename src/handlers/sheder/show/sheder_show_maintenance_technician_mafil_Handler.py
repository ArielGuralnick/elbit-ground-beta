from flask import render_template, redirect, url_for,flash
import pandas as pd
from myboto3 import upload_files
import os, sys

async def sheder_show_maintenance_technician_mafil_Handler(request):

    if request.method == 'GET':
        data = pd.read_csv('app/db/sheder/maintenance.csv')
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
<section id="show_data_errors" dir="rtl" lang="he">''')
        dphtml += data.to_html(table_id="show_maintenance_technician_mafil", classes = "table table-hover", border=0, index=False)
        with open('app/templates/sheder/show/sheder_show_maintenance_technician_mafil.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' + '\n' + r"</form>" + '\n' + r"</section>" + '\n' +
            r'''<section id="insertError" dir="rtl" lang="he">
    <form action="" method="post">
    <div class = "row">
        <div class="col form-group">
          <label for="">מאמן</label>
          <select class="form-control" name="type_of_simulator">
            <option>נייד 987</option>
            <option>נייד 988</option>
            <option>נייד 989</option>
          </select>
          <br>
        </div>
        <div class="col form-group">
          <label for="" class="labelSettings">תאריך</label>
          <input type="date" name="date_upload" class="form-control" min="2021-01-01">
          <br>
        </div>
    </div>
    <div class = "row">
        <div class="col form-group">
          <label for="" class="labelSettings">מה הפער</label>
          <textarea class="form-control" name= "disparity"  rows="2" placeholder="אנא הסבר"></textarea>
          <br>
        </div>
        <div class="col form-group">
          <label for="">טופל \ לא טופל</label>
          <select class="form-control" name = "status">
            <option>V</option>
            <option>X</option>
          </select>
          <br>
        </div>
        <div class="col form-group">
          <label for="" class="labelSettings">תאריך טיפול</label>
          <input type="date" name="date_treatment" class="form-control" min="2021-01-01">
          <br>
        </div>
    </div>
</section>

<script type="text/javascript">
  $('#show_maintenance_technician_mafil').DataTable();
</script>

<div class="container">
<div class="col form-group" style="text-align: center;">
    <form method="POST">
        <button type="sumbit" class="btn btn-outline-success" name="options" value="option_add">הוספת פער</button>
        <button type="sumbit" class="btn btn-outline-danger" name="options" value="option_edit">עריכת שורה</button>
    </form>
</div>
</div>
</body>
{% endblock %}'''])
            f.close()
        return render_template('sheder/show/sheder_show_maintenance_technician_mafil.html')

    elif request.method == 'POST':
        if request.form.get("options") == 'option_add':
            type_of_simulator = request.form.get('type_of_simulator')
            date_upload = request.form.get('date_upload')
            disparity = request.form.get('disparity')
            status = request.form.get('status')
            date_treatment = request.form.get('date_treatment')

            if date_upload == "" or disparity == "" :
                flash(f'!נא למלא את כל הערכים', category="danger")
            else:
                field_content = ['מאמן','תאריך','מה הפער','טופל / לא טופל','תאריך טיפול']
                data_errors = pd.DataFrame([{'מאמן' : type_of_simulator,'תאריך' : date_upload,
                'מה הפער' : disparity, 'טופל / לא טופל':status, 'תאריך טיפול': date_treatment}], columns=field_content)
                with open('app/db/sheder/maintenance.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    data_errors.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
                    flash(f'!הפער תועד בהצלחה', category="success")
            
            src_upload_file_path = "app/db/sheder/maintenance.csv"
            bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
            upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
            return redirect(url_for('sheder_show_maintenance_technician_mafil'))

        elif request.form.get("options") == 'option_edit':
            return redirect(url_for('sheder_edit_maintenance_technician_mafil'))