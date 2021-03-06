from flask import render_template, flash, redirect, url_for, send_file
import pandas as pd
from myboto3 import upload_files
import os, sys

async def mini_raam_show_warehouse_inventory_Handler(request):

    if request.method == 'GET':
        data = pd.read_csv('app/db/mini_raam/warehouse_inventory.csv')
        dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>מלאי מחסן </h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">''')
        dphtml += data.to_html(classes = "table table-hover", border=0, index=False)
        with open('app/templates/mini_raam/show/mini_raam_show_warehouse_inventory.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>'  + '\n' + r'</section>' + '\n' + 
            r'''<section id="insertError" dir="rtl" lang="he">
<form action="" method="post">
    <div class = "row">
        <div class="col form-group">
            <label>סוג הפריט</label>
            <input type="text" name="type_of_item" class="form-control">
            <br>
        </div>
        <div class="col form-group">
            <label>דגם</label>
            <input type="text" name="model" class="form-control">
            <br>
        </div>
        <div class="col form-group">
            <label>כמות במלאי</label>
            <input type="number" name="quantity"  class="form-control" min="0">
            <br>
        </div>
        <div class="col form-group">
            <label >נדרש להשלים \ לרכוש</label>
            <select class="form-control" name = "needs_to_complete">
                <option>לא</option>
                <option>כן</option>
            </select>
            <br>
        </div>
        <div class="col form-group">
            <label>הערות</label>
            <input type="text" name="remarks" class="form-control">
            <br>
        </div>
    </div>
</section>

<div class="container">
    <div class="col form-group" style="text-align: center;">
        <button type="sumbit" class="btn btn-outline-success" name="options" value="option_add">הוספת פריט</button>
        <button type="sumbit" class="btn btn-outline-danger" name="options" value="option_edit">עריכת פריט</button>
        <button type="sumbit" class="btn btn-phone btn-outline-secondary" name="options" value="option_open_csv">דוח אקסל</button>
        <button type="sumbit" class="btn btn-outline-dark btn-phone" name="options" value="option_back">לדשבורד</button>
    </div>
</div>
</form>
</body>
{% endblock %}'''])
            f.close()
        return render_template('mini_raam/show/mini_raam_show_warehouse_inventory.html')

    elif request.method == 'POST':
        if request.form.get("options") == 'option_add':
            type_of_item = request.form.get('type_of_item')
            model = request.form.get('model')
            quantity = request.form.get('quantity')
            needs_to_complete = request.form.get('needs_to_complete')
            remarks = request.form.get('remarks')

            if type_of_item == "" or model == "" or quantity =="" :
                flash(f'! נא למלא את כל הערכים', category="danger")
            else:
                field_content = ['סוג הפריט','דגם','כמות במלאי','נדרש להשלים \ לרכוש','הערות']
                data = pd.DataFrame([{'סוג הפריט' : type_of_item, 'דגם' : model, 'כמות במלאי':quantity, 'נדרש להשלים \ לרכוש': needs_to_complete, 'הערות': remarks}], columns=field_content)
                current_cd_path = os.getcwd()
                print("CD=", current_cd_path)
                sys.stdout.flush()
                with open('app/db/mini_raam/warehouse_inventory.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    data.to_csv(file, index=False, na_rep='null',header=file.tell()==0, encoding='utf-8-sig')
                    flash(f'!הפריט התווסף למלאי', category="success")
            
            src_upload_file_path = "app/db/mini_raam/warehouse_inventory.csv"
            bucket_dest_file_path = src_upload_file_path.replace('/app/db/', '').replace('app/db/', '')
            upload_files.upload_to_s3_bucket(src_upload_file_path, bucket_dest_file_path)
            return redirect(url_for('mini_raam_show_warehouse_inventory'))

        elif request.form.get("options") == 'option_edit':
            return redirect(url_for('mini_raam_edit_warehouse_inventory'))
        
        elif request.form.get("options") == 'option_open_csv':
            return send_file('db/mini_raam/warehouse_inventory.csv',
            mimetype='text/csv',attachment_filename='מחסן מיני רעם.csv',
            as_attachment=True)

        elif request.form.get("options") == 'option_back':
            return redirect(url_for('mini_raam'))