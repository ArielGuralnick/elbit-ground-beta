from flask import render_template

async def literature_Handler(request):
    if request.method == 'GET':
        return render_template('literature.html')