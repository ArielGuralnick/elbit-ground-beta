from flask import render_template

async def tzevet_mafil_Handler(request):
    if request.method == 'GET':
        return render_template('tzevet/tzevet_mafil.html', title_simulator = "דשבורד מפעיל", second_paragraph = "משפט של מאמני צוותתתתתת")