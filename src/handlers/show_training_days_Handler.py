from flask import render_template, send_file
import pandas as pd


async def show_training_days_Handler(request):
    if request.method == 'GET':       
      data_training = pd.read_csv('elbit-ground-beta/app/db/order_training.csv')
        
      dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
      r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
      '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
      '\n' + '</a>' + '\n' + '<h1>דוח סיכום ימי אימון</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
      '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
      '\n' + '<form action="" method="post">' + '\n')        
      dphtml += data_training.to_html(table_id="show_activity", classes = "table table-hover", border=0)
      with open('elbit-ground-beta/app/templates/show_training_days.html','w', encoding='utf-8-sig') as f:
          f.writelines([dphtml + '\n' + r'<br>' + '\n' + 
        r'''
        <div class='col-md-3 form-group'>
        <form method="POST">
        <button type="sumbit" name="options" value="option3" class="btn btn-outline-secondary">פתיחת דוח באקסל</button>
        </form>
        </div>
        ''' + r"</form>" + '\n' + r"</section>" + '\n' +
        r'<script type="text/javascript">' + '\n' + r"$('#show_activity').DataTable();" + 
          '\n' + r"</script>" +'\n' + r"</body>" + '\n' + r"{% endblock %}"])
          f.close()
      return render_template('show_training_days.html')

    if request.method == 'POST':   
      return send_file('db/order_training.csv',
      mimetype='text/csv',attachment_filename='Full_Training_days.csv',
      as_attachment=True)
    
