from flask import render_template

async def moreshet_mafil_Handler(request):
    if request.method == 'GET':
        return render_template('moreshet/moreshet_mafil.html', title_simulator = "דשבורד מדריך טכני", second_paragraph = "עַיִן לְצִיּוֹן צוֹפִיָּה")