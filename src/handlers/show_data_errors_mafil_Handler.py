from flask import render_template
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
            f.writelines([dphtml,r' <form method="POST"><button type="sumbit" class="btn btn-outline-success">עדכן</button></form>',r"</form>",r"</section>",r"</body>" ,r"{% endblock %}"])
            f.close()
        return render_template('show_data_errors_mafil.html')