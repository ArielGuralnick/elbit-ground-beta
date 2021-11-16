from flask import render_template

async def manager_feedbacks_Handler(request):
    if request.method == 'GET':
        return render_template('manager_feedbacks.html', title_simulator = "משובי מתאמנים", second_paragraph = "משובי המתאמנים במאמנים בלה בלה בלה")