from flask import render_template

async def mars_mafil_Handler(request):
    if request.method == 'GET':
        return render_template('mars/mars_mafil.html', title_simulator = "עמדת מפעיל", second_paragraph = "וְאַתָּ֣ה בֶן־אָדָ֔ם צֹפֶ֥ה נְתַתִּ֖יךָ לְבֵ֣ית יִשְׂרָאֵ֑ל")