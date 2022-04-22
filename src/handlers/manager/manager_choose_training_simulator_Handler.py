from flask import render_template,send_file

async def manager_choose_training_simulator_Handler(request):
    if request.method == 'GET':
        return render_template('manager/manager_choose_training_simulator.html', title_simulator = "דוחות הזמנת ימי אימון", second_paragraph = "אנא בחר מאמן לצפייה בדוח הזמנת ימי אימון")
    elif request.method == 'POST':
        if request.form.get('options') == 'option_shotef':
            return send_file('db/manager/order_training.csv',
            mimetype='text/csv',attachment_filename='דוחות הזמנת ימי אימון רוכ"ש מרס ומורשת.csv',
            as_attachment=True)

        elif request.form.get('options') == 'option_driving':
            return send_file('db/manager/driving_order_training.csv',
            mimetype='text/csv',attachment_filename='דוח הזמנת ימי אימון מאמני נהיגה.csv',
            as_attachment=True)

        elif request.form.get('options') == 'option_tzevet':
            return send_file('db/manager/tzevet_order_training.csv',
            mimetype='text/csv',attachment_filename='דוח הזמנת ימי אימון מאמני צוות.csv',
            as_attachment=True)

        elif request.form.get('options') == 'option_sheder':
            return send_file('db/manager/sheder_order_training.csv',
            mimetype='text/csv',attachment_filename='דוח הזמנת ימי אימון מאמני שדר חם.csv',
            as_attachment=True)