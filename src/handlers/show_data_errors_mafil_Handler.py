from flask import render_template, redirect, url_for
import pandas as pd

async def show_data_errors_mafil_Handler(request):
    if request.method == 'GET':       
        data_errors = pd.read_csv('elbit-ground-beta/app/db/data_errors.csv')
        print(data_errors)
        dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
        r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
        '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
        '\n' + '</a>' + '\n' + '<h1>דוח תקלות למפעיל</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
        '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
        '\n' + '<form action="" method="post">' + '\n')        
        dphtml += data_errors.to_html(classes = "table table-hover", border=0)
        with open('elbit-ground-beta/app/templates/show_data_errors_mafil.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' + '\n' + 
            r'''
            <div class="container">
            <div class="row col form-group" style="text-align: center;">
            <form method="POST">
                <button type="sumbit" class="btn btn-outline-success" name="options" value="option1">הוספת תקלה</button>
                <button type="sumbit" class="btn btn-outline-danger" name="options" value="option2">עריכה</button>
            </form>
            </div>
            </div>
            ''' + '\n' + r"</form>",r"</section>",r"</body>" ,r"{% endblock %}"])
            f.close()
        return render_template('show_data_errors_mafil.html')

    elif request.method == 'POST':
        if request.form.get("options") == 'option1':
            return redirect(url_for('insert_error'))
        elif request.form.get("options") == 'option2':
            return redirect(url_for('edit_data_errors_mafil'))