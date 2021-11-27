from flask import render_template

async def skyLark_mafil_Handler(request):
    if request.method == 'GET':
        return render_template('skyLark/skyLark_mafil.html')