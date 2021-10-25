from flask import render_template

async def order_training_Handler(request):
    if request.method == 'GET':
        return render_template('order_training.html')