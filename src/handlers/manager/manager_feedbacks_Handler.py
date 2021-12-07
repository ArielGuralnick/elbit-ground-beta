from flask import render_template, send_file

# ברגע שיהיו לי כל הדפי משובים של כל המאמנים, יהיה אפשר למלא את כל העמוד
async def manager_feedbacks_Handler(request):
    if request.method == 'GET':
        return render_template('manager/manager_feedbacks.html', title_simulator = "משובי מתאמנים", second_paragraph = "אנא בחר מאמן לצפייה במשובי המתאמנים")
    elif request.method == 'POST':
        if request.form.get('options') == 'option_skyLark':
            return send_file('db/skyLark/feedback.csv',
            mimetype='text/csv',attachment_filename='משוב רוכש.csv',
            as_attachment=True)

        elif request.form.get('options') == 'option_mars':
            return send_file('db/mars/feedback.csv',
            mimetype='text/csv',attachment_filename='משוב מרס.csv',
            as_attachment=True)

        elif request.form.get('options') == 'option_moreshet':
            return send_file('db/moreshet/feedback.csv',
            mimetype='text/csv',attachment_filename='משוב מורשת.csv',
            as_attachment=True)

        elif request.form.get('options') == 'option_driving':
            return send_file('db/driving/feedback.csv',
            mimetype='text/csv',attachment_filename='משוב נהיגה.csv',
            as_attachment=True)