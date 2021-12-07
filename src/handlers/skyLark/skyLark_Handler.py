from flask import render_template

async def skyLark_Handler(request):
    if request.method == 'GET':
        return render_template('skyLark/skyLark_user.html', title_simulator = "מאמן רוכב שמיים", second_paragraph = "אֵין כָּאֵל יְשֻׁרוּן רֹכֵב שָׁמַיִם בְּעֶזְרֶךָ וּבְגַאֲוָתוֹ שְׁחָקִים")