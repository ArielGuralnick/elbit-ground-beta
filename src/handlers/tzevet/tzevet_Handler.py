from flask import render_template

async def tzevet_Handler(request):
    if request.method == 'GET':
        return render_template('tzevet/tzevet_user.html', title_simulator = "מאמני צוות", second_paragraph = "משפט של מאמני צוותתתתתת")