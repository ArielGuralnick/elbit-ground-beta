from flask import render_template

async def mars_Handler(request):
    if request.method == 'GET':
        return render_template('user.html', title_simulator = "מאמן מרס", second_paragraph = "מרס מרס מרס מרס מרס מרס")