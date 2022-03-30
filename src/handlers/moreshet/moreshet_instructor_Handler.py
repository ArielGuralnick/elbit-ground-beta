from flask import render_template

async def moreshet_instructor_Handler(request):
    if request.method == 'GET':
        return render_template('moreshet/moreshet_instructor.html', title_simulator = "דשבורד מדריכה", second_paragraph = "עַיִן לְצִיּוֹן צוֹפִיָּה")