from flask import render_template

async def sheder_Handler(request):
    if request.method == 'GET':
        return render_template('sheder/sheder_user.html', title_simulator = "מאמן שדר חם", second_paragraph = "משפט תנכי של שדר חם")