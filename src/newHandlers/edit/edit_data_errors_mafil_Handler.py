from flask import render_template, flash, redirect, url_for
import pandas as pd
import time
from newHandlers.simulator import Simulator

async def edit_data_errors_mafil_Handler(request, simulator: Simulator):
    if request.method == 'GET':       
      data = pd.read_csv(f'app/db/{simulator.englishName}/data_errors.csv')
      error = data.index
      
      return render_template('mars/edit/mars_edit_data_errors_mafil.html', data = error)
  
    elif request.method == 'POST':
      if request.form.get('options') == 'option_edit':
        error = int(request.form.get('error'))
        type_of_fault = request.form.get('type_of_fault')
        fault_operation = request.form.get('fault_operation')
        computer = request.form.get('computer')
        situation = request.form.get('situation')
        
        data = pd.read_csv('app/db/mars/data_errors.csv')
        row_to_edit = data.index[error]
        data.loc[row_to_edit,['סוג התקלה','תפעול התקלה','באיזה מחשב','טופל \ לא טופל']] = [type_of_fault,fault_operation,computer,situation]
        with open('app/db/mars/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה עודכנה בהצלחה', category="success")
        return redirect(url_for('mars_show_data_errors_mafil'))
      
      
      if request.form.get('options') == 'option_delet':
        time.sleep(1.5)
        error = int(request.form.get('error'))
        data = pd.read_csv('app/db/mars/data_errors.csv')
        row_to_delet = data.index[error]
        data.drop(row_to_delet, inplace=True, axis=0)
        with open('app/db/mars/data_errors.csv', 'w', newline='', encoding='utf-8-sig') as file:
            data.to_csv(file, index=False, na_rep='N/A',header=file.tell()==0, encoding='utf-8-sig')
            flash(f'!התקלה נמחקה בהצלחה', category="success")
        return redirect(url_for('mars_show_data_errors_mafil'))