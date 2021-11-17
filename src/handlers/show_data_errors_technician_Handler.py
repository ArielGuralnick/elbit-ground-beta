from flask import render_template, send_file
import pandas as pd

async def show_data_errors_technician_Handler(request):
    if request.method == 'GET':       
        important_columns = ['תאריך','עמדה','סוג התקלה','הסבר','זמן השבתה']
        data_errors = pd.read_csv('elbit-ground-beta/app/db/data_errors.csv')
        
        dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
        r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
        '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
        '\n' + '</a>' + '\n' + '<h1>דוח תקלות לטכנאי</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
        '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
        '\n' + '<form action="" method="post">' + '\n')  
        dphtml += data_errors.to_html(table_id="show_data_errors_technician", classes = "table table-hover", border=0, columns=important_columns)
        with open('elbit-ground-beta/app/templates/show_data_errors_technician.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' +'\n' +
            r'''
            <form method="POST">
              <button type="sumbit" class="btn btn-outline-secondary">פתיחת דוח באקסל</button>
            </form>
            </div>'''   
            r"</form>" + '\n' + r"</section>" + '\n' +
            r'<script type="text/javascript">' + '\n' + r"$('#show_data_errors_technician').DataTable();" + 
            '\n' + r"</script>" + r"</body>" + '\n' + r"{% endblock %}"])
            f.close()
        return render_template('show_data_errors_technician.html')
   
    elif request.method == 'POST':
        return send_file('db/data_errors.csv',
        mimetype='text/csv',attachment_filename='דוח תקלות רוכ"ש.csv',
        as_attachment=True)
      
