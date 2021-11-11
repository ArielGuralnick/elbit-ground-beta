from flask import render_template
import pandas as pd

async def show_training_days_Handler(request):
    if request.method == 'GET':       
        important_columns = ['סוג מאמן','תאריך התחלה','שעת התחלה','תאריך סיום','שעת סיום']
        data_training = pd.read_csv('elbit-ground-beta/app/db/order_training.csv')
        
        dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
        r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
        '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
        '\n' + '</a>' + '\n' + '<h1>דוח סיכום ימי אימון</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
        '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
        '\n' + '<form action="" method="post">' + '\n')        
        with open('elbit-ground-beta/app/templates/show_training_days.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' + '\n' + 
          r'''<div class="col-md-3 form-group">
          <label for="">בחר סוג מאמן</label>
          <select class="form-control" name="type_simulator">
            <option>אנא בחר מאמן</option>
            <option>רוכב שמיים</option>
            <option>מרס</option>
            <option>מורשת</option>
            <option>רעם</option>
          </select>
          <br>
          <form method="POST">
          <button type="sumbit" class="btn btn-outline-success">חפש</button>
          </form>
          '''+ '\n' + r"</div>" + '\n' +
          r'''<div class='col-md-3 form-group'>
          <label for="" class="labelSettings">אנא בחר תאריך</label>
          <input type="date" name="date_start" class="form-control">
          <br>
          <form method="POST">
          <button type="sumbit" class="btn btn-outline-success">חפש</button>
          </form>
          ''' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
            f.close()
        return render_template('show_training_days.html')

    if request.method == 'POST':       
        important_columns = ['סוג מאמן','תאריך התחלה','שעת התחלה','תאריך סיום','שעת סיום']
        data_training = pd.read_csv('elbit-ground-beta/app/db/order_training.csv')
        type_simulator = request.form.get('type_simulator')
        date_start = request.form.get('date_start')
        
        specific_simulator = data_training.loc[data_training['סוג מאמן'] ==type_simulator]
        specific_date = data_training.loc[data_training['תאריך התחלה'] ==date_start]

        dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
        r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
        '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
        '\n' + '</a>' + '\n' + '<h1>דוח סיכום ימי אימון</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
        '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
        '\n' + '<form action="" method="post">' + '\n')        
        dphtml += specific_simulator.to_html(classes = "table table-hover", border=0, columns=important_columns)
        dphtml += specific_date.to_html(classes = "table table-hover", border=0, columns=important_columns)
        with open('elbit-ground-beta/app/templates/show_training_days.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' + '\n' + 
          r'''<div class="col-md-3 form-group">
          <label for="">בחר סוג מאמן</label>
          <select class="form-control" name="type_simulator">
            <option>אנא בחר מאמן</option>
            <option>רוכב שמיים</option>
            <option>מרס</option>
            <option>מורשת</option>
            <option>רעם</option>
          </select>
          <br>
          <form method="POST">
          <button type="sumbit" class="btn btn-outline-success">חפש</button>
          </form>
          '''+ '\n' + r"</div>" + '\n' +
          r'''<div class='col-md-3 form-group'>
          <label for="" class="labelSettings">אנא בחר תאריך</label>
          <input type="date" name="date_start" class="form-control">
          <br>
          <form method="POST">
          <button type="sumbit" class="btn btn-outline-success">חפש</button>
          </form>
          ''' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
            f.close()
        return render_template('show_training_days.html')
    
