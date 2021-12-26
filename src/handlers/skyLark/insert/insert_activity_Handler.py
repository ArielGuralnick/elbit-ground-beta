import pandas as pd
from src.types.Simulator import Simulator
from flask import render_template, flash, redirect, url_for
import psycopg2

async def insert_activity_Handler(request):
    if request.method == 'GET':
        return render_template('skyLark/insert/insert_activity.html')
    elif request.method == 'POST':
        position_upload = request.form.get('position_upload')
        number_training = request.form.get('number_training')
        date_upload = request.form.get('date_upload')
        group_training = request.form.get('group_training')
        name_updater = request.form.get('name_updater')
        time_upload = request.form.get('time_upload')
        name_downloader = request.form.get('name_downloader')
        time_download = request.form.get('time_download')

        con = psycopg2.connect(database='elbit_ground_simulators', user='postgres', password='Integ123', host="127.0.0.1", port="5432")
        print("Database opened successfully")
        cur = con.cursor()
        
        #cur.execute('''CREATE TABLE skylark_data_activity_4
        #    (aaa CHAR(50)   NOT NULL,
        #    bbb  CHAR(50)   NOT NULL,
        #    ccc   DATE     NOT NULL,
        #    ddd CHAR(50)   NOT NULL,
        #    eee CHAR(50)   NOT NULL,
        #    fff  TIME      NOT NULL,
        #    ggg  CHAR(50)  NOT NULL,
        #    hhh  TIME      NOT NULL);''')
        #print("Table created successfully")

        postgres_insert_query = """ INSERT INTO skylark_data_activity_4 (aaa,bbb,ccc,ddd,eee,fff,ggg,hhh) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (position_upload,number_training, date_upload, group_training, name_updater, time_upload, name_downloader, time_download)
        cur.execute(postgres_insert_query, record_to_insert)

        con.commit()
        print("Record inserted successfully")
        con.close()

        field_content = ['סוג מאמן', 'מספר אימון', 'תאריך העלאה', 'פעילות עבור','שם המעלה', 'שעת התחלה', 'שם המורידה', 'שעת סיום']
        data_activity = pd.DataFrame([{'סוג מאמן': position_upload, 'מספר אימון' : number_training, 'תאריך העלאה' : date_upload,
        'פעילות עבור' : group_training, 'שם המעלה' : name_updater,'שעת התחלה' : time_upload,
        'שם המורידה' : name_downloader, 'שעת סיום' : time_download}], columns=field_content)
        with open('elbit-ground-beta/app/db/skyLark/data_activity.csv', 'a', newline='', encoding='utf-8-sig') as file:
            data_activity.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding = "utf-8-sig")
            flash(f'התיעוד נשלח בהצלחה!', category="success")
        return redirect(url_for('skyLark_instructor'))
