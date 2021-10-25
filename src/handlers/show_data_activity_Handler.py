from flask import render_template
import pandas as pd

async def show_data_activity_Handler(request):
    if request.method == 'GET':       
        data_activity = pd.read_csv('elbit-ground-beta/app/db/data_activity.csv')
        dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
        r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
        '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
        '\n' + '</a>' + '\n' + '<h1>דוח פעילות מתקן </h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
        '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_activity" dir="rtl" lang="he">' +
        '\n' + '<form action="" method="post">' + '\n' +
        r'''<div class="col-md-3 form-group">
                <label for="">סוג מאמן</label>
                <select class="form-control" id="exampleFormControlSelect1" name="position_upload">
                    <option>אנא בחר מאמן</option>
                    <option>עמדות פרט</option>
                    <option>משימה 1</option>
                    <option>משימה 2</option>
                    <option>משימה 3</option>
                    <option>משימה 4</option>
                </select>
                <br>
                <form method="POST">
                    <button type="sumbit" class="btn btn-outline-success">חפש</button>
                </form>
                </div>''')        
        dphtml += data_activity.to_html(classes = "table table-hover", border=0)
        with open('elbit-ground-beta/app/templates/show_data_activity.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
            f.close()
        return render_template('show_data_activity.html')


    if request.method == 'POST':
        data_activity = pd.read_csv('elbit-ground-beta/app/db/data_activity.csv')
        position_upload = request.form.get('position_upload')
        specific_position = data_activity.loc[data_activity['סוג מאמן'] == position_upload]

        dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
        r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
        '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
        '\n' + '</a>' + '\n' + '<h1>דוח פעילות מתקן </h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
        '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_activity" dir="rtl" lang="he">' +
        '\n' + '<form action="" method="post">' + '\n' + 
        r'''<div class="col-md-3 form-group">
                <label for="">סוג מאמן</label>
                <select class="form-control" id="exampleFormControlSelect1" name="position_upload">
                    <option>אנא בחר מאמן</option>
                    <option>עמדות פרט</option>
                    <option>משימה 1</option>
                    <option>משימה 2</option>
                    <option>משימה 3</option>
                    <option>משימה 4</option>
                </select>
                <br>
                <form method="POST">
                    <button type="sumbit" class="btn btn-outline-success">חפש</button>
                </form>
                </div>''')        
        dphtml += specific_position.to_html(classes = "table table-hover", border=0)
        with open('elbit-ground-beta/app/templates/show_data_activity.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
            f.close()
        return render_template('show_data_activity.html')

