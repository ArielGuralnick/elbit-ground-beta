from flask import render_template

async def driving_Handler(request):
    if request.method == 'GET':
        return render_template('driving/driving_user.html', title_simulator = "מאמני נהיגה", second_paragraph = "משפט של מאמני נהיגה")