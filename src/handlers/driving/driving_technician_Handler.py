from flask import render_template

async def driving_technician_Handler(request):
    if request.method == 'GET':
        return render_template('driving/driving_technician.html', title_simulator = "עמדת טכנאי", second_paragraph = "משפט של מאמני נהיגה")