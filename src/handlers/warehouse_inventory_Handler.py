from flask import render_template
import pandas as pd
async def warehouse_inventory_Handler(request):
    if request.method == 'GET':
        return render_template('warehouse_inventory.html')  
    elif request.method == 'POST':
        item_type = request.form.get('th1_1')
        item_type = request.form.get('th1_2')
        item_type = request.form.get('th1_3')
        item_type = request.form.get('th1_4')
        item_type = request.form.get('th1_5')
        item_type = request.form.get('th2_1')
        item_type = request.form.get('th2_2')
        item_type = request.form.get('th2_3')
        item_type = request.form.get('th2_4')
        item_type = request.form.get('th2_5')
        item_type = request.form.get('th3_1')
        item_type = request.form.get('th3_2')
        item_type = request.form.get('th3_3')
        item_type = request.form.get('th3_4')
        item_type = request.form.get('th3_5')
    
        field_content = ['סוג הפריט', 'דגם', 'כמות במלאי', 'נדרש להשלים/לרכוש', 'הערות']
#        data_warehouse_inventory = pd.DataFrame([{'הערות': , 'נדרש להשלים/לרכוש' : , 'כמות במלאי' : , 'דגם' : , 'סוג הפריט' : }])