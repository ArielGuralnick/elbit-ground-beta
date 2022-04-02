from flask import render_template

async def driving_mafil_Handler(request):
    if request.method == 'GET':
        return render_template('driving/driving_mafil.html', title_simulator = "דשבורד מפעיל", second_paragraph = "משפט של מאמני נהיגה")