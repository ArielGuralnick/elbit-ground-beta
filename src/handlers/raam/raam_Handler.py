from flask import render_template

async def raam_Handler(request):
    if request.method == 'GET':
        return render_template('raam/raam.html', title_simulator = "עמדת טכנאי ומשובים", second_paragraph = "משפט כלשהו של רעם")