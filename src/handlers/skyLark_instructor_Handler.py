from flask import render_template

async def skyLark_instructor_Handler(request):
    if request.method == 'GET':
        return render_template('skyLark_instructor.html', title_simulator = "מאמן רוכב שמיים")