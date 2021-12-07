from flask import render_template, flash, redirect, url_for
import pandas as pd
from pandas.core.indexes.base import Index

async def moreshet_edit_data_errors_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('elbit-ground-beta/app/db/moreshet/data_errors.csv')
      error = data.index
      
      dphtml = (r'''
{% extends 'layout.html' %}
{% block content %}
<section id="title" style="background-color: rgb(244, 248, 248); border-bottom: 3px solid var(--black);" >
<div>
  <a href="/"><img class="Logo" src="static/images/logo.png" alt="logo-img"></a>
  <h1>עריכת תקלה</h1>
</div>
</section>
<body style="background-color: rgb(211, 218, 218);">
<section id="show_data_errors" dir="rtl" lang="he">
<form action="" method="post">''')       
      with open('elbit-ground-beta/app/templates/moreshet/edit/moreshet_edit_data_errors_mafil.html','w', encoding='utf-8-sig') as f:
        f.writelines([dphtml + '\n' + r'''
<div class="col form-group">
<label>למחיקת שורה יש דבר לבחור רק מספר תקלה</label>
</div>
<div class="row">
<div class="col form-group">
  <label for="">בחר מספר תקלה</label>
  <select class="form-control" name="error">
    {% for i in data %}
      <option>{{ i }}</option>
    {% endfor %}
  </select>
</div>
<div class="col form-group">
    <label for="">סוג התקלה</label>
    <select class="form-control" name="type_of_fault">
              <option>מחולל:</option>
              <option>תקלה כלשהי שיש אצל עדי</option>
              <option>'הרצת תרגיל' מואפר</option>
              <option>מחולל זירה תקוע/לא מגיב</option>
              <option>ישויות לא התפקדו לעמדת ייצוג</option>
              <option>'מיפוי סד"כ' מואפר</option>
              <option>"איקסים צהובים"/ישויות נמחקו מהדו-מימד (BE1 קרס)</option>
              <option>"שרת הנתונים לא עובד נא להדליקו"</option>
              <option>"שרת המשאבים לא עובד נא להדליקו"</option>
              <option>"הפצת תרגיל רשת נכשלה"</option>
              <option>תרגיל קרס/ נסגר (simengine קרס)</option>
              <option>NICE SENDER/RECIVER נאלץ להסגר/ לא עולה </option>
              <option>TVEIW:</option>
              <option>TVIEW לא נטען</option>
              <option>TVIEW קרס/נסגר (עם עליית שגיאה)</option>
              <option>TVIEW תקוע- אמצעי לא זז</option>
              <option>לא רואים ישויות ב TVIEW</option>
              <option>תקלת HASP בtview</option>
              <option>תקלת TVIEWBARAK.EXE</option>
              <option>חומרה:</option>
              <option>מחשב תקוע</option>
              <option>תצוגת מסך שחורה</option>
              <option>מקלדת לא עובדת</option>
              <option>עכבר לא פעיל</option>
              <option>מחשב לא עולה (תקוע בהתחלה על HP וכד)</option>
              <option> גויסטיק PTT לא עובד</option>
              <option>עמדות :</option>
              <option>"תקלת תקשורת יחצ"ג"</option>
              <option>תקלת תקשורת "קופסת אל/מיטל/אלקטקרוניקה"</option>
              <option>נץ נפתח עם שגיאה ונסגר לאחר יציאה מהתקלה</option>
              <option>נץ לא קופץ לאזימוט נכון</option>
              <option>נץ לא משויך לעמדה</option>
              <option>לא ניתן לקפוץ לנק' באפליקציה מכ"ם</option>
              <option>פונקצית לזירה לא עובדת</option>
              <option>נץ לא עולה -חלון שחור שורות רצות -אין רשת </option>
              <option>שיגאת MMI - לפרט בהערות מה התקלה בעקבות השגיאה </option>
              <option>אפליקציות לא עולות בעמדה (רשיון)</option>
              <option>אין גילויים במכ"ם /מכ"ם לא עובד תקין </option>
              <option>משואה:</option>
              <option>פונקציות עריכה במשואה לא פעילות</option>
              <option>איתורים לא מתעדכנים בשאר הכיתה</option>
              <option>הגעת למס' ישויות מקסימלי במשואה</option>
              <option>קשר:</option>
              <option>רעש חשמלי בקשר</option>
              <option>אין שמע/דיבור</option>
              <option>"שורות אדומות"-קשר מנותק </option>
              <option>כללי:</option>
              <option>מסכי מיתוג לא עובדים (משבצת ורודה בפארגון)</option>
              <option>תקלת רשיונות</option>
              <option>אחר</option>
            </select>
    <br>
</div>
<div class="col form-group">
    <label for="">תפעול התקלה</label>
            <select class="form-control" name = "fault_operation" placeholder="אנא בחר מהרשימת תפעול תקלות">
              <option>אנא בחר מהרשימת תפעול תקלות</option>
              <option>Restart best</option>
              <option>Recover ios</option>
              <option>אתחול עמדה "הפלת עמדה"</option>
              <option>Start preasentaion</option>
              <option>יציאה מתרגיל והעלאת תרגיל חדש</option>
              <option>כיבוי והדלקת מחשב דרך חדר מחשבים</option>
              <option>אתחול מחשב</option>
              <option>אתחול מחשבי הכיתה דרך תקיית shutdown</option>
              <option>אתחול מחשבי עמדה</option>
              <option>אתחול מחשבי מכלול</option>
              <option>אתחול אפליקציית משואה</option>
              <option>LOG OFF-LOG IN</option>
              <option>העלאת RADARGETWAY- LOGGER</option>
              <option>העלאה ידנית של DBSERVER</option>
              <option>העלאה ידנית של NICE RECIVER/SENDER</option>
              <option>שיוך מכמ"ים ידנית</option>
              <option>אתחול רשיונות</option>
              <option>כיבוי והדלקה לפארגון</option>
              <option>שינוי רזולוציות מסך</option>
              <option>הרמת פחת מפצל שקעים</option>
              <option>חיזוק חיבורים</option>
              <option>החלפת רכיב</option>
              <option>העתקת תיקיית נץ</option>
              <option>שימוש במסכי מיתוג</option>
              <option>שפיכת אימאג' וקונפיגורציה</option>
              <option>אחר</option>
            </select>
    <br>
</div>
</div>

<div class="row">
<div class="col form-group">
    <label for="">סוג עמדה</label>
    <select class="form-control" name="type_of_position">
        <option>עמדה 1</option>
        <option>עמדה 2</option>
        <option>עמדה 3</option>
        <option>עמדה 4</option>
        <option>מדריך</option>
        <option>כל הכיתה</option>  
    </select>
    <br>
</div>
<div class="col form-group">
    <label for="">באיזה מחשב</label>
    <select class="form-control" name="computer" id="exampleFormControlSelect1">
        <option>LOG</option>
        <option>BCNT</option>
        <option>IN1</option>
        <option>IN2</option>
        <option>TRN</option>
        <option>TRS</option>
        <option>TRM</option>
        <option>קשר</option>
    </select>
    <br>
</div>
<div class="col form-group">
  <label for="">טופל \ לא טופל</label>
  <select class="form-control" name = "situation">
    <option>V</option>
    <option>X</option>
  </select>
  <br>
</div>
</div>

<div class="container">
  <div class="col form-group" style="text-align: center;">
    <form method="POST">
      <button type="sumbit" name="options" value="option_edit" class="btn btn-outline-success">עדכן</button>
      <button type="sumbit" name="options" value="option_delet" class="btn btn-outline-danger">מחיקת שורה</button>
    </form>
  </div>
</div>
</div>
</form>
</section>
</body>
{% endblock %}'''])
        f.close()
      return render_template('moreshet/edit/moreshet_edit_data_errors_mafil.html', data = error)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        error = int(request.form.get('error'))

        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        type_of_position = request.form.get('type_of_position')
        computer = request.form.get('computer')
        situation = request.form.get('situation')
        
        data = pd.read_csv('elbit-ground-beta/app/db/moreshet/data_errors.csv')
        row_to_edit = data.index[error]
        data.loc[row_to_edit,['סוג התקלה','תפעול התקלה','סוג עמדה','באיזה מחשב','טופל \ לא טופל']] = [type_of_fault,fault_operation,type_of_position,computer,situation]
        with open('elbit-ground-beta/app/db/moreshet/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה עודכנה בהצלחה', category="success")
        return redirect(url_for('moreshet_show_data_errors_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        error = int(request.form.get('error'))
        data = pd.read_csv('elbit-ground-beta/app/db/moreshet/data_errors.csv')
        row_to_delet = data.index[error]
        data.drop(row_to_delet, inplace=True, axis=0)
      
        with open('elbit-ground-beta/app/db/moreshet/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נמחקה בהצלחה', category="success")
        return redirect(url_for('moreshet_show_data_errors_mafil'))