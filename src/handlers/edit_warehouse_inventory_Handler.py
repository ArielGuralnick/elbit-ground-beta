from flask import render_template, flash, redirect, url_for
import pandas as pd

async def edit_warehouse_inventory_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('elbit-ground-beta/app/db/warehouse_inventory.csv')
      type_of_item = data["סוג הפריט"]
      
      dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
      r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
      '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
      '\n' + '</a>' + '\n' + '<h1>עריכה מחסן רוכב שמיים</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
      '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
      '\n' + '<form action="" method="post">' + '\n')       
      with open('elbit-ground-beta/app/templates/edit_warehouse_inventory.html','w', encoding='utf-8-sig') as f:
        f.writelines([dphtml + '\n' + r'''
<div class="container">
<div class="row">
<div class="col form-group">
<label for="">בחר פריט לעריכה</label>
<select class="form-control" name="type_of_item">
  {% for i in data %}
    <option>{{ i }}</option>
  {% endfor %}
</select>
</div>
<div class="col form-group">
    <label>כמות במלאי</label>
    <input type="number" class="form-control" name="quantity">
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
</div>
<div class="row">
<div class="col form-group">
    <label">הערות</label>
    <input type="text" name="remarks" class="form-control">
    <br>
</div>
</div>
</div>
<div class="container">
<div class="row col form-group" style="text-align: center;">
  <form method="POST">
    <button type="sumbit" name="options" value="option_edit" class="btn btn-outline-success">עדכן</button>
    <button type="sumbit" name="options" value="option_delet" class="btn btn-outline-danger">מחיקה</button>
  </form>
</div>
</div>'''+ '\n' + r"</div>" + '\n' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
        f.close()
      return render_template('edit_warehouse_inventory.html', data = type_of_item)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        type_of_item = request.form.get('type_of_item')
        quantity = request.form.get('quantity')
        needs_to_complete = request.form.get('needs_to_complete')
        remarks = request.form.get('remarks')
        data = pd.read_csv('elbit-ground-beta/app/db/warehouse_inventory.csv')
        row_to_edit = data.index[data['סוג הפריט'] == type_of_item]
        data.loc[row_to_edit, ['כמות במלאי','נדרש להשלים \ לרכוש','הערות']] = [quantity, needs_to_complete, remarks]
        with open('elbit-ground-beta/app/db/warehouse_inventory.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!השורה עודכנה בהצלחה', category="success")
        return redirect(url_for('warehouse_inventory'))
      
      
      if request.form.get('options') == 'option_delet':
        type_of_item = request.form.get('type_of_item')
        data = pd.read_csv('elbit-ground-beta/app/db/warehouse_inventory.csv')
        row_to_delet = data.index[data['סוג הפריט'] == type_of_item]
        data.drop(row_to_delet, inplace=True, axis=0)
      
        with open('elbit-ground-beta/app/db/warehouse_inventory.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!השורה נמחקה בהצלחה', category="success")
        return redirect(url_for('warehouse_inventory'))