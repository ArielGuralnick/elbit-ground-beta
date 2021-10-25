import pandas as pd
from flask import render_template, flash, redirect, url_for


async def feedback_Handler(request):
    if request.method == 'GET':
        return render_template('feedback.html', title_simulator = "מאמן רוכב שמיים")
    elif request.method == 'POST':
        question_1 = request.form.get('question_1')
        question_2 = request.form.get('question_2')
        question_3 = request.form.get('question_3')
        question_4 = request.form.get('question_4')
        question_5 = request.form.get('question_5')
        print(question_1, question_2,question_3,question_4,question_5)
        field_content = ['אנא דרג את איכות האימון','לפי דעתך עד כמה המאמן מתאר את המציאות','עד כמה אתה מרגיש בנוח בתפעול המאמן','עד כמה אתה מת עכשיו להיות בתאילנד','עד כמה אתה מת לאכול עכשיו פיצה']
        feedback_information = pd.DataFrame([{'אנא דרג את איכות האימון' : question_1, 'לפי דעתך עד כמה המאמן מתאר את המציאות' : question_2, 'עד כמה אתה מרגיש בנוח בתפעול המאמן' : question_3, 'עד כמה אתה מת עכשיו להיות בתאילנד' : question_4, 'עד כמה אתה מת לאכול עכשיו פיצה' : question_5}], columns=field_content)
        with open('elbit-ground-beta/app/db/feedback.csv', 'a', newline='', encoding='utf-8-sig') as file:
            feedback_information.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'המשוב נקלט בהצלחה! תודה!', category="success")
        return redirect(url_for('skyLark_instructor'))