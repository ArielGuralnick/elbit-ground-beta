import pandas as pd
from flask import render_template, flash, redirect, url_for
import time

async def skyLark_feedback_Handler(request):
    answer_1 = None
    answer_2 = None
    answer_3 = None
    answer_4 = None
    answer_5 = None
    if request.method == 'GET':
        return render_template('feedback.html', title_simulator = "משוב מאמן רוכב שמיים")
    elif request.method == 'POST':
        time.sleep(1.5)
        if request.form.get("question1") == 'ques1-5':
            answer_1 = "5"
        elif request.form.get("question1") == 'ques1-4':
            answer_1 = "4"
        elif request.form.get("question1") == 'ques1-3':
            answer_1 = "3"
        elif request.form.get("question1") == 'ques1-2':
            answer_1 = "2"
        elif request.form.get("question1") == 'ques1-1':
            answer_1 = "1"
        
        if request.form.get("question2") == 'ques2-5':
            answer_2 = "5"
        elif request.form.get("question2") == 'ques2-4':
            answer_2 = "4"
        elif request.form.get("question2") == 'ques2-3':
            answer_2 = "3"
        elif request.form.get("question2") == 'ques2-2':
            answer_2 = "2"
        elif request.form.get("question2") == 'ques2-1':
            answer_2 = "1"
        
        if request.form.get("question3") == 'ques3-5':
            answer_3 = "5"
        elif request.form.get("question3") == 'ques3-4':
            answer_3 = "4"
        elif request.form.get("question3") == 'ques3-3':
            answer_3 = "3"
        elif request.form.get("question3") == 'ques3-2':
            answer_3 = "2"
        elif request.form.get("question3") == 'ques3-1':
            answer_3 = "1"
        
        if request.form.get("question4") == 'ques4-5':
            answer_4 = "5"
        elif request.form.get("question4") == 'ques4-4':
            answer_4 = "4"
        elif request.form.get("question4") == 'ques4-3':
            answer_4 = "3"
        elif request.form.get("question4") == 'ques4-2':
            answer_4 = "2"
        elif request.form.get("question4") == 'ques4-1':
            answer_4 = "1"

        if request.form.get("question5") == 'ques5-5':
            answer_5 = "5"
        elif request.form.get("question5") == 'ques5-4':
            answer_5 = "4"
        elif request.form.get("question5") == 'ques5-3':
            answer_5 = "3"
        elif request.form.get("question5") == 'ques5-2':
            answer_5 = "2"
        elif request.form.get("question5") == 'ques5-1':
            answer_5 = "1"
        field_content = ['אנא דרג את איכות האימון','לפי דעתך עד כמה המאמן מתאר את המציאות','עד כמה אתה מרגיש בנוח בתפעול המאמן','עד כמה אתה מת עכשיו להיות בתאילנד','עד כמה אתה מת לאכול עכשיו פיצה']
        feedback_information = pd.DataFrame([{'אנא דרג את איכות האימון' : answer_1,
        'לפי דעתך עד כמה המאמן מתאר את המציאות' : answer_2,
        'עד כמה אתה מרגיש בנוח בתפעול המאמן' : answer_3,
        'עד כמה אתה מת עכשיו להיות בתאילנד' : answer_4,
        'עד כמה אתה מת לאכול עכשיו פיצה' : answer_5}], columns=field_content)
        with open('elbit-ground-beta/app/db/skyLark/feedback.csv', 'a', newline='', encoding='utf-8-sig') as file:
            feedback_information.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'המשוב נשלח בהצלחה! תודה', category="success")
        return redirect(url_for('skyLark_instructor'))