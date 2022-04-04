from flask import render_template

async def tzevet_instructor_Handler(request):
    if request.method == 'GET':
        return render_template('tzevet/tzevet_instructor.html', title_simulator = "דשבורד מדריכה", second_paragraph = "משפט של מאמני צוותתתתתת")