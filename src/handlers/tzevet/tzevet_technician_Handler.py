from flask import render_template

async def tzevet_technician_Handler(request):
    if request.method == 'GET':
        return render_template('tzevet/tzevet_technician.html', title_simulator = "עמדת טכנאי", second_paragraph = "משפט של מאמני צוווותתתתת")