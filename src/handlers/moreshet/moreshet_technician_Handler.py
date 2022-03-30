from flask import render_template

async def moreshet_technician_Handler(request):
    if request.method == 'GET':
        return render_template('moreshet/moreshet_technician.html', title_simulator = "דשבורד טכנאי", second_paragraph = "עַיִן לְצִיּוֹן צוֹפִיָּה")