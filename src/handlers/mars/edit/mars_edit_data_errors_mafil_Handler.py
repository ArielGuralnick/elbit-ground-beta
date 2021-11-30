from flask import render_template, flash, redirect, url_for
import pandas as pd
from pandas.core.indexes.base import Index

async def mars_edit_data_errors_mafil_Handler(request):
    if request.method == 'GET':       
      data = pd.read_csv('elbit-ground-beta/app/db/mars/data_errors.csv')
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
      with open('elbit-ground-beta/app/templates/mars/edit/mars_edit_data_errors_mafil.html','w', encoding='utf-8-sig') as f:
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
              <option>אנא בחר מהרשימת תקלות</option>
              <option>אפליקציית מר"ס לא עולה (שגיאה beacon fail)</option>
              <option>אמצעים לא כשירים בעמדה מבצעית</option>
              <option>מקלדת מר"ס לא עובדת</option>
              <option>מסך עליון שחור</option>
              <option>מסך עליון במסך תחתון ומסך עליון שחור</option>
              <option>תצוגת מסכים בעמדה מבצעית לא תקינים</option>
              <option>משימות לא עוברות לעמדת חקירה</option>
              <option>משימות לא נכנסות לעמדת ניטור</option>
              <option>קשר לא עובד</option>
              <option>אמצעי בעמדה בצבע ירוק</option>
              <option>בעמדה "וידיאו לא זמין"</option>
              <option>עמדת שליטה:</option>
              <option>אמצעי לא קיים בשיבוץ אמצעים –אמצעי על גזרתי</option>
              <option>אמצעים לא נכנסים לתא</option>
              <option>שקשוק לא עובד</option>
              <option>לחיצה על פונקציות במשואה לא עובד</option>
              <option>מחולל זירה:</option>
              <option>'הרצת תרגיל' מואפר</option>
              <option>'מיפוי סד"כ' מואפר</option>
              <option>אפליקציה מחולל זירה קרסה/תקועה</option>
              <option>מפת דו- מימד נעלמת (צג אפור)</option>
              <option>שגיאה close program –vrf</option>
              <option>שגיאה close program –Tview barak</option>
              <option>שגיאה close program –SimEngine off</option>
              <option>ישות נמחקו מהדו-מימד</option>
              <option>קליק ימני על ישות לא פותח תפריט רצוי </option>
              <option>כל האמצעים לא עלו בתרגיל </option>
              <option>משתמש נעול –החלפת סיסמה</option>
              <option>"שרת נתונים לא עובד נא להדליקו"</option>
              <option>"הפצת תרגיל רשת נכשלה"</option>
              <option>לא נוצרות משימות במחולל</option>
              <option>עמדת ייצוג לא עולה –שגיאה license</option>
              <option>תצוגת חוזי לא תקינה</option>
              <option>לא רואים ישויות בחוזי (דרך SVM)</option>
              <option>מסכי מיתוג לא עובדים (משבצת ורודה)</option>
              <option>ישויות לא התפקדו לעמדת ייצוג</option>
              <option>תרגיל תקוע ברשת</option>
              <option>אמצעי לא זז (ב SVM כשמזיזים את הקרן במחולל )</option>
              <option>NICE SENDER/RECIVER קרס</option>
              <option>Ness לא עובד (אין תצוגת הקלטות)</option>
              <option>אין תצוגה במחשבי Ness</option>
              <option>חומרה:</option>
              <option>מחשב תקוע</option>
              <option>חוזק רשת 100MB</option>
              <option>מחשב לא נמצא ב TOP.SECRET</option>
              <option>מקלדת לא עובדת עמדת מחולל </option>
              <option>הפסקת חשמל</option>
              <option>מקליט וידאו לא עובד בעמדה</option>
              <option>חלק מהמחשבים לא נדלקים</option>
              <option>אחר</option> 
            </select>
    <br>
</div>
<div class="col form-group">
    <label for="">תפעול התקלה</label>
            <select class="form-control" name = "fault_operation" placeholder="אנא בחר מהרשימת תפעול תקלות">
              <option>אנא בחר מהרשימת תפעול תקלות</option>
              <option>אתחול מחשב</option>
              <option>אתחול מחשבי מכלול</option>
              <option>אתחול שרת אמצעי</option>
              <option>אתחול עמדה מבצעית</option>
              <option>אתחול ברקודה/ממיר וידאו</option>
              <option>פתיחת מחשב MGW עם סיסמה</option>
              <option>פתיחת מחשב BCNT עם סיסמה</option>
              <option>LOG OFF-LOG IN</option>
              <option>אתחול סיסמת משתמש</option>
              <option>יציאה מתרגיל והעלאה מחדש</option>
              <option>restart best</option>
              <option>Recover ios</option>
              <option>Start preasentaion</option>
              <option>העלאה ידנית marsGW</option>
              <option>MGW- refresh device name</option>
              <option>העלאה ידנית Dbserver</option>
              <option>חיבור לרשת Top.secret</option>
              <option>הגדרת עמדת יצוג ואתחול עמדה</option>
              <option>אתחול מחשבים + אתחול שרת נתונים</option>
              <option>שינוי פורט ב nice reciver</option>
              <option>שינוי הגדרת מסך</option>
              <option>חיזוק חיבורים</option>
              <option>החלפת רכיב</option>
              <option>אתחול UST</option>
              <option>הרמת מפסקים ח.מחשבים</option>
              <option>תפעול מרחוק של HD</option>
              <option>עץ חמל הגדרת תא גזרתי/עמדות</option>
              <option>הגדרת שיבוץ אמצעים ועמדות</option>
              <option>שקשור החלפה תצוגה ידני</option>
              <option>לחיצה על 2 במקלדת (בחוזי של SVM)</option>
              <option>קריאה למפעיל</option>
              <option>אחר</option>
            </select>
    <br>
</div>
</div>

<div class="row">
<div class="col form-group">
    <label for="">סוג עמדה</label>
    <select class="form-control" name="type_of_position">
        <option>מבצעית</option>
        <option>עמדת מדריך</option>
        <option>כל הכיתה</option>    
    </select>
    <br>
</div>
<div class="col form-group">
    <label for="">באיזה מחשב</label>
    <select class="form-control" name="computer" id="exampleFormControlSelect1">
      <option>MGW</option>
      <option>BCNT</option>
      <option>IN1</option>
      <option>IN2</option>
      <option>SVM</option>
      <option>קשר</option>
      <option>אחר</option>
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
      return render_template('mars/edit/mars_edit_data_errors_mafil.html', data = error)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        error = int(request.form.get('error'))

        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        type_of_position = request.form.get('type_of_position')
        computer = request.form.get('computer')
        situation = request.form.get('situation')
        
        data = pd.read_csv('elbit-ground-beta/app/db/mars/data_errors.csv')
        row_to_edit = data.index[error]
        data.loc[row_to_edit,['סוג התקלה','תפעול התקלה','סוג עמדה','באיזה מחשב','טופל \ לא טופל']] = [type_of_fault,fault_operation,type_of_position,computer,situation]
        with open('elbit-ground-beta/app/db/mars/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה עודכנה בהצלחה', category="success")
        return redirect(url_for('mars_show_data_errors_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        error = int(request.form.get('error'))
        data = pd.read_csv('elbit-ground-beta/app/db/mars/data_errors.csv')
        row_to_delet = data.index[error]
        data.drop(row_to_delet, inplace=True, axis=0)
      
        with open('elbit-ground-beta/app/db/mars/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נמחקה בהצלחה', category="success")
        return redirect(url_for('mars_show_data_errors_mafil'))