from flask import render_template,send_file


async def training_package_Handler(request):
    if request.method == 'GET':
        return render_template('training_package.html')
    if request.method == 'POST':
        if request.form.get('options') == 'option_meholel_advanced':
            return send_file('meholel_advanced.pptx',
            mimetype='text/csv', attachment_filename='מצגת מחולל זירה מתקדמת',
            as_attachment=True)
        elif request.form.get('options') == 'option_kamas':
            return send_file('kamas.pptx',
            attachment_filename='הכרת המאמן לקמ"ס',
            as_attachment=True)
        elif request.form.get('options') == 'option_meholel_basic':
            return send_file('meholel_basic.pptx',
            attachment_filename='סדנת מחולל בסיסית',
            as_attachment=True)