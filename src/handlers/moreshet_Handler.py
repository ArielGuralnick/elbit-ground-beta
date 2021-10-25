from flask import render_template

async def moreshet_Handler(request):
    if request.method == 'GET':
        return render_template('user.html', title_simulator = "מאמן מורשת", second_paragraph = "מורשת מורשת מורשת מורשת מורשת")