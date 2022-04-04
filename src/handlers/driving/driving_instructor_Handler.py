from flask import render_template

async def driving_instructor_Handler(request):
    if request.method == 'GET':
        return render_template('driving/driving_instructor.html', title_simulator = "דשבורד מדריכה", second_paragraph = "משפט של מאמני נהיגה")