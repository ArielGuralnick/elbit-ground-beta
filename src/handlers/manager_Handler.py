from flask import render_template

async def manager_Handler(request):
    if request.method == 'GET':
        return render_template('manager.html', title_simulator = "דף ניהולי", second_paragraph = "עבור אייל ורעות עחאןעחםןהגםהקהכ")