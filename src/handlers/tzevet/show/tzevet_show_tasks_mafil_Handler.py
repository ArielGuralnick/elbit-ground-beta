from flask import render_template, flash, redirect, url_for
import pandas as pd
import time
from myboto3 import upload_files
import os, sys

async def tzevet_show_tasks_mafil_Handler(request):

    if request.method == 'GET':
        data = pd.read_csv('app/db/tzevet/tasks.csv')
        dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1 style="padding-left: 19%;">משימות</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">''')
        dphtml += data.to_html(classes = "table table-hover", border=0, index=False)
        with open('app/templates/tzevet/show/tzevet_show_tasks_mafil.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>'  + '\n' + r'</section>' + '\n' + 
            r'''<section id="insertError" dir="rtl" lang="he">
    <form action="" method="post">
    <div class = "row">
        <div class="col form-group">
            <label>נושא</label>
            <input type="text" name="subject" class="form-control">
            <br>
        </div>
        <div class="col form-group">
            <label>מטרה</label>
            <input type="text" name="goal" class="form-control">
            <br>
        </div>
        <div class="col form-group">
            <label>הישגים נדרשים</label>
            <input type="text" name="achievements" class="form-control">
            <br>
        </div>
    </div>
    <div class = "row">
        <div class="col form-group">
            <label>גורם מבצע</label>
            <input type="text" name="responsible" class="form-control">
            <br>
        </div>
        <div class="col form-group">
          <label for="" class="labelSettings">תאריך לביצוע</label>
          <input type="date" name="date" class="form-control" min="2022-01-01">
          <br>
        </div>
        <div class="col form-group">
            <label for="">סטטוס ביצוע</label>
            <select class="form-control"  name="status">
                <option>לא בוצע</option>
                <option>בהרצה</option>
                <option>בוצע</option>
            </select>
          <br>
        </div>
    </div>
</section>

<div class="container">
    <div class="col form-group" style="text-align: center;">
        <button type="sumbit" class="btn btn-outline-success" name="options" value="option_add" onclick="fireSweetAlert()">הוספת שורה</button>
        <button type="sumbit" class="btn btn-outline-danger" name="options" value="option_edit">עריכת שורה</button>
        <button type="sumbit" class="btn btn-outline-dark btn-phone" name="options" value="option_back">לדשבורד</button>
    </div>
</div>

<!-- Alert Message after clicking on sumbit.-->
<script>
    function fireSweetAlert() {
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: '!היעד התווסף בהצלחה',
            showConfirmButton: false,
            timer: 1500
        })
    }      
</script>
</form>
</body>
{% endblock %}'''])
            f.close()
        return render_template('tzevet/show/tzevet_show_tasks_mafil.html')

    elif request.method == 'POST':
        if request.form.get("options") == 'option_add':
            time.sleep(1.5)
            subject = request.form.get('subject')
            goal = request.form.get('goal')
            achievements = request.form.get('achievements')
            responsible = request.form.get('responsible')
            date = request.form.get('date')
            status = request.form.get('status')

            if subject == "" or goal == "" or achievements =="" or responsible =="":
                flash(f'!נא למלא את כל הערכים', category="danger")
            else:
                field_content = ['נושא','מטרה','הישגים נדרשים','גורם מבצע','תאריך לביצוע' ,'סטטוס ביצוע']
                data = pd.DataFrame([{'נושא' : subject, 'מטרה' : goal, 'הישגים נדרשים':achievements, 'גורם מבצע': responsible,'תאריך לביצוע': date, 'סטטוס ביצוע': status}], columns=field_content)
                current_cd_path = os.getcwd()
                print("CD=", current_cd_path)
                sys.stdout.flush()
                with open('app/db/tzevet/tasks.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    data.to_csv(file, index=False, na_rep='null',header=file.tell()==0, encoding='utf-8-sig')
                    flash(f'! השורה התווספה בהצלחה', category="success")
            
            src_upload_file_path = "app/db/tzevet/tasks.csv"
            bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
            upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
            return redirect(url_for('tzevet_show_tasks_mafil'))

        elif request.form.get("options") == 'option_edit':
            return redirect(url_for('tzevet_edit_tasks_mafil'))

        elif request.form.get("options") == 'option_back':
            return redirect(url_for('tzevet_mafil'))