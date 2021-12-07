from flask import render_template

async def mars_Handler(request):
    if request.method == 'GET':
        return render_template('mars/mars_user.html', title_simulator = "מאמן מרס", second_paragraph = "וְאַתָּ֣ה בֶן־אָדָ֔ם צֹפֶ֥ה נְתַתִּ֖יךָ לְבֵ֣ית יִשְׂרָאֵ֑ל")