from flask import render_template

async def skyLark_technician_Handler(request):
    if request.method == 'GET':
        return render_template('skyLark/skyLark_technician.html')