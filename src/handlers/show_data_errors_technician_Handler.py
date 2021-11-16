from flask import render_template, send_file
import pandas as pd

async def show_data_errors_technician_Handler(request):
    if request.method == 'GET':       
        important_columns = ['עמדה', 'סוג התקלה', 'הסבר', 'זמן השבתה']
        data_errors = pd.read_csv('elbit-ground-beta/app/db/data_errors.csv')
        
        dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
        r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
        '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
        '\n' + '</a>' + '\n' + '<h1>דוח תקלות לטכנאי</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
        '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
        '\n' + '<form action="" method="post">' + '\n' +
        r'''
          <div class="container">
          <div class="row">
            <div class="col-sm form-group">
              <select class="form-control" id="exampleFormControlSelect1" name="type_of_fault" placeholder='אנא בחר תקלה'>
                <option value="">אנא בחר תקלה</option>
                <option>רזולוציה</option>
                <option>מקודד חוזי</option>
                <option>ריצודי לל"ק</option>
                <option>BE1 לא נפתח ב LOGGER</option>
                <option>בלהה</option>
                <option>בלהההה</option>
              </select>
            </div>
            <div class="col-sm">
            <form method="POST">
              <button type="sumbit" name="options" value="option1" class="btn btn-outline-success">חפש</button>
            </form>
            </div>
            <div class='col-md-3 form-group'>
            <form method="POST">
              <button type="sumbit" name="options" value="option2" class="btn btn-outline-secondary">פתיחת דוח באקסל</button>
            </form>
            </div>
          </div>
          </div>''')        
        dphtml += data_errors.to_html(classes = "table table-hover", border=0, columns=important_columns)
        with open('elbit-ground-beta/app/templates/show_data_errors_technician.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' + '\n' +  r"</div>" + '\n' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
            f.close()
        return render_template('show_data_errors_technician.html')
    


    elif request.method == 'POST':
      if request.form.get('options') == 'option1':
        important_columns = ['עמדה', 'סוג התקלה', 'הסבר', 'זמן השבתה']
        data_errors = pd.read_csv('elbit-ground-beta/app/db/data_errors.csv')
        type_of_fault = request.form.get('type_of_fault')
        specific_error = data_errors.loc[data_errors['סוג התקלה'] == type_of_fault]

        dphtml = (r"{% extends 'layout.html' %}" + '\n' + r"{% block content %}" + '\n' +
        r'<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >' +
        '\n' + '<div>' + '\n' + '<a href="/">' + '\n' + '<img class="Logo" src="static/images/logo.png" alt="logo-img">' +
        '\n' + '</a>' + '\n' + '<h1>דוח תקלות לטכנאי</h1>' + '\n' + '</div>' + '\n' + '</section>' + '\n' +
        '<body style="background-color: rgb(211, 218, 218);">' + '\n' + '<section id="show_data_errors" dir="rtl" lang="he">' +
        '\n' + '<form action="" method="post">' + '\n' +
        r'''
          <div class="container">
          <div class="row">
            <div class="col-sm form-group">
              <select class="form-control" id="exampleFormControlSelect1" name="type_of_fault" placeholder='אנא בחר תקלה'>
                <option value="">אנא בחר תקלה</option>
                <option>רזולוציה</option>
                <option>מקודד חוזי</option>
                <option>ריצודי לל"ק</option>
                <option>BE1 לא נפתח ב LOGGER</option>
                <option>בלהה</option>
                <option>בלהההה</option>
              </select>
            </div>
            <div class="col-sm">
            <form method="POST">
              <button type="sumbit" name="options" value="option1" class="btn btn-outline-success">חפש</button>
            </form>
            </div>
            <div class='col-md-3 form-group'>
            <form method="POST">
              <button type="sumbit" name="options" value="option2" class="btn btn-outline-secondary">פתיחת דוח באקסל</button>
            </form>
            </div>
          </div>
          </div>''')
        dphtml += specific_error.to_html(classes = "table table-hover", border=0, columns=important_columns)
        with open('elbit-ground-beta/app/templates/show_data_errors_technician.html','w', encoding='utf-8-sig') as f:
            f.writelines([dphtml + '\n' + r'<br>' + '\n' + r"</div>" + '\n' + r"</form>" + '\n' + r"</section>" + '\n' + r"</body>" + '\n' + r"{% endblock %}"])
            f.close()
        return render_template('show_data_errors_technician.html')

      elif request.form.get('options') == 'option2':
            return send_file('db/data_errors.csv',
            mimetype='text/csv',attachment_filename='דוח תקלות רוכ"ש.csv',
            as_attachment=True)
      
