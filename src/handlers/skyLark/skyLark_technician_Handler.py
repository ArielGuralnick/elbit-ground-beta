from flask import render_template

async def skyLark_technician_Handler(request):
    if request.method == 'GET':
        return render_template('technician.html', title_simulator = "עמדת טכנאי", second_paragraph = "אֵין כָּאֵל יְשֻׁרוּן רֹכֵב שָׁמַיִם בְּעֶזְרֶךָ וּבְגַאֲוָתוֹ שְׁחָקִים")