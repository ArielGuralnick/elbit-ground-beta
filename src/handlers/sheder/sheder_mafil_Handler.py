from flask import render_template

async def sheder_mafil_Handler(request):
    if request.method == 'GET':
        return render_template('sheder/sheder_mafil.html', title_simulator = "עמדת מפעיל", second_paragraph = "משפט תנכי של שדררר חם")