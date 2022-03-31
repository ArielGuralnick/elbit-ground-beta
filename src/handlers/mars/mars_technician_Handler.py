from flask import render_template

async def mars_technician_Handler(request):
    if request.method == 'GET':
        return render_template('mars/mars_technician.html', title_simulator = "דשבורד טכנאי", second_paragraph = "וְאַתָּ֣ה בֶן־אָדָ֔ם צֹפֶ֥ה נְתַתִּ֖יךָ לְבֵ֣ית יִשְׂרָאֵ֑ל")