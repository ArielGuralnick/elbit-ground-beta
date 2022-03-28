from flask import render_template

async def mini_raam_Handler(request):
    if request.method == 'GET':
        return render_template('mini_raam/mini_raam.html', title_simulator = "עמדת טכנאי ומשובים", second_paragraph = "משפט של מיני רעם")