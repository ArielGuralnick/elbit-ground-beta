from flask import render_template

async def sheder_technician_Handler(request):
    if request.method == 'GET':
        return render_template('sheder/sheder_technician.html', title_simulator = "דשבורד טכנאי", second_paragraph = "משפט תנכייי של שדר חם")